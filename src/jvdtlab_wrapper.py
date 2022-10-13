import sys
import win32com.client

class JVDTLab:

    # DLL管理用インスタンス
    _instance = None

    def __init__(self):
        '''
        コンストラクタ
        '''

        self._instance = win32com.client.Dispatch('JVDTLab.JVLink')

    def JVInit(self, sid : str) -> int:
        '''
        JVInit は JV-Link の初期化のために必ず最初に呼び出さなければなりません(※)。JVInit は
        JV-Link が使用する変数などのリソースを初期化します。サーバーとの通信は行なわれません。
        JVInit は自身のプロパティをレジストリの内容で初期化しますが、JVSetUIProperties を呼び出し
        た後に変更されたレジストリの内容を読み込ませるという理由で再度JVInit を呼び出す必要はあり
        ません。JVOpen あるいは JVRTOpen により変更されたレジストリ内容は再度読み込まれます。
        ※アプリケーションの初期化時に呼び出しを行ってください。JVOpen あるいは JVRTOpen の都度
        呼び出す必要はありません。
        '''

        return self._instance.JVInit(sid)

    def JVSetUIProperties(self) -> int:
        '''
        JV-Link が持つプロパティのうちエンドユーザーによって変更可能な項目について値を変更するた
        めのダイアログ表示と値のセットを行います。
        '''

        return self._instance.JVSetUIProperties()

    def JVSetServiceKey(self, service_key : str) -> int:
        '''
        利用キーが正しくセットされた場合は0、 指定された値が不正である場合あるいはエラー発生によ
        り終了した場合は-100が返り、値はレジストリにセットされません。(利用キーが設定済の場合は、
        利用キーは変更不可となります。)
        '''

        return self._instance.JVSetServiceKey(service_key)

    def JVSetSaveFlag(self, save_flag : int) -> int:
        '''
        JVSetSaveFlag メソッドで利用キーを設定するとその値がレジストリに保存され、 それ以降
        JVInit,JVOpen,JVRTOpen を呼び出したタイミングでこのレジストリの値が使用されます。
        '''

        return self._instance.JVSetSaveFlag(save_flag)

    def JVSetSavePath(self, save_path : str) -> str:
        '''
        JVSetSavePath メソッドで保存パスを設定するとその値がレジストリに保存され、 それ以降
        JVInit,JVOpen,JVRTOpen を呼び出したタイミングでこのレジストリの値が使用されます。
        実際に JV-Data が保存されるのはここで指定されたパスの下に自動的に作成される”cache”
        と”data”フォルダになります。”cache”と”data”フォルダが存在しない場合には JVOpen,JVRTOpen
        が自動的に作成しますが、保存パスそのものが存在しない場合には JVOpen,JVRTOpen は「－２１
        １」（レジストリ内容が不正）エラーとなります。したがってこの JVSetSavePath メソッドで設定する保
        存パスは存在するパスを指定する必要があります。
        '''

        return self._instance.JVSetSaveFlag(save_path)

    def JVOpen(self, data_spec : str, from_time : str, option : int) -> list:
        '''
        読み出したいデータを識別するデータ種別IDを文字列として連結したものを指定します。１つ
        のデータ種別IDは４桁固定ですので dataspec に指定する文字列は４の倍数桁でなければい
        けません。option パラメータとの組み合わせで指定できないデータ種別 ID があります。
        '''

        return self._instance.JVOpen(data_spec, from_time, option, 0, 0, "")

    def JVRTOpen(self, data_spec : str, key : str) -> int:
        '''
        データ識別文字列で指定したデータを読み込むための準備をします。具体的には以下の処理を行
        います。
        ・dataspecの検査を行います。
        ・dataspec および key に対応するデータをサーバにリクエストします。
        ・データの受信を完了した時点で処理をアプリケーションに返します。
        '''

        return self._instance.JVRTOpen(data_spec, key)

    def JVStatus(self) -> int:
        '''
        JVOpen をコールした際に起動されたダウンロードスレッドがダウンロードを完了したファイル数を返
        します。 ファイルのダウンロードが完了すると JVStatus の返す値は JVOpen をコールした際 の
        downloadcount と一致し ます。この一致を も っ てダ ウ ン ロー ドの終了を判断してください。以
        降 JVClose がコールされるまでの 間、JVStatus はこの値を返します。ダウンロード処理の完了を
        待たず JVRead/JVGets を呼び出すと 予期しないエラーが発生する場合があります。
        JVOpen が呼び出されていない、または dataspec に合致するデータが存在せずダウンロードが行
        われていない時に呼び出された場合や、エラーが発生した場合は負のエラーコードが返りま す。
        JVStatus の戻り値をプログレスバー表示に利用する場合は、ダウンロードすべきファイルが存在し
        ないときに、0による除算が発生する場合があることに注意してください。
        '''

        return self._instance.JVStatus()

    def JVRead(self) -> list:

        '''
        JVOpen / JVRTOpen で準備した JV-Data を現在のファイルポインタから１行分読み出します。
        JVOpen / JVRTOpen を行なわずに JVRead メソッドを呼び出すとエラーが返ります。
        JVOpen ではデータ種別IDが複数指定できるため、JVRead メソッドは物理的には複数のファイルで
        あっても１つのファイルであるかのように連続してデータを読み出します。 ただし、ファイル間をまた
        ぐごとに戻り値としてファイル切り替わり（-1）が返り、全てのファイルを読 み終わった際に戻り値と
        して EOF（0）が返ります。
        例えば「2002 年 11 月 10 日以降現在までの RACE データ」を指定して読み出した場合に、レース詳
        細データが 36 件存在したとすると１回目から 36 回目の呼出しまではレース詳細のレコードが 1 行ず
        つバッファにセットされ、37 回目の呼び出しでファイル切り替わり（-1）が返されます。38 回目以降
        の呼出しには馬毎レース情報がセットされます。全てのレコードが無くなった時点で EOF（0）が返さ
        れます。
        '''

        return self._instance.JVRead("", sys.maxsize, "")

    def JVGets(self) -> list:

        '''
        JVOpen / JVRTOpen で準備した JV-Data を現在のファイルポインタから１行分読み出します。
        JVOpen / JVRTOpen を行なわずに JVGets メソッドを呼び出すとエラーが返ります。
        JVOpen ではデータ種別IDが複数指定できるため、JVGets メソッドは物理的には複数のファイルで
        あっても１つのファイルであるかのように連続してデータを読み出します。 ただし、ファイル間をまた
        ぐごとに戻り値としてファイル切り替わり（-1）が返り、全てのファイルを読 み終わった際に戻り値と
        して EOF（0）が返ります。
        例えば「2002 年 11 月 10 日以降現在までの RACE データ」を指定して読み出した場合に、レース詳
        細データが 36 件存在したとすると１回目から 36 回目の呼出しまではレース詳細のレコードが 1 行ず
        つバッファにセットされ、37 回目の呼び出しでファイル切り替わり（-1）が返されます。38 回目以降
        の呼出しには馬毎レース情報がセットされます。全てのレコードが無くなった時点で EOF（0）が返さ
        れます。
        '''

        # bytearrayで受ける
        result, file_data, file_name = self._instance.JVGets(bytearray(0), sys.maxsize, "")

        # bytesで返却する
        return result, bytes(file_data), file_name

    def JVSkip(self) -> None:

        '''
        JVOpen で準備した JV-Data を読み込み中に不要なレコード種別を読み飛ばすために使用します。
        JVSkip メソッドを呼び出すと現在読み込み中のファイルにレコードが残っていても次のファイルの先
        頭までファイルポインタを進めます。
        JVRead/JVGets メソッドは物理的には複数のファイルであっても１つのファイルであるかのように連
        続してデータを読み出します。蓄積系データは１つのファイルにレコード種別は１種類しか収容され
        ていません。したがって JVRead/JVGets メソッドで読み出されたレコードが処理不要のレコード種別
        であった場合に JVSkip メソッドを呼び出し、そのファイルに収容されている残りの処理不要レコード
        を読み飛ばし処理時間を短縮することができます。速報系データは１回の JVRTOpen に対して１ファ
        イルしか返されないので JVSkip には意味がありません。
        例えばデータ種別”DIFF”を dataspec に指定して JVRead/JVGets を行なうと
        ・レース詳細(“RA”) ・馬毎レース情報(“SE”)
        ・競走馬(“UM”) ・騎手(“KS”)
        ・調教師(“CH”) ・生産者(“BR”)
        ・馬主(“BN”) ・レコード(“RC”)
        の8種類のデータを読み出す可能性がありますが、このうち”BR”と”BN”が不要なデータである場合
        には次のロジックにより処理時間が短縮されます。

        '''

        self._instance.JVSkip()

    def JVCancel(self) -> None:

        '''
        JVOpen により起動されたファイル準備処理（ダウンロード）を中止します。
        JVOpen を呼び出すとローカルディスクに無いデータは JRA-VAN サーバーからダウンロードを開始
        します。ダウンロード中はその進捗状況を JVStatus で取得することが可能ですが、このときアプリ
        ケーション側から JVCancel を呼び出すことで、これらのファイル準備処理を中断することができます。
        JVCancel によって中断した状態で JVRead/JVGets を呼び出すとエラーとなります。
        JVCancel の代わりに JVClose を呼び出した場合もファイル準備処理を中断します。
        '''

        self._instance.JVCancel()

    def JVClose(self) -> int:
        '''
        開いているファイルを全てクローズし、実行中のダウンロードスレッドがあれば中止します。保存パス
        が示すフォルダから不要なファイルを削除します。
        '''

        return self._instance.JVClose()

    def JVFiledelete(self, file_name : str) -> int:

        '''
        保存パスが示すフォルダから指定されたファイルを削除します。
        保存パスに保存されているファイルの問題により JVRead/JVGets 中にエラーが発生した場合、
        JVFiledelete メソッドでファイルを削除してください。削除が成功した後、直前に行なった JVOpen か
        らの処理をやり直してください。
        '''

        return self._instance.JVFiledelete(file_name)

    def JVFukuFile(self, pattern : str, file_path : str) -> int:

        '''
        服色標示パラメータより、勝負服画像の画像データを返します。
        作成される画像データは、サイズ 50pix * 50pixのビットマップ形式（24 ビット）となります。形式・サイ
        ズについては、必要に応じて競馬ソフト側で変換してご使用ください。
        '''

        return self._instance.JVFukuFile(pattern, file_path)

    def JVFuku(self, pattern : str) -> list:

        '''
        服色標示パラメータより、勝負服画像の画像データを返します。
        作成される画像データは、サイズ 50pix * 50pixのビットマップ形式（24 ビット）となります。形式・サイ
        ズについては、必要に応じて競馬ソフト側で変換してご使用ください。
        '''

        return self._instance.JVFuku(pattern)
    
    def JVMVCheck(self, key : str) -> int:

        '''
        key で指定したレース映像の再生を行います。具体的には以下の処理を行います。
        ・JRA レーシングビュアー連携機能が利用可能なソフトウェアであるかの認証を行います。
        ・指定した映像が公開されている場合、映像の再生を行います。
        映像の再生は HTML5 Player (MP4 形式の場合)を利用して行います。
        再生するブラウザは JV-Link 設定画面の動画再生ブラウザにて設定した
        「Microsoft Edge」「Google Chrome」「IE」のいずれかになります。
        レース映像については、JVMVCheck メソッドもしくは JVMVCheckWithType メソッドを利用する事で、
        レース映像の公開状況を判別する事が可能となります。JVMVCheck もしくは JVMVCheckWithType
        と組み合わせてご利用下さい。
        パドック映像、マルチカメラ映像、パトロール映像については、JVMVCheckWithType メソッドを利用す
        る事で、パドック動画、マルチカメラ動画、パトロール動画の公開状況 を判別する事が可能となります。
        JVMVCheckWithType と組み合わせてご利用下さい。
        ※１度公開されたパドック動画のレースが中止になった場合、該当のレースについて本メソッドを使 用
        すると該当データ無し：-1が返ります。

        調教映像については、JVMVOpen で対象映像を指定し、JVMVRead で公開中の調教映像の key
        が取得可能です。取得した key を JVMVPlayWithType に設定して下さい。また、movietype について
        は”11”、”12”、”13”どれを指定しても再生される映像は同じです。
        ※JVOpen/JVRTOpen/JVMVOpen 中は本メソッドを使用できません。オープン中の場合、先に
        JVClose を呼び出してから使用してください。
        '''

        return self._instance.JVMVCheck(key)

    def JVMVCheckWithType(self, movie_type : str, key : str) -> int:

        '''
        key で指定したレース映像の再生を行います。具体的には以下の処理を行います。
        ・JRA レーシングビュアー連携機能が利用可能なソフトウェアであるかの認証を行います。
        ・指定した映像が公開されている場合、映像の再生を行います。
        映像の再生は HTML5 Player (MP4 形式の場合)を利用して行います。
        再生するブラウザは JV-Link 設定画面の動画再生ブラウザにて設定した
        「Microsoft Edge」「Google Chrome」「IE」のいずれかになります。
        レース映像については、JVMVCheck メソッドもしくは JVMVCheckWithType メソッドを利用する事で、
        レース映像の公開状況を判別する事が可能となります。JVMVCheck もしくは JVMVCheckWithType
        と組み合わせてご利用下さい。
        パドック映像、マルチカメラ映像、パトロール映像については、JVMVCheckWithType メソッドを利用す
        る事で、パドック動画、マルチカメラ動画、パトロール動画の公開状況 を判別する事が可能となります。
        JVMVCheckWithType と組み合わせてご利用下さい。
        ※１度公開されたパドック動画のレースが中止になった場合、該当のレースについて本メソッドを使 用
        すると該当データ無し：-1が返ります。

        調教映像については、JVMVOpen で対象映像を指定し、JVMVRead で公開中の調教映像の key
        が取得可能です。取得した key を JVMVPlayWithType に設定して下さい。また、movietype について
        は”11”、”12”、”13”どれを指定しても再生される映像は同じです。
        ※JVOpen/JVRTOpen/JVMVOpen 中は本メソッドを使用できません。オープン中の場合、先に
        JVClose を呼び出してから使用してください。
        '''

        return self._instance.JVMVCheckWithType(movie_type, key)

    def JVMVPlay(self, key : str) -> int:

        '''
        key で指定したレース映像の再生を行います。具体的には以下の処理を行います。
        ・JRA レーシングビュアー連携機能が利用可能なソフトウェアであるかの認証を行います。
        ・指定した映像が公開されている場合、映像の再生を行います。
        映像の再生は HTML5 Player (MP4 形式の場合)を利用して行います。
        再生するブラウザは JV-Link 設定画面の動画再生ブラウザにて設定した
        「Microsoft Edge」「Google Chrome」「IE」のいずれかになります。
        レース映像については、JVMVCheck メソッドもしくは JVMVCheckWithType メソッドを利用する事で、
        レース映像の公開状況を判別する事が可能となります。JVMVCheck もしくは JVMVCheckWithType
        と組み合わせてご利用下さい。
        パドック映像、マルチカメラ映像、パトロール映像については、JVMVCheckWithType メソッドを利用す
        る事で、パドック動画、マルチカメラ動画、パトロール動画の公開状況 を判別する事が可能となります。
        JVMVCheckWithType と組み合わせてご利用下さい。
        ※１度公開されたパドック動画のレースが中止になった場合、該当のレースについて本メソッドを使 用
        すると該当データ無し：-1が返ります。

        調教映像については、JVMVOpen で対象映像を指定し、JVMVRead で公開中の調教映像の key
        が取得可能です。取得した key を JVMVPlayWithType に設定して下さい。また、movietype について
        は”11”、”12”、”13”どれを指定しても再生される映像は同じです。
        ※JVOpen/JVRTOpen/JVMVOpen 中は本メソッドを使用できません。オープン中の場合、先に
        JVClose を呼び出してから使用してください。
        '''

        return self._instance.JVMVPlay(key)

    def JVMVPlayWithType(self, movie_type : str, key : str) -> int:

        '''
        key で指定したレース映像の再生を行います。具体的には以下の処理を行います。
        ・JRA レーシングビュアー連携機能が利用可能なソフトウェアであるかの認証を行います。
        ・指定した映像が公開されている場合、映像の再生を行います。
        映像の再生は HTML5 Player (MP4 形式の場合)を利用して行います。
        再生するブラウザは JV-Link 設定画面の動画再生ブラウザにて設定した
        「Microsoft Edge」「Google Chrome」「IE」のいずれかになります。
        レース映像については、JVMVCheck メソッドもしくは JVMVCheckWithType メソッドを利用する事で、
        レース映像の公開状況を判別する事が可能となります。JVMVCheck もしくは JVMVCheckWithType
        と組み合わせてご利用下さい。
        パドック映像、マルチカメラ映像、パトロール映像については、JVMVCheckWithType メソッドを利用す
        る事で、パドック動画、マルチカメラ動画、パトロール動画の公開状況 を判別する事が可能となります。
        JVMVCheckWithType と組み合わせてご利用下さい。
        ※１度公開されたパドック動画のレースが中止になった場合、該当のレースについて本メソッドを使 用
        すると該当データ無し：-1が返ります。

        調教映像については、JVMVOpen で対象映像を指定し、JVMVRead で公開中の調教映像の key
        が取得可能です。取得した key を JVMVPlayWithType に設定して下さい。また、movietype について
        は”11”、”12”、”13”どれを指定しても再生される映像は同じです。
        ※JVOpen/JVRTOpen/JVMVOpen 中は本メソッドを使用できません。オープン中の場合、先に
        JVClose を呼び出してから使用してください。
        '''

        return self._instance.JVMVPlayWithType(movie_type, key)

    def JVMVOpen(self, movie_type : str, search_key : str) -> int:

        '''
        データ識別文字列で指定したデータを読み込むための準備をします。具体的には以下の処理を行
        います。
        ・movietype、searchkey の検査を行います。
        ・movietype および searchkeyに対応するデータをサーバにリクエストします。
        ・データの受信を完了した時点で処理をアプリケーションに返します。

        '''

        return self._instance.JVMVOpen(movie_type, search_key)

    def JVMVRead(self, buffer : str, size : int) -> int:

        '''
        JVMVOpen で準備した動画リストをカレント行から１行分読み出します。
        JVMVOpen を行なわずに JVMVReadメソッドを呼び出すとエラーが返ります。
        JVOpen / JVRTOpen 中は使用できません。（エラーが返ります。）
        '''

        return self._instance.JVMVRead(buffer, size)

    def JVCourseFile(self, key : str, file_path : str, explanation : str) -> int:

        '''
        ｋey で指定した該当レースのコース図が取得できます。 コンテンツサーバから取得したコース図
        は m_savepath 以下の pictures フォルダに一時的に保存 れます。
        取得したコース図は、サイズ 256pix × 200pix の GIF 形式となります。形式・サイズについては、
        必要に応じて競馬ソフト側で変換してご使用ください。
        '''

        return self._instance.JVCourseFile(key, file_path, explanation)

    def JVCourseFile2(self, key : str, file_path : str) -> int:

        '''
        ｋey で指定した該当レースのコース図を取得します。取得したファイルは filepathで指定したパスに 保
        存されます。
        取得したコース図は、サイズ 256pix × 200pix の GIF 形式となります。形式・サイズについては、 必
        要に応じて競馬ソフト側で変換してご使用ください。 蓄積系データとして取得したコース情報からコース
        図を取得する際は、コース改修年月日を開催年、 開催月、開催日として要求キーに指定してください。
        データ区分「2：更新」のデータは、コース解説やコース図画像ファイルが変更された際に提供するデ
        ータです。従いまして、データ区分が「1：新規登録」、または「2：更新」のレコードが存在する場合は、
        このメソッドを使用してコース図を取得してください。
        データ仕様の詳細につきましては、JV-Data 仕様書をご参照ください。
        '''

        return self._instance.JVCourseFile2(key, file_path)

    def JVWatchEvent(self) -> int:

        '''
        確定・変更情報が発生した際、イベントを通知するスレッドを開始します。
        JVInit を行わずに JVWatchEvent メソッドを呼び出すとエラーが返ります。
        '''

        return self._instance.JVWatchEvent()

    def JVWatchEventClose(self) -> int:

        '''
        イベント通知スレッドを終了します。 イベント受信処理を終了したい場合ご使用ください。
        '''

        return self._instance.JVWatchEventClose()
