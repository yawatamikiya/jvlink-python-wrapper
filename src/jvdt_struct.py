class YMD:

	'''
	年
	'''
	__year = bytes()

	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, value):
		self.__year = value

	'''
	月
	'''
	__month = bytes()

	@property
	def month(self):
		return self.__month

	@month.setter
	def month(self, value):
		self.__month = value

	'''
	日
	'''
	__day = bytes()

	@property
	def day(self):
		return self.__day

	@day.setter
	def day(self, value):
		self.__day = value

	def __init__(self, source : bytes) -> None:

		self.__year = source[0:4]
		self.__month = source[4:6]
		self.__day = source[6:8]

class HMS:

	'''
	時
	'''
	__hour = bytes()

	@property
	def hour(self):
		return self.__hour

	@hour.setter
	def hour(self, value):
		self.__hour = value

	'''
	分
	'''
	__minute = bytes()

	@property
	def minute(self):
		return self.__minute

	@minute.setter
	def minute(self, value):
		self.__minute = value

	'''
	秒
	'''
	__second = bytes()

	@property
	def second(self):
		return self.__second

	@second.setter
	def second(self, value):
		self.__second = value

	def __init__(self, source : bytes) -> None:

		self.__hour = source[0:2]
		self.__minute = source[2:4]
		self.__second = source[4:6]

class HM:

	'''
	時
	'''
	__hour = bytes()

	@property
	def hour(self):
		return self.__hour

	@hour.setter
	def hour(self, value):
		self.__hour = value

	'''
	分
	'''
	__minute = bytes()

	@property
	def minute(self):
		return self.__minute

	@minute.setter
	def minute(self, value):
		self.__minute = value

	def __init__(self, source : bytes) -> None:

		self.__hour = source[0:2]
		self.__minute = source[2:4]

class MDHM:

	'''
	月
	'''
	__month = bytes()

	@property
	def month(self):
		return self.__month

	@month.setter
	def month(self, value):
		self.__month = value

	'''
	日
	'''
	__day = bytes()

	@property
	def day(self):
		return self.__day

	@day.setter
	def day(self, value):
		self.__day = value

	'''
	時
	'''
	__hour = bytes()

	@property
	def hour(self):
		return self.__hour

	@hour.setter
	def hour(self, value):
		self.__hour = value

	'''
	分
	'''
	__minute = bytes()

	@property
	def minute(self):
		return self.__minute

	@minute.setter
	def minute(self, value):
		self.__minute = value

	def __init__(self, source : bytes) -> None:

		self.__month = source[0:2]
		self.__day = source[2:4]
		self.__hour = source[4:6]
		self.__minute = source[6:8]

class RECORD_ID:

	'''
	レコード種別
	'''
	__record_spec = bytes()

	@property
	def record_spec(self):
		return self.__record_spec

	@record_spec.setter
	def record_spec(self, value):
		self.__record_spec = value

	'''
	データ区分
	'''
	__data_kubun = bytes()

	@property
	def data_kubun(self):
		return self.__data_kubun

	@data_kubun.setter
	def data_kubun(self, value):
		self.__data_kubun = value

	'''
	データ作成年月日
	'''
	__make_date = None

	@property
	def make_date(self):
		return self.__make_date

	@make_date.setter
	def make_date(self, value):
		self.__make_date = value

	def __init__(self, source : bytes) -> None:

		self.__record_spec = source[0:2]
		self.__data_kubun = source[2:3]
		self.__make_date = YMD(source[3:11])

class RACE_ID:

	'''
	開催年
	'''
	__year = bytes()

	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, value):
		self.__year = value

	'''
	開催月日
	'''
	__month_day = bytes()

	@property
	def month_day(self):
		return self.__month_day

	@month_day.setter
	def month_day(self, value):
		self.__month_day = value

	'''
	競馬場コード
	'''
	__jyo_cd = bytes()

	@property
	def jyo_cd(self):
		return self.__jyo_cd

	@jyo_cd.setter
	def jyo_cd(self, value):
		self.__jyo_cd = value

	'''
	開催回[第N回]
	'''
	__kaiji = bytes()

	@property
	def kaiji(self):
		return self.__kaiji

	@kaiji.setter
	def kaiji(self, value):
		self.__kaiji = value

	'''
	開催日目[N日目]
	'''
	__nichiji = bytes()

	@property
	def nichiji(self):
		return self.__nichiji

	@nichiji.setter
	def nichiji(self, value):
		self.__nichiji = value

	'''
	レース番号
	'''
	__race_num = bytes()

	@property
	def race_num(self):
		return self.__race_num

	@race_num.setter
	def race_num(self, value):
		self.__race_num = value

	def __init__(self, source : bytes) -> None:

		self.__year = source[0:4]
		self.__month_day = source[4:8]
		self.__jyo_cd = source[8:10]
		self.__kaiji = source[10:12]
		self.__nichiji = source[12:14]
		self.__race_num = source[14:16]

class RACE_ID2:

	'''
	開催年
	'''
	__year = bytes()

	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, value):
		self.__year = value

	'''
	開催月日
	'''
	__month_day = bytes()

	@property
	def month_day(self):
		return self.__month_day

	@month_day.setter
	def month_day(self, value):
		self.__month_day = value

	'''
	競馬場コード
	'''
	__jyo_cd = bytes()

	@property
	def jyo_cd(self):
		return self.__jyo_cd

	@jyo_cd.setter
	def jyo_cd(self, value):
		self.__jyo_cd = value

	'''
	開催回[第N回]
	'''
	__kaiji = bytes()

	@property
	def kaiji(self):
		return self.__kaiji

	@kaiji.setter
	def kaiji(self, value):
		self.__kaiji = value

	'''
	開催日目[N日目]
	'''
	__nichiji = bytes()

	@property
	def nichiji(self):
		return self.__nichiji

	@nichiji.setter
	def nichiji(self, value):
		self.__nichiji = value

	def __init__(self, source : bytes) -> None:

		self.__year = source[0:4]
		self.__month_day = source[4:8]
		self.__jyo_cd = source[8:10]
		self.__kaiji = source[10:12]
		self.__nichiji = source[12:14]

class SEI_RUIKEI_INFO:

	'''
	設定年
	'''
	__set_year = bytes()

	@property
	def set_year(self):
		return self.__set_year

	@set_year.setter
	def set_year(self, value):
		self.__set_year = value

	'''
	本賞金合計
	'''
	__hon_syokin_total = bytes()

	@property
	def hon_syokin_total(self):
		return self.__hon_syokin_total

	@hon_syokin_total.setter
	def hon_syokin_total(self, value):
		self.__hon_syokin_total = value

	'''
	付加賞金合計
	'''
	__fuka_syokin = bytes()

	@property
	def fuka_syokin(self):
		return self.__fuka_syokin

	@fuka_syokin.setter
	def fuka_syokin(self, value):
		self.__fuka_syokin = value

	'''
	着回数
	'''
	__chaku_kaisu = []

	@property
	def chaku_kaisu(self):
		return self.__chaku_kaisu

	@chaku_kaisu.setter
	def chaku_kaisu(self, value):
		self.__chaku_kaisu = value

	def __init__(self, source : bytes) -> None:

		self.__set_year = source[0:4]
		self.__hon_syokin_total = source[4:14]
		self.__fuka_syokin = source[14:24]
		self.__chaku_kaisu = []
		for i in range(6):
			self.__chaku_kaisu.append(source[24 + i * 6:24 + i * 6 + 6])

class SAIKIN_JYUSYO_INFO:

	'''
	年月日場回日R
	'''
	__saikin_jyusyoid = None

	@property
	def saikin_jyusyoid(self):
		return self.__saikin_jyusyoid

	@saikin_jyusyoid.setter
	def saikin_jyusyoid(self, value):
		self.__saikin_jyusyoid = value

	'''
	競走名本題
	'''
	__hondai = bytes()

	@property
	def hondai(self):
		return self.__hondai

	@hondai.setter
	def hondai(self, value):
		self.__hondai = value

	'''
	競走名略称10字
	'''
	__ryakusyo10 = bytes()

	@property
	def ryakusyo10(self):
		return self.__ryakusyo10

	@ryakusyo10.setter
	def ryakusyo10(self, value):
		self.__ryakusyo10 = value

	'''
	競走名略称6字
	'''
	__ryakusyo6 = bytes()

	@property
	def ryakusyo6(self):
		return self.__ryakusyo6

	@ryakusyo6.setter
	def ryakusyo6(self, value):
		self.__ryakusyo6 = value

	'''
	競走名略称3字
	'''
	__ryakusyo3 = bytes()

	@property
	def ryakusyo3(self):
		return self.__ryakusyo3

	@ryakusyo3.setter
	def ryakusyo3(self, value):
		self.__ryakusyo3 = value

	'''
	グレードコード
	'''
	__grade_cd = bytes()

	@property
	def grade_cd(self):
		return self.__grade_cd

	@grade_cd.setter
	def grade_cd(self, value):
		self.__grade_cd = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	def __init__(self, source : bytes) -> None:

		self.__saikin_jyusyoid = RACE_ID(source[0:16])
		self.__hondai = source[16:76]
		self.__ryakusyo10 = source[76:96]
		self.__ryakusyo6 = source[96:108]
		self.__ryakusyo3 = source[108:114]
		self.__grade_cd = source[114:115]
		self.__syusso_tosu = source[115:117]
		self.__ketto_num = source[117:127]
		self.__bamei = source[127:163]

class HON_ZEN_RUIKEISEI_INFO:

	'''
	設定年
	'''
	__set_year = bytes()

	@property
	def set_year(self):
		return self.__set_year

	@set_year.setter
	def set_year(self, value):
		self.__set_year = value

	'''
	平地本賞金合計
	'''
	__hon_syokin_heichi = bytes()

	@property
	def hon_syokin_heichi(self):
		return self.__hon_syokin_heichi

	@hon_syokin_heichi.setter
	def hon_syokin_heichi(self, value):
		self.__hon_syokin_heichi = value

	'''
	障害本賞金合計
	'''
	__hon_syokin_syogai = bytes()

	@property
	def hon_syokin_syogai(self):
		return self.__hon_syokin_syogai

	@hon_syokin_syogai.setter
	def hon_syokin_syogai(self, value):
		self.__hon_syokin_syogai = value

	'''
	平地付加賞金合計
	'''
	__fuka_syokin_heichi = bytes()

	@property
	def fuka_syokin_heichi(self):
		return self.__fuka_syokin_heichi

	@fuka_syokin_heichi.setter
	def fuka_syokin_heichi(self, value):
		self.__fuka_syokin_heichi = value

	'''
	障害付加賞金合計
	'''
	__fuka_syokin_syogai = bytes()

	@property
	def fuka_syokin_syogai(self):
		return self.__fuka_syokin_syogai

	@fuka_syokin_syogai.setter
	def fuka_syokin_syogai(self, value):
		self.__fuka_syokin_syogai = value

	'''
	平地着回数
	'''
	__chaku_kaisu_heichi = None

	@property
	def chaku_kaisu_heichi(self):
		return self.__chaku_kaisu_heichi

	@chaku_kaisu_heichi.setter
	def chaku_kaisu_heichi(self, value):
		self.__chaku_kaisu_heichi = value

	'''
	障害着回数
	'''
	__chaku_kaisu_syogai = None

	@property
	def chaku_kaisu_syogai(self):
		return self.__chaku_kaisu_syogai

	@chaku_kaisu_syogai.setter
	def chaku_kaisu_syogai(self, value):
		self.__chaku_kaisu_syogai = value

	'''
	競馬場別着回数
	'''
	__chaku_kaisu_jyo = []

	@property
	def chaku_kaisu_jyo(self):
		return self.__chaku_kaisu_jyo

	@chaku_kaisu_jyo.setter
	def chaku_kaisu_jyo(self, value):
		self.__chaku_kaisu_jyo = value

	'''
	距離別着回数
	'''
	__chaku_kaisu_kyori = []

	@property
	def chaku_kaisu_kyori(self):
		return self.__chaku_kaisu_kyori

	@chaku_kaisu_kyori.setter
	def chaku_kaisu_kyori(self, value):
		self.__chaku_kaisu_kyori = value

	def __init__(self, source : bytes) -> None:

		self.__set_year = source[0:4]
		self.__hon_syokin_heichi = source[4:14]
		self.__hon_syokin_syogai = source[14:24]
		self.__fuka_syokin_heichi = source[24:34]
		self.__fuka_syokin_syogai = source[34:44]
		self.__chaku_kaisu_heichi = CHAKUKAISU6_INFO(source[44:80])
		self.__chaku_kaisu_syogai = CHAKUKAISU6_INFO(source[80:116])

		self.__chaku_kaisu_jyo = []
		for i in range(20):
			self.__chaku_kaisu_jyo.append(CHAKUKAISU6_INFO(source[116 + i * 36 :116 + i * 36 + 36]))

		self.__chaku_kaisu_kyori = []
		for i in range(6):
			self.__chaku_kaisu_kyori.append(CHAKUKAISU6_INFO(source[836 + i * 36 :836 + i * 36 + 36]))

class RACE_INFO:

	'''
	曜日コード
	'''
	__youbi_cd = bytes()

	@property
	def youbi_cd(self):
		return self.__youbi_cd

	@youbi_cd.setter
	def youbi_cd(self, value):
		self.__youbi_cd = value

	'''
	特別競走番号
	'''
	__toku_num = bytes()

	@property
	def toku_num(self):
		return self.__toku_num

	@toku_num.setter
	def toku_num(self, value):
		self.__toku_num = value

	'''
	競走名本題
	'''
	__hondai = bytes()

	@property
	def hondai(self):
		return self.__hondai

	@hondai.setter
	def hondai(self, value):
		self.__hondai = value

	'''
	競走名副題
	'''
	__fukudai = bytes()

	@property
	def fukudai(self):
		return self.__fukudai

	@fukudai.setter
	def fukudai(self, value):
		self.__fukudai = value

	'''
	競走名カッコ内
	'''
	__kakko = bytes()

	@property
	def kakko(self):
		return self.__kakko

	@kakko.setter
	def kakko(self, value):
		self.__kakko = value

	'''
	競走名本題欧字
	'''
	__hondai_eng = bytes()

	@property
	def hondai_eng(self):
		return self.__hondai_eng

	@hondai_eng.setter
	def hondai_eng(self, value):
		self.__hondai_eng = value

	'''
	競走名副題欧字
	'''
	__fukudai_eng = bytes()

	@property
	def fukudai_eng(self):
		return self.__fukudai_eng

	@fukudai_eng.setter
	def fukudai_eng(self, value):
		self.__fukudai_eng = value

	'''
	競走名カッコ内欧字
	'''
	__kakko_eng = bytes()

	@property
	def kakko_eng(self):
		return self.__kakko_eng

	@kakko_eng.setter
	def kakko_eng(self, value):
		self.__kakko_eng = value

	'''
	競走名略称１０字
	'''
	__ryakusyo10 = bytes()

	@property
	def ryakusyo10(self):
		return self.__ryakusyo10

	@ryakusyo10.setter
	def ryakusyo10(self, value):
		self.__ryakusyo10 = value

	'''
	競走名略称６字
	'''
	__ryakusyo6 = bytes()

	@property
	def ryakusyo6(self):
		return self.__ryakusyo6

	@ryakusyo6.setter
	def ryakusyo6(self, value):
		self.__ryakusyo6 = value

	'''
	競走名略称３字
	'''
	__ryakusyo3 = bytes()

	@property
	def ryakusyo3(self):
		return self.__ryakusyo3

	@ryakusyo3.setter
	def ryakusyo3(self, value):
		self.__ryakusyo3 = value

	'''
	競走名区分
	'''
	__kubun = bytes()

	@property
	def kubun(self):
		return self.__kubun

	@kubun.setter
	def kubun(self, value):
		self.__kubun = value

	'''
	重賞回次[第N回]
	'''
	__nkai = bytes()

	@property
	def nkai(self):
		return self.__nkai

	@nkai.setter
	def nkai(self, value):
		self.__nkai = value

	def __init__(self, source : bytes) -> None:

		self.__youbi_cd = source[0:1]
		self.__toku_num = source[1:5]
		self.__hondai = source[5:65]
		self.__fukudai = source[65:125]
		self.__kakko = source[125:185]
		self.__hondai_eng = source[185:305]
		self.__fukudai_eng = source[305:425]
		self.__kakko_eng = source[425:545]
		self.__ryakusyo10 = source[545:565]
		self.__ryakusyo6 = source[565:577]
		self.__ryakusyo3 = source[577:583]
		self.__kubun = source[583:584]
		self.__nkai = source[584:587]

class TENKO_BABA_INFO:

	'''
	天候コード
	'''
	__tenko_cd = bytes()

	@property
	def tenko_cd(self):
		return self.__tenko_cd

	@tenko_cd.setter
	def tenko_cd(self, value):
		self.__tenko_cd = value

	'''
	芝馬場状態コード
	'''
	__siba_baba_cd = bytes()

	@property
	def siba_baba_cd(self):
		return self.__siba_baba_cd

	@siba_baba_cd.setter
	def siba_baba_cd(self, value):
		self.__siba_baba_cd = value

	'''
	ダート馬場状態コード
	'''
	__dirt_baba_cd = bytes()

	@property
	def dirt_baba_cd(self):
		return self.__dirt_baba_cd

	@dirt_baba_cd.setter
	def dirt_baba_cd(self, value):
		self.__dirt_baba_cd = value

	def __init__(self, source : bytes) -> None:

		self.__tenko_cd = source[0:1]
		self.__siba_baba_cd = source[1:2]
		self.__dirt_baba_cd = source[2:3]

class CHAKUKAISU3_INFO:

	'''
	
	'''
	__chaku_kaisu = []

	@property
	def chaku_kaisu(self):
		return self.__chaku_kaisu

	@chaku_kaisu.setter
	def chaku_kaisu(self, value):
		self.__chaku_kaisu = value

	def __init__(self, source : bytes) -> None:

		self.__chaku_kaisu = []
		for i in range(6):
			self.__chaku_kaisu.append(source[0 + i * 3:0 + i * 3 + 3])

class CHAKUKAISU4_INFO:

	'''
	
	'''
	__chaku_kaisu = []

	@property
	def chaku_kaisu(self):
		return self.__chaku_kaisu

	@chaku_kaisu.setter
	def chaku_kaisu(self, value):
		self.__chaku_kaisu = value

	def __init__(self, source : bytes) -> None:

		self.__chaku_kaisu = []
		for i in range(6):
			self.__chaku_kaisu.append(source[0 + i * 4:0 + i * 4 + 4])

class CHAKUKAISU5_INFO:

	'''
	
	'''
	__chaku_kaisu = []

	@property
	def chaku_kaisu(self):
		return self.__chaku_kaisu

	@chaku_kaisu.setter
	def chaku_kaisu(self, value):
		self.__chaku_kaisu = value

	def __init__(self, source : bytes) -> None:

		self.__chaku_kaisu = []
		for i in range(6):
			self.__chaku_kaisu.append(source[0 + i * 5:0 + i * 5 + 5])

class CHAKUKAISU6_INFO:

	'''
	
	'''
	__chaku_kaisu = []

	@property
	def chaku_kaisu(self):
		return self.__chaku_kaisu

	@chaku_kaisu.setter
	def chaku_kaisu(self, value):
		self.__chaku_kaisu = value

	def __init__(self, source : bytes) -> None:

		self.__chaku_kaisu = []
		for i in range(6):
			self.__chaku_kaisu.append(source[0 + i * 6:0 + i * 6 + 6])

class RACE_JYOKEN:

	'''
	競走種別コード
	'''
	__syubetu_cd = bytes()

	@property
	def syubetu_cd(self):
		return self.__syubetu_cd

	@syubetu_cd.setter
	def syubetu_cd(self, value):
		self.__syubetu_cd = value

	'''
	競走記号コード
	'''
	__kigo_cd = bytes()

	@property
	def kigo_cd(self):
		return self.__kigo_cd

	@kigo_cd.setter
	def kigo_cd(self, value):
		self.__kigo_cd = value

	'''
	重量種別コード
	'''
	__jyuryo_cd = bytes()

	@property
	def jyuryo_cd(self):
		return self.__jyuryo_cd

	@jyuryo_cd.setter
	def jyuryo_cd(self, value):
		self.__jyuryo_cd = value

	'''
	競走条件コード
	'''
	__jyoken_cd = []

	@property
	def jyoken_cd(self):
		return self.__jyoken_cd

	@jyoken_cd.setter
	def jyoken_cd(self, value):
		self.__jyoken_cd = value

	def __init__(self, source : bytes) -> None:

		self.__syubetu_cd = source[0:2]
		self.__kigo_cd = source[2:5]
		self.__jyuryo_cd = source[5:6]
		self.__jyoken_cd = []
		for i in range(5):
			self.__jyoken_cd.append(source[6 + i * 3:6 + i * 3 + 3])

class TOKUUMA_INFO:

	'''
	連番
	'''
	__num = bytes()

	@property
	def num(self):
		return self.__num

	@num.setter
	def num(self, value):
		self.__num = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	馬記号コード
	'''
	__uma_kigo_cd = bytes()

	@property
	def uma_kigo_cd(self):
		return self.__uma_kigo_cd

	@uma_kigo_cd.setter
	def uma_kigo_cd(self, value):
		self.__uma_kigo_cd = value

	'''
	性別コード
	'''
	__sex_cd = bytes()

	@property
	def sex_cd(self):
		return self.__sex_cd

	@sex_cd.setter
	def sex_cd(self, value):
		self.__sex_cd = value

	'''
	調教師東西所属コード
	'''
	__tozai_cd = bytes()

	@property
	def tozai_cd(self):
		return self.__tozai_cd

	@tozai_cd.setter
	def tozai_cd(self, value):
		self.__tozai_cd = value

	'''
	調教師コード
	'''
	__chokyosi_cd = bytes()

	@property
	def chokyosi_cd(self):
		return self.__chokyosi_cd

	@chokyosi_cd.setter
	def chokyosi_cd(self, value):
		self.__chokyosi_cd = value

	'''
	調教師名略称
	'''
	__chokyosi_ryakusyo = bytes()

	@property
	def chokyosi_ryakusyo(self):
		return self.__chokyosi_ryakusyo

	@chokyosi_ryakusyo.setter
	def chokyosi_ryakusyo(self, value):
		self.__chokyosi_ryakusyo = value

	'''
	負担重量
	'''
	__futan = bytes()

	@property
	def futan(self):
		return self.__futan

	@futan.setter
	def futan(self, value):
		self.__futan = value

	'''
	交流区分
	'''
	__koryu = bytes()

	@property
	def koryu(self):
		return self.__koryu

	@koryu.setter
	def koryu(self, value):
		self.__koryu = value

	def __init__(self, source : bytes) -> None:

		self.__num = source[0:3]
		self.__ketto_num = source[3:13]
		self.__bamei = source[13:49]
		self.__uma_kigo_cd = source[49:51]
		self.__sex_cd = source[51:52]
		self.__tozai_cd = source[52:53]
		self.__chokyosi_cd = source[53:58]
		self.__chokyosi_ryakusyo = source[58:66]
		self.__futan = source[66:69]
		self.__koryu = source[69:70]

class JV_TK_TOKUUMA:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	レース情報
	'''
	__race_info = None

	@property
	def race_info(self):
		return self.__race_info

	@race_info.setter
	def race_info(self, value):
		self.__race_info = value

	'''
	グレードコード
	'''
	__grade_cd = bytes()

	@property
	def grade_cd(self):
		return self.__grade_cd

	@grade_cd.setter
	def grade_cd(self, value):
		self.__grade_cd = value

	'''
	競走条件コード
	'''
	__jyoken_info = None

	@property
	def jyoken_info(self):
		return self.__jyoken_info

	@jyoken_info.setter
	def jyoken_info(self, value):
		self.__jyoken_info = value

	'''
	距離
	'''
	__kyori = bytes()

	@property
	def kyori(self):
		return self.__kyori

	@kyori.setter
	def kyori(self, value):
		self.__kyori = value

	'''
	トラックコード
	'''
	__track_cd = bytes()

	@property
	def track_cd(self):
		return self.__track_cd

	@track_cd.setter
	def track_cd(self, value):
		self.__track_cd = value

	'''
	コース区分
	'''
	__course_kubun_cd = bytes()

	@property
	def course_kubun_cd(self):
		return self.__course_kubun_cd

	@course_kubun_cd.setter
	def course_kubun_cd(self, value):
		self.__course_kubun_cd = value

	'''
	ハンデ発表日
	'''
	__handi_date = None

	@property
	def handi_date(self):
		return self.__handi_date

	@handi_date.setter
	def handi_date(self, value):
		self.__handi_date = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	登録馬毎情報
	'''
	__toku_uma_info = []

	@property
	def toku_uma_info(self):
		return self.__toku_uma_info

	@toku_uma_info.setter
	def toku_uma_info(self, value):
		self.__toku_uma_info = value

	'''
	レコード区切
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__race_info = RACE_INFO(source[27:614])
		self.__grade_cd = source[614:615]
		self.__jyoken_info = RACE_JYOKEN(source[615:636])
		self.__kyori = source[636:640]
		self.__track_cd = source[640:642]
		self.__course_kubun_cd = source[642:644]
		self.__handi_date = YMD(source[644:652])
		self.__toroku_tosu = source[652:655]

		self.__toku_uma_info = []
		for i in range(300):
			self.__toku_uma_info.append(TOKUUMA_INFO(source[655 + i * 70 :655 + i * 70 + 70]))

		self.__crlf = source[21655:21657]

class CORNER_INFO:

	'''
	コーナー
	'''
	__corner = bytes()

	@property
	def corner(self):
		return self.__corner

	@corner.setter
	def corner(self, value):
		self.__corner = value

	'''
	周回数
	'''
	__syukaisu = bytes()

	@property
	def syukaisu(self):
		return self.__syukaisu

	@syukaisu.setter
	def syukaisu(self, value):
		self.__syukaisu = value

	'''
	各通過順位
	'''
	__jyuni = bytes()

	@property
	def jyuni(self):
		return self.__jyuni

	@jyuni.setter
	def jyuni(self, value):
		self.__jyuni = value

	def __init__(self, source : bytes) -> None:

		self.__corner = source[0:1]
		self.__syukaisu = source[1:2]
		self.__jyuni = source[2:72]

class JV_RA_RACE:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	レース情報
	'''
	__race_info = None

	@property
	def race_info(self):
		return self.__race_info

	@race_info.setter
	def race_info(self, value):
		self.__race_info = value

	'''
	グレードコード
	'''
	__grade_cd = bytes()

	@property
	def grade_cd(self):
		return self.__grade_cd

	@grade_cd.setter
	def grade_cd(self, value):
		self.__grade_cd = value

	'''
	変更前グレードコード
	'''
	__grade_cd_before = bytes()

	@property
	def grade_cd_before(self):
		return self.__grade_cd_before

	@grade_cd_before.setter
	def grade_cd_before(self, value):
		self.__grade_cd_before = value

	'''
	競走条件コード
	'''
	__jyoken_info = None

	@property
	def jyoken_info(self):
		return self.__jyoken_info

	@jyoken_info.setter
	def jyoken_info(self, value):
		self.__jyoken_info = value

	'''
	競走条件名称
	'''
	__jyoken_name = bytes()

	@property
	def jyoken_name(self):
		return self.__jyoken_name

	@jyoken_name.setter
	def jyoken_name(self, value):
		self.__jyoken_name = value

	'''
	距離
	'''
	__kyori = bytes()

	@property
	def kyori(self):
		return self.__kyori

	@kyori.setter
	def kyori(self, value):
		self.__kyori = value

	'''
	変更前距離
	'''
	__kyori_before = bytes()

	@property
	def kyori_before(self):
		return self.__kyori_before

	@kyori_before.setter
	def kyori_before(self, value):
		self.__kyori_before = value

	'''
	トラックコード
	'''
	__track_cd = bytes()

	@property
	def track_cd(self):
		return self.__track_cd

	@track_cd.setter
	def track_cd(self, value):
		self.__track_cd = value

	'''
	変更前トラックコード
	'''
	__track_cd_before = bytes()

	@property
	def track_cd_before(self):
		return self.__track_cd_before

	@track_cd_before.setter
	def track_cd_before(self, value):
		self.__track_cd_before = value

	'''
	コース区分
	'''
	__course_kubun_cd = bytes()

	@property
	def course_kubun_cd(self):
		return self.__course_kubun_cd

	@course_kubun_cd.setter
	def course_kubun_cd(self, value):
		self.__course_kubun_cd = value

	'''
	変更前コース区分
	'''
	__course_kubun_cd_before = bytes()

	@property
	def course_kubun_cd_before(self):
		return self.__course_kubun_cd_before

	@course_kubun_cd_before.setter
	def course_kubun_cd_before(self, value):
		self.__course_kubun_cd_before = value

	'''
	本賞金
	'''
	__honsyokin = []

	@property
	def honsyokin(self):
		return self.__honsyokin

	@honsyokin.setter
	def honsyokin(self, value):
		self.__honsyokin = value

	'''
	変更前本賞金
	'''
	__honsyokin_before = []

	@property
	def honsyokin_before(self):
		return self.__honsyokin_before

	@honsyokin_before.setter
	def honsyokin_before(self, value):
		self.__honsyokin_before = value

	'''
	付加賞金
	'''
	__fukasyokin = []

	@property
	def fukasyokin(self):
		return self.__fukasyokin

	@fukasyokin.setter
	def fukasyokin(self, value):
		self.__fukasyokin = value

	'''
	変更前付加賞金
	'''
	__fukasyokin_before = []

	@property
	def fukasyokin_before(self):
		return self.__fukasyokin_before

	@fukasyokin_before.setter
	def fukasyokin_before(self, value):
		self.__fukasyokin_before = value

	'''
	発走時刻
	'''
	__hasso_time = bytes()

	@property
	def hasso_time(self):
		return self.__hasso_time

	@hasso_time.setter
	def hasso_time(self, value):
		self.__hasso_time = value

	'''
	変更前発走時刻
	'''
	__hasso_time_before = bytes()

	@property
	def hasso_time_before(self):
		return self.__hasso_time_before

	@hasso_time_before.setter
	def hasso_time_before(self, value):
		self.__hasso_time_before = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	入線頭数
	'''
	__nyusen_tosu = bytes()

	@property
	def nyusen_tosu(self):
		return self.__nyusen_tosu

	@nyusen_tosu.setter
	def nyusen_tosu(self, value):
		self.__nyusen_tosu = value

	'''
	天候・馬場状態コード
	'''
	__tenko_baba = None

	@property
	def tenko_baba(self):
		return self.__tenko_baba

	@tenko_baba.setter
	def tenko_baba(self, value):
		self.__tenko_baba = value

	'''
	ラップタイム
	'''
	__lap_time = []

	@property
	def lap_time(self):
		return self.__lap_time

	@lap_time.setter
	def lap_time(self, value):
		self.__lap_time = value

	'''
	障害マイルタイム
	'''
	__syogai_mile_time = bytes()

	@property
	def syogai_mile_time(self):
		return self.__syogai_mile_time

	@syogai_mile_time.setter
	def syogai_mile_time(self, value):
		self.__syogai_mile_time = value

	'''
	前３ハロンタイム
	'''
	__haron_time_s3 = bytes()

	@property
	def haron_time_s3(self):
		return self.__haron_time_s3

	@haron_time_s3.setter
	def haron_time_s3(self, value):
		self.__haron_time_s3 = value

	'''
	前４ハロンタイム
	'''
	__haron_time_s4 = bytes()

	@property
	def haron_time_s4(self):
		return self.__haron_time_s4

	@haron_time_s4.setter
	def haron_time_s4(self, value):
		self.__haron_time_s4 = value

	'''
	後３ハロンタイム
	'''
	__haron_time_l3 = bytes()

	@property
	def haron_time_l3(self):
		return self.__haron_time_l3

	@haron_time_l3.setter
	def haron_time_l3(self, value):
		self.__haron_time_l3 = value

	'''
	後４ハロンタイム
	'''
	__haron_time_l4 = bytes()

	@property
	def haron_time_l4(self):
		return self.__haron_time_l4

	@haron_time_l4.setter
	def haron_time_l4(self, value):
		self.__haron_time_l4 = value

	'''
	コーナー通過順位
	'''
	__corner_info = []

	@property
	def corner_info(self):
		return self.__corner_info

	@corner_info.setter
	def corner_info(self, value):
		self.__corner_info = value

	'''
	レコード更新区分
	'''
	__record_up_kubun = bytes()

	@property
	def record_up_kubun(self):
		return self.__record_up_kubun

	@record_up_kubun.setter
	def record_up_kubun(self, value):
		self.__record_up_kubun = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__race_info = RACE_INFO(source[27:614])
		self.__grade_cd = source[614:615]
		self.__grade_cd_before = source[615:616]
		self.__jyoken_info = RACE_JYOKEN(source[616:637])
		self.__jyoken_name = source[637:697]
		self.__kyori = source[697:701]
		self.__kyori_before = source[701:705]
		self.__track_cd = source[705:707]
		self.__track_cd_before = source[707:709]
		self.__course_kubun_cd = source[709:711]
		self.__course_kubun_cd_before = source[711:713]
		self.__honsyokin = []
		for i in range(7):
			self.__honsyokin.append(source[713 + i * 8:713 + i * 8 + 8])
		self.__honsyokin_before = []
		for i in range(5):
			self.__honsyokin_before.append(source[769 + i * 8:769 + i * 8 + 8])
		self.__fukasyokin = []
		for i in range(5):
			self.__fukasyokin.append(source[809 + i * 8:809 + i * 8 + 8])
		self.__fukasyokin_before = []
		for i in range(3):
			self.__fukasyokin_before.append(source[849 + i * 8:849 + i * 8 + 8])
		self.__hasso_time = source[873:877]
		self.__hasso_time_before = source[877:881]
		self.__toroku_tosu = source[881:883]
		self.__syusso_tosu = source[883:885]
		self.__nyusen_tosu = source[885:887]
		self.__tenko_baba = TENKO_BABA_INFO(source[887:890])
		self.__lap_time = []
		for i in range(25):
			self.__lap_time.append(source[890 + i * 3:890 + i * 3 + 3])
		self.__syogai_mile_time = source[965:969]
		self.__haron_time_s3 = source[969:972]
		self.__haron_time_s4 = source[972:975]
		self.__haron_time_l3 = source[975:978]
		self.__haron_time_l4 = source[978:981]

		self.__corner_info = []
		for i in range(4):
			self.__corner_info.append(CORNER_INFO(source[981 + i * 72 :981 + i * 72 + 72]))

		self.__record_up_kubun = source[1269:1270]
		self.__crlf = source[1270:1272]

class CHAKUUMA_INFO:

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	def __init__(self, source : bytes) -> None:

		self.__ketto_num = source[0:10]
		self.__bamei = source[10:46]

class JV_SE_RACE_UMA:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	枠番
	'''
	__wakuban = bytes()

	@property
	def wakuban(self):
		return self.__wakuban

	@wakuban.setter
	def wakuban(self, value):
		self.__wakuban = value

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	馬記号コード
	'''
	__uma_kigo_cd = bytes()

	@property
	def uma_kigo_cd(self):
		return self.__uma_kigo_cd

	@uma_kigo_cd.setter
	def uma_kigo_cd(self, value):
		self.__uma_kigo_cd = value

	'''
	性別コード
	'''
	__sex_cd = bytes()

	@property
	def sex_cd(self):
		return self.__sex_cd

	@sex_cd.setter
	def sex_cd(self, value):
		self.__sex_cd = value

	'''
	品種コード
	'''
	__hinsyu_cd = bytes()

	@property
	def hinsyu_cd(self):
		return self.__hinsyu_cd

	@hinsyu_cd.setter
	def hinsyu_cd(self, value):
		self.__hinsyu_cd = value

	'''
	毛色コード
	'''
	__keiro_cd = bytes()

	@property
	def keiro_cd(self):
		return self.__keiro_cd

	@keiro_cd.setter
	def keiro_cd(self, value):
		self.__keiro_cd = value

	'''
	馬齢
	'''
	__barei = bytes()

	@property
	def barei(self):
		return self.__barei

	@barei.setter
	def barei(self, value):
		self.__barei = value

	'''
	東西所属コード
	'''
	__tozai_cd = bytes()

	@property
	def tozai_cd(self):
		return self.__tozai_cd

	@tozai_cd.setter
	def tozai_cd(self, value):
		self.__tozai_cd = value

	'''
	調教師コード
	'''
	__chokyosi_cd = bytes()

	@property
	def chokyosi_cd(self):
		return self.__chokyosi_cd

	@chokyosi_cd.setter
	def chokyosi_cd(self, value):
		self.__chokyosi_cd = value

	'''
	調教師名略称
	'''
	__chokyosi_ryakusyo = bytes()

	@property
	def chokyosi_ryakusyo(self):
		return self.__chokyosi_ryakusyo

	@chokyosi_ryakusyo.setter
	def chokyosi_ryakusyo(self, value):
		self.__chokyosi_ryakusyo = value

	'''
	馬主コード
	'''
	__banusi_cd = bytes()

	@property
	def banusi_cd(self):
		return self.__banusi_cd

	@banusi_cd.setter
	def banusi_cd(self, value):
		self.__banusi_cd = value

	'''
	馬主名
	'''
	__banusi_name = bytes()

	@property
	def banusi_name(self):
		return self.__banusi_name

	@banusi_name.setter
	def banusi_name(self, value):
		self.__banusi_name = value

	'''
	服色標示
	'''
	__fukusyoku = bytes()

	@property
	def fukusyoku(self):
		return self.__fukusyoku

	@fukusyoku.setter
	def fukusyoku(self, value):
		self.__fukusyoku = value

	'''
	予備
	'''
	__reserved1 = bytes()

	@property
	def reserved1(self):
		return self.__reserved1

	@reserved1.setter
	def reserved1(self, value):
		self.__reserved1 = value

	'''
	負担重量
	'''
	__futan = bytes()

	@property
	def futan(self):
		return self.__futan

	@futan.setter
	def futan(self, value):
		self.__futan = value

	'''
	変更前負担重量
	'''
	__futan_before = bytes()

	@property
	def futan_before(self):
		return self.__futan_before

	@futan_before.setter
	def futan_before(self, value):
		self.__futan_before = value

	'''
	ブリンカー使用区分
	'''
	__blinker = bytes()

	@property
	def blinker(self):
		return self.__blinker

	@blinker.setter
	def blinker(self, value):
		self.__blinker = value

	'''
	予備
	'''
	__reserved2 = bytes()

	@property
	def reserved2(self):
		return self.__reserved2

	@reserved2.setter
	def reserved2(self, value):
		self.__reserved2 = value

	'''
	騎手コード
	'''
	__kisyu_cd = bytes()

	@property
	def kisyu_cd(self):
		return self.__kisyu_cd

	@kisyu_cd.setter
	def kisyu_cd(self, value):
		self.__kisyu_cd = value

	'''
	変更前騎手コード
	'''
	__kisyu_cd_before = bytes()

	@property
	def kisyu_cd_before(self):
		return self.__kisyu_cd_before

	@kisyu_cd_before.setter
	def kisyu_cd_before(self, value):
		self.__kisyu_cd_before = value

	'''
	騎手名略称
	'''
	__kisyu_ryakusyo = bytes()

	@property
	def kisyu_ryakusyo(self):
		return self.__kisyu_ryakusyo

	@kisyu_ryakusyo.setter
	def kisyu_ryakusyo(self, value):
		self.__kisyu_ryakusyo = value

	'''
	変更前騎手名略称
	'''
	__kisyu_ryakusyo_before = bytes()

	@property
	def kisyu_ryakusyo_before(self):
		return self.__kisyu_ryakusyo_before

	@kisyu_ryakusyo_before.setter
	def kisyu_ryakusyo_before(self, value):
		self.__kisyu_ryakusyo_before = value

	'''
	騎手見習コード
	'''
	__minarai_cd = bytes()

	@property
	def minarai_cd(self):
		return self.__minarai_cd

	@minarai_cd.setter
	def minarai_cd(self, value):
		self.__minarai_cd = value

	'''
	変更前騎手見習コード
	'''
	__minarai_cd_before = bytes()

	@property
	def minarai_cd_before(self):
		return self.__minarai_cd_before

	@minarai_cd_before.setter
	def minarai_cd_before(self, value):
		self.__minarai_cd_before = value

	'''
	馬体重
	'''
	__ba_taijyu = bytes()

	@property
	def ba_taijyu(self):
		return self.__ba_taijyu

	@ba_taijyu.setter
	def ba_taijyu(self, value):
		self.__ba_taijyu = value

	'''
	増減符号
	'''
	__zogen_fugo = bytes()

	@property
	def zogen_fugo(self):
		return self.__zogen_fugo

	@zogen_fugo.setter
	def zogen_fugo(self, value):
		self.__zogen_fugo = value

	'''
	増減差
	'''
	__zogen_sa = bytes()

	@property
	def zogen_sa(self):
		return self.__zogen_sa

	@zogen_sa.setter
	def zogen_sa(self, value):
		self.__zogen_sa = value

	'''
	異常区分コード
	'''
	__ijyo_cd = bytes()

	@property
	def ijyo_cd(self):
		return self.__ijyo_cd

	@ijyo_cd.setter
	def ijyo_cd(self, value):
		self.__ijyo_cd = value

	'''
	入線順位
	'''
	__nyusen_jyuni = bytes()

	@property
	def nyusen_jyuni(self):
		return self.__nyusen_jyuni

	@nyusen_jyuni.setter
	def nyusen_jyuni(self, value):
		self.__nyusen_jyuni = value

	'''
	確定着順
	'''
	__kakutei_jyuni = bytes()

	@property
	def kakutei_jyuni(self):
		return self.__kakutei_jyuni

	@kakutei_jyuni.setter
	def kakutei_jyuni(self, value):
		self.__kakutei_jyuni = value

	'''
	同着区分
	'''
	__dochaku_kubun = bytes()

	@property
	def dochaku_kubun(self):
		return self.__dochaku_kubun

	@dochaku_kubun.setter
	def dochaku_kubun(self, value):
		self.__dochaku_kubun = value

	'''
	同着頭数
	'''
	__dochaku_tosu = bytes()

	@property
	def dochaku_tosu(self):
		return self.__dochaku_tosu

	@dochaku_tosu.setter
	def dochaku_tosu(self, value):
		self.__dochaku_tosu = value

	'''
	走破タイム
	'''
	__time = bytes()

	@property
	def time(self):
		return self.__time

	@time.setter
	def time(self, value):
		self.__time = value

	'''
	着差コード
	'''
	__chakusa_cd = bytes()

	@property
	def chakusa_cd(self):
		return self.__chakusa_cd

	@chakusa_cd.setter
	def chakusa_cd(self, value):
		self.__chakusa_cd = value

	'''
	+着差コード
	'''
	__chakusa_cd_p = bytes()

	@property
	def chakusa_cd_p(self):
		return self.__chakusa_cd_p

	@chakusa_cd_p.setter
	def chakusa_cd_p(self, value):
		self.__chakusa_cd_p = value

	'''
	++着差コード
	'''
	__chakusa_cd_p_p = bytes()

	@property
	def chakusa_cd_p_p(self):
		return self.__chakusa_cd_p_p

	@chakusa_cd_p_p.setter
	def chakusa_cd_p_p(self, value):
		self.__chakusa_cd_p_p = value

	'''
	1コーナーでの順位
	'''
	__jyuni1c = bytes()

	@property
	def jyuni1c(self):
		return self.__jyuni1c

	@jyuni1c.setter
	def jyuni1c(self, value):
		self.__jyuni1c = value

	'''
	2コーナーでの順位
	'''
	__jyuni2c = bytes()

	@property
	def jyuni2c(self):
		return self.__jyuni2c

	@jyuni2c.setter
	def jyuni2c(self, value):
		self.__jyuni2c = value

	'''
	3コーナーでの順位
	'''
	__jyuni3c = bytes()

	@property
	def jyuni3c(self):
		return self.__jyuni3c

	@jyuni3c.setter
	def jyuni3c(self, value):
		self.__jyuni3c = value

	'''
	4コーナーでの順位
	'''
	__jyuni4c = bytes()

	@property
	def jyuni4c(self):
		return self.__jyuni4c

	@jyuni4c.setter
	def jyuni4c(self, value):
		self.__jyuni4c = value

	'''
	単勝オッズ
	'''
	__odds = bytes()

	@property
	def odds(self):
		return self.__odds

	@odds.setter
	def odds(self, value):
		self.__odds = value

	'''
	単勝人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	'''
	獲得本賞金
	'''
	__honsyokin = bytes()

	@property
	def honsyokin(self):
		return self.__honsyokin

	@honsyokin.setter
	def honsyokin(self, value):
		self.__honsyokin = value

	'''
	獲得付加賞金
	'''
	__fukasyokin = bytes()

	@property
	def fukasyokin(self):
		return self.__fukasyokin

	@fukasyokin.setter
	def fukasyokin(self, value):
		self.__fukasyokin = value

	'''
	予備
	'''
	__reserved3 = bytes()

	@property
	def reserved3(self):
		return self.__reserved3

	@reserved3.setter
	def reserved3(self, value):
		self.__reserved3 = value

	'''
	予備
	'''
	__reserved4 = bytes()

	@property
	def reserved4(self):
		return self.__reserved4

	@reserved4.setter
	def reserved4(self, value):
		self.__reserved4 = value

	'''
	後４ハロンタイム
	'''
	__haron_time_l4 = bytes()

	@property
	def haron_time_l4(self):
		return self.__haron_time_l4

	@haron_time_l4.setter
	def haron_time_l4(self, value):
		self.__haron_time_l4 = value

	'''
	後３ハロンタイム
	'''
	__haron_time_l3 = bytes()

	@property
	def haron_time_l3(self):
		return self.__haron_time_l3

	@haron_time_l3.setter
	def haron_time_l3(self, value):
		self.__haron_time_l3 = value

	'''
	1着馬(相手馬)情報
	'''
	__chaku_uma_info = []

	@property
	def chaku_uma_info(self):
		return self.__chaku_uma_info

	@chaku_uma_info.setter
	def chaku_uma_info(self, value):
		self.__chaku_uma_info = value

	'''
	タイム差
	'''
	__time_diff = bytes()

	@property
	def time_diff(self):
		return self.__time_diff

	@time_diff.setter
	def time_diff(self, value):
		self.__time_diff = value

	'''
	レコード更新区分
	'''
	__record_up_kubun = bytes()

	@property
	def record_up_kubun(self):
		return self.__record_up_kubun

	@record_up_kubun.setter
	def record_up_kubun(self, value):
		self.__record_up_kubun = value

	'''
	マイニング区分
	'''
	__d_m_kubun = bytes()

	@property
	def d_m_kubun(self):
		return self.__d_m_kubun

	@d_m_kubun.setter
	def d_m_kubun(self, value):
		self.__d_m_kubun = value

	'''
	マイニング予想走破タイム
	'''
	__d_m_time = bytes()

	@property
	def d_m_time(self):
		return self.__d_m_time

	@d_m_time.setter
	def d_m_time(self, value):
		self.__d_m_time = value

	'''
	予測誤差(信頼度)＋
	'''
	__d_m_gosa_p = bytes()

	@property
	def d_m_gosa_p(self):
		return self.__d_m_gosa_p

	@d_m_gosa_p.setter
	def d_m_gosa_p(self, value):
		self.__d_m_gosa_p = value

	'''
	予測誤差(信頼度)－
	'''
	__d_m_gosa_m = bytes()

	@property
	def d_m_gosa_m(self):
		return self.__d_m_gosa_m

	@d_m_gosa_m.setter
	def d_m_gosa_m(self, value):
		self.__d_m_gosa_m = value

	'''
	マイニング予想順位
	'''
	__d_m_jyuni = bytes()

	@property
	def d_m_jyuni(self):
		return self.__d_m_jyuni

	@d_m_jyuni.setter
	def d_m_jyuni(self, value):
		self.__d_m_jyuni = value

	'''
	今回レース脚質判定
	'''
	__kyakusitu_kubun = bytes()

	@property
	def kyakusitu_kubun(self):
		return self.__kyakusitu_kubun

	@kyakusitu_kubun.setter
	def kyakusitu_kubun(self, value):
		self.__kyakusitu_kubun = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__wakuban = source[27:28]
		self.__umaban = source[28:30]
		self.__ketto_num = source[30:40]
		self.__bamei = source[40:76]
		self.__uma_kigo_cd = source[76:78]
		self.__sex_cd = source[78:79]
		self.__hinsyu_cd = source[79:80]
		self.__keiro_cd = source[80:82]
		self.__barei = source[82:84]
		self.__tozai_cd = source[84:85]
		self.__chokyosi_cd = source[85:90]
		self.__chokyosi_ryakusyo = source[90:98]
		self.__banusi_cd = source[98:104]
		self.__banusi_name = source[104:168]
		self.__fukusyoku = source[168:228]
		self.__reserved1 = source[228:288]
		self.__futan = source[288:291]
		self.__futan_before = source[291:294]
		self.__blinker = source[294:295]
		self.__reserved2 = source[295:296]
		self.__kisyu_cd = source[296:301]
		self.__kisyu_cd_before = source[301:306]
		self.__kisyu_ryakusyo = source[306:314]
		self.__kisyu_ryakusyo_before = source[314:322]
		self.__minarai_cd = source[322:323]
		self.__minarai_cd_before = source[323:324]
		self.__ba_taijyu = source[324:327]
		self.__zogen_fugo = source[327:328]
		self.__zogen_sa = source[328:331]
		self.__ijyo_cd = source[331:332]
		self.__nyusen_jyuni = source[332:334]
		self.__kakutei_jyuni = source[334:336]
		self.__dochaku_kubun = source[336:337]
		self.__dochaku_tosu = source[337:338]
		self.__time = source[338:342]
		self.__chakusa_cd = source[342:345]
		self.__chakusa_cd_p = source[345:348]
		self.__chakusa_cd_p_p = source[348:351]
		self.__jyuni1c = source[351:353]
		self.__jyuni2c = source[353:355]
		self.__jyuni3c = source[355:357]
		self.__jyuni4c = source[357:359]
		self.__odds = source[359:363]
		self.__ninki = source[363:365]
		self.__honsyokin = source[365:373]
		self.__fukasyokin = source[373:381]
		self.__reserved3 = source[381:384]
		self.__reserved4 = source[384:387]
		self.__haron_time_l4 = source[387:390]
		self.__haron_time_l3 = source[390:393]

		self.__chaku_uma_info = []
		for i in range(3):
			self.__chaku_uma_info.append(CHAKUUMA_INFO(source[393 + i * 46 :393 + i * 46 + 46]))

		self.__time_diff = source[531:535]
		self.__record_up_kubun = source[535:536]
		self.__d_m_kubun = source[536:537]
		self.__d_m_time = source[537:542]
		self.__d_m_gosa_p = source[542:546]
		self.__d_m_gosa_m = source[546:550]
		self.__d_m_jyuni = source[550:552]
		self.__kyakusitu_kubun = source[552:553]
		self.__crlf = source[553:555]

class PAY_INFO1:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	払戻金
	'''
	__pay = bytes()

	@property
	def pay(self):
		return self.__pay

	@pay.setter
	def pay(self, value):
		self.__pay = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:2]
		self.__pay = source[2:11]
		self.__ninki = source[11:13]

class PAY_INFO2:

	'''
	組番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	払戻金
	'''
	__pay = bytes()

	@property
	def pay(self):
		return self.__pay

	@pay.setter
	def pay(self, value):
		self.__pay = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:4]
		self.__pay = source[4:13]
		self.__ninki = source[13:16]

class PAY_INFO3:

	'''
	組番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	払戻金
	'''
	__pay = bytes()

	@property
	def pay(self):
		return self.__pay

	@pay.setter
	def pay(self, value):
		self.__pay = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:6]
		self.__pay = source[6:15]
		self.__ninki = source[15:18]

class PAY_INFO4:

	'''
	組番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	払戻金
	'''
	__pay = bytes()

	@property
	def pay(self):
		return self.__pay

	@pay.setter
	def pay(self, value):
		self.__pay = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:6]
		self.__pay = source[6:15]
		self.__ninki = source[15:19]

class JV_HR_PAY:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	不成立フラグ
	'''
	__fuseiritu_flag = []

	@property
	def fuseiritu_flag(self):
		return self.__fuseiritu_flag

	@fuseiritu_flag.setter
	def fuseiritu_flag(self, value):
		self.__fuseiritu_flag = value

	'''
	特払フラグ
	'''
	__tokubarai_flag = []

	@property
	def tokubarai_flag(self):
		return self.__tokubarai_flag

	@tokubarai_flag.setter
	def tokubarai_flag(self, value):
		self.__tokubarai_flag = value

	'''
	返還フラグ
	'''
	__henkan_flag = []

	@property
	def henkan_flag(self):
		return self.__henkan_flag

	@henkan_flag.setter
	def henkan_flag(self, value):
		self.__henkan_flag = value

	'''
	返還馬番情報(馬番01～28)
	'''
	__henkan_uma = []

	@property
	def henkan_uma(self):
		return self.__henkan_uma

	@henkan_uma.setter
	def henkan_uma(self, value):
		self.__henkan_uma = value

	'''
	返還枠番情報(枠番1～8)
	'''
	__henkan_waku = []

	@property
	def henkan_waku(self):
		return self.__henkan_waku

	@henkan_waku.setter
	def henkan_waku(self, value):
		self.__henkan_waku = value

	'''
	返還同枠情報(枠番1～8)
	'''
	__henkan_do_waku = []

	@property
	def henkan_do_waku(self):
		return self.__henkan_do_waku

	@henkan_do_waku.setter
	def henkan_do_waku(self, value):
		self.__henkan_do_waku = value

	'''
	単勝払戻
	'''
	__pay_tansyo = []

	@property
	def pay_tansyo(self):
		return self.__pay_tansyo

	@pay_tansyo.setter
	def pay_tansyo(self, value):
		self.__pay_tansyo = value

	'''
	複勝払戻
	'''
	__pay_fukusyo = []

	@property
	def pay_fukusyo(self):
		return self.__pay_fukusyo

	@pay_fukusyo.setter
	def pay_fukusyo(self, value):
		self.__pay_fukusyo = value

	'''
	枠連払戻
	'''
	__pay_wakuren = []

	@property
	def pay_wakuren(self):
		return self.__pay_wakuren

	@pay_wakuren.setter
	def pay_wakuren(self, value):
		self.__pay_wakuren = value

	'''
	馬連払戻
	'''
	__pay_umaren = []

	@property
	def pay_umaren(self):
		return self.__pay_umaren

	@pay_umaren.setter
	def pay_umaren(self, value):
		self.__pay_umaren = value

	'''
	ワイド払戻
	'''
	__pay_wide = []

	@property
	def pay_wide(self):
		return self.__pay_wide

	@pay_wide.setter
	def pay_wide(self, value):
		self.__pay_wide = value

	'''
	予備
	'''
	__pay_reserved1 = []

	@property
	def pay_reserved1(self):
		return self.__pay_reserved1

	@pay_reserved1.setter
	def pay_reserved1(self, value):
		self.__pay_reserved1 = value

	'''
	馬単払戻
	'''
	__pay_umatan = []

	@property
	def pay_umatan(self):
		return self.__pay_umatan

	@pay_umatan.setter
	def pay_umatan(self, value):
		self.__pay_umatan = value

	'''
	3連複払戻
	'''
	__pay_sanrenpuku = []

	@property
	def pay_sanrenpuku(self):
		return self.__pay_sanrenpuku

	@pay_sanrenpuku.setter
	def pay_sanrenpuku(self, value):
		self.__pay_sanrenpuku = value

	'''
	3連単払戻
	'''
	__pay_sanrentan = []

	@property
	def pay_sanrentan(self):
		return self.__pay_sanrentan

	@pay_sanrentan.setter
	def pay_sanrentan(self, value):
		self.__pay_sanrentan = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__toroku_tosu = source[27:29]
		self.__syusso_tosu = source[29:31]
		self.__fuseiritu_flag = []
		for i in range(9):
			self.__fuseiritu_flag.append(source[31 + i * 1:31 + i * 1 + 1])
		self.__tokubarai_flag = []
		for i in range(9):
			self.__tokubarai_flag.append(source[40 + i * 1:40 + i * 1 + 1])
		self.__henkan_flag = []
		for i in range(9):
			self.__henkan_flag.append(source[49 + i * 1:49 + i * 1 + 1])
		self.__henkan_uma = []
		for i in range(28):
			self.__henkan_uma.append(source[58 + i * 1:58 + i * 1 + 1])
		self.__henkan_waku = []
		for i in range(8):
			self.__henkan_waku.append(source[86 + i * 1:86 + i * 1 + 1])
		self.__henkan_do_waku = []
		for i in range(8):
			self.__henkan_do_waku.append(source[94 + i * 1:94 + i * 1 + 1])

		self.__pay_tansyo = []
		for i in range(3):
			self.__pay_tansyo.append(PAY_INFO1(source[102 + i * 13 :102 + i * 13 + 13]))

		self.__pay_fukusyo = []
		for i in range(5):
			self.__pay_fukusyo.append(PAY_INFO1(source[141 + i * 13 :141 + i * 13 + 13]))

		self.__pay_wakuren = []
		for i in range(3):
			self.__pay_wakuren.append(PAY_INFO1(source[206 + i * 13 :206 + i * 13 + 13]))

		self.__pay_umaren = []
		for i in range(3):
			self.__pay_umaren.append(PAY_INFO2(source[245 + i * 16 :245 + i * 16 + 16]))

		self.__pay_wide = []
		for i in range(7):
			self.__pay_wide.append(PAY_INFO2(source[293 + i * 16 :293 + i * 16 + 16]))

		self.__pay_reserved1 = []
		for i in range(3):
			self.__pay_reserved1.append(PAY_INFO2(source[405 + i * 16 :405 + i * 16 + 16]))

		self.__pay_umatan = []
		for i in range(6):
			self.__pay_umatan.append(PAY_INFO2(source[453 + i * 16 :453 + i * 16 + 16]))

		self.__pay_sanrenpuku = []
		for i in range(3):
			self.__pay_sanrenpuku.append(PAY_INFO3(source[549 + i * 18 :549 + i * 18 + 18]))

		self.__pay_sanrentan = []
		for i in range(6):
			self.__pay_sanrentan.append(PAY_INFO4(source[603 + i * 19 :603 + i * 19 + 19]))

		self.__crlf = source[717:719]

class HYO_INFO1:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	票数
	'''
	__hyo = bytes()

	@property
	def hyo(self):
		return self.__hyo

	@hyo.setter
	def hyo(self, value):
		self.__hyo = value

	'''
	人気
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:2]
		self.__hyo = source[2:13]
		self.__ninki = source[13:15]

class HYO_INFO2:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	票数
	'''
	__hyo = bytes()

	@property
	def hyo(self):
		return self.__hyo

	@hyo.setter
	def hyo(self, value):
		self.__hyo = value

	'''
	人気
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:4]
		self.__hyo = source[4:15]
		self.__ninki = source[15:18]

class HYO_INFO3:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	票数
	'''
	__hyo = bytes()

	@property
	def hyo(self):
		return self.__hyo

	@hyo.setter
	def hyo(self, value):
		self.__hyo = value

	'''
	人気
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:6]
		self.__hyo = source[6:17]
		self.__ninki = source[17:20]

class HYO_INFO4:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	票数
	'''
	__hyo = bytes()

	@property
	def hyo(self):
		return self.__hyo

	@hyo.setter
	def hyo(self, value):
		self.__hyo = value

	'''
	人気
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:6]
		self.__hyo = source[6:17]
		self.__ninki = source[17:21]

class JV_H1_HYOSU_ZENKAKE:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	発売フラグ
	'''
	__hatubai_flag = []

	@property
	def hatubai_flag(self):
		return self.__hatubai_flag

	@hatubai_flag.setter
	def hatubai_flag(self, value):
		self.__hatubai_flag = value

	'''
	複勝着払キー
	'''
	__fuku_chaku_barai_key = bytes()

	@property
	def fuku_chaku_barai_key(self):
		return self.__fuku_chaku_barai_key

	@fuku_chaku_barai_key.setter
	def fuku_chaku_barai_key(self, value):
		self.__fuku_chaku_barai_key = value

	'''
	返還馬番情報(馬番01～28)
	'''
	__henkan_uma = []

	@property
	def henkan_uma(self):
		return self.__henkan_uma

	@henkan_uma.setter
	def henkan_uma(self, value):
		self.__henkan_uma = value

	'''
	返還枠番情報(枠番1～8)
	'''
	__henkan_waku = []

	@property
	def henkan_waku(self):
		return self.__henkan_waku

	@henkan_waku.setter
	def henkan_waku(self, value):
		self.__henkan_waku = value

	'''
	返還同枠情報(枠番1～8)
	'''
	__henkan_do_waku = []

	@property
	def henkan_do_waku(self):
		return self.__henkan_do_waku

	@henkan_do_waku.setter
	def henkan_do_waku(self, value):
		self.__henkan_do_waku = value

	'''
	単勝票数
	'''
	__hyo_tansyo = []

	@property
	def hyo_tansyo(self):
		return self.__hyo_tansyo

	@hyo_tansyo.setter
	def hyo_tansyo(self, value):
		self.__hyo_tansyo = value

	'''
	複勝票数
	'''
	__hyo_fukusyo = []

	@property
	def hyo_fukusyo(self):
		return self.__hyo_fukusyo

	@hyo_fukusyo.setter
	def hyo_fukusyo(self, value):
		self.__hyo_fukusyo = value

	'''
	枠連票数
	'''
	__hyo_wakuren = []

	@property
	def hyo_wakuren(self):
		return self.__hyo_wakuren

	@hyo_wakuren.setter
	def hyo_wakuren(self, value):
		self.__hyo_wakuren = value

	'''
	馬連票数
	'''
	__hyo_umaren = []

	@property
	def hyo_umaren(self):
		return self.__hyo_umaren

	@hyo_umaren.setter
	def hyo_umaren(self, value):
		self.__hyo_umaren = value

	'''
	ワイド票数
	'''
	__hyo_wide = []

	@property
	def hyo_wide(self):
		return self.__hyo_wide

	@hyo_wide.setter
	def hyo_wide(self, value):
		self.__hyo_wide = value

	'''
	馬単票数
	'''
	__hyo_umatan = []

	@property
	def hyo_umatan(self):
		return self.__hyo_umatan

	@hyo_umatan.setter
	def hyo_umatan(self, value):
		self.__hyo_umatan = value

	'''
	3連複票数
	'''
	__hyo_sanrenpuku = []

	@property
	def hyo_sanrenpuku(self):
		return self.__hyo_sanrenpuku

	@hyo_sanrenpuku.setter
	def hyo_sanrenpuku(self, value):
		self.__hyo_sanrenpuku = value

	'''
	票数合計
	'''
	__hyo_total = []

	@property
	def hyo_total(self):
		return self.__hyo_total

	@hyo_total.setter
	def hyo_total(self, value):
		self.__hyo_total = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__toroku_tosu = source[27:29]
		self.__syusso_tosu = source[29:31]
		self.__hatubai_flag = []
		for i in range(7):
			self.__hatubai_flag.append(source[31 + i * 1:31 + i * 1 + 1])
		self.__fuku_chaku_barai_key = source[38:39]
		self.__henkan_uma = []
		for i in range(28):
			self.__henkan_uma.append(source[39 + i * 1:39 + i * 1 + 1])
		self.__henkan_waku = []
		for i in range(8):
			self.__henkan_waku.append(source[67 + i * 1:67 + i * 1 + 1])
		self.__henkan_do_waku = []
		for i in range(8):
			self.__henkan_do_waku.append(source[75 + i * 1:75 + i * 1 + 1])

		self.__hyo_tansyo = []
		for i in range(28):
			self.__hyo_tansyo.append(HYO_INFO1(source[83 + i * 15 :83 + i * 15 + 15]))

		self.__hyo_fukusyo = []
		for i in range(28):
			self.__hyo_fukusyo.append(HYO_INFO1(source[503 + i * 15 :503 + i * 15 + 15]))

		self.__hyo_wakuren = []
		for i in range(36):
			self.__hyo_wakuren.append(HYO_INFO1(source[923 + i * 15 :923 + i * 15 + 15]))

		self.__hyo_umaren = []
		for i in range(153):
			self.__hyo_umaren.append(HYO_INFO2(source[1463 + i * 18 :1463 + i * 18 + 18]))

		self.__hyo_wide = []
		for i in range(153):
			self.__hyo_wide.append(HYO_INFO2(source[4217 + i * 18 :4217 + i * 18 + 18]))

		self.__hyo_umatan = []
		for i in range(306):
			self.__hyo_umatan.append(HYO_INFO2(source[6971 + i * 18 :6971 + i * 18 + 18]))

		self.__hyo_sanrenpuku = []
		for i in range(816):
			self.__hyo_sanrenpuku.append(HYO_INFO3(source[12479 + i * 20 :12479 + i * 20 + 20]))

		self.__hyo_total = []
		for i in range(14):
			self.__hyo_total.append(source[28799 + i * 11:28799 + i * 11 + 11])
		self.__crlf = source[28953:28955]

class JV_H6_HYOSU_SANRENTAN:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	発売フラグ
	'''
	__hatubai_flag = bytes()

	@property
	def hatubai_flag(self):
		return self.__hatubai_flag

	@hatubai_flag.setter
	def hatubai_flag(self, value):
		self.__hatubai_flag = value

	'''
	返還馬番情報(馬番01～18)
	'''
	__henkan_uma = []

	@property
	def henkan_uma(self):
		return self.__henkan_uma

	@henkan_uma.setter
	def henkan_uma(self, value):
		self.__henkan_uma = value

	'''
	3連単票数
	'''
	__hyo_sanrentan = []

	@property
	def hyo_sanrentan(self):
		return self.__hyo_sanrentan

	@hyo_sanrentan.setter
	def hyo_sanrentan(self, value):
		self.__hyo_sanrentan = value

	'''
	票数合計
	'''
	__hyo_total = []

	@property
	def hyo_total(self):
		return self.__hyo_total

	@hyo_total.setter
	def hyo_total(self, value):
		self.__hyo_total = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__toroku_tosu = source[27:29]
		self.__syusso_tosu = source[29:31]
		self.__hatubai_flag = source[31:32]
		self.__henkan_uma = []
		for i in range(18):
			self.__henkan_uma.append(source[32 + i * 1:32 + i * 1 + 1])

		self.__hyo_sanrentan = []
		for i in range(4896):
			self.__hyo_sanrentan.append(HYO_INFO4(source[50 + i * 21 :50 + i * 21 + 21]))

		self.__hyo_total = []
		for i in range(2):
			self.__hyo_total.append(source[102866 + i * 11:102866 + i * 11 + 11])
		self.__crlf = source[102888:102890]

class ODDS_TANSYO_INFO:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	オッズ
	'''
	__odds = bytes()

	@property
	def odds(self):
		return self.__odds

	@odds.setter
	def odds(self, value):
		self.__odds = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:2]
		self.__odds = source[2:6]
		self.__ninki = source[6:8]

class ODDS_FUKUSYO_INFO:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	最低オッズ
	'''
	__odds_low = bytes()

	@property
	def odds_low(self):
		return self.__odds_low

	@odds_low.setter
	def odds_low(self, value):
		self.__odds_low = value

	'''
	最高オッズ
	'''
	__odds_high = bytes()

	@property
	def odds_high(self):
		return self.__odds_high

	@odds_high.setter
	def odds_high(self, value):
		self.__odds_high = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:2]
		self.__odds_low = source[2:6]
		self.__odds_high = source[6:10]
		self.__ninki = source[10:12]

class ODDS_WAKUREN_INFO:

	'''
	組番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	オッズ
	'''
	__odds = bytes()

	@property
	def odds(self):
		return self.__odds

	@odds.setter
	def odds(self, value):
		self.__odds = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:2]
		self.__odds = source[2:7]
		self.__ninki = source[7:9]

class JV_O1_ODDS_TANFUKUWAKU:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	発売フラグ
	'''
	__tansyo_flag = bytes()

	@property
	def tansyo_flag(self):
		return self.__tansyo_flag

	@tansyo_flag.setter
	def tansyo_flag(self, value):
		self.__tansyo_flag = value

	'''
	発売フラグ
	'''
	__fukusyo_flag = bytes()

	@property
	def fukusyo_flag(self):
		return self.__fukusyo_flag

	@fukusyo_flag.setter
	def fukusyo_flag(self, value):
		self.__fukusyo_flag = value

	'''
	発売フラグ
	'''
	__wakuren_flag = bytes()

	@property
	def wakuren_flag(self):
		return self.__wakuren_flag

	@wakuren_flag.setter
	def wakuren_flag(self, value):
		self.__wakuren_flag = value

	'''
	複勝着払キー
	'''
	__fuku_chaku_barai_key = bytes()

	@property
	def fuku_chaku_barai_key(self):
		return self.__fuku_chaku_barai_key

	@fuku_chaku_barai_key.setter
	def fuku_chaku_barai_key(self, value):
		self.__fuku_chaku_barai_key = value

	'''
	単勝オッズ
	'''
	__odds_tansyo_info = []

	@property
	def odds_tansyo_info(self):
		return self.__odds_tansyo_info

	@odds_tansyo_info.setter
	def odds_tansyo_info(self, value):
		self.__odds_tansyo_info = value

	'''
	複勝票数オッズ
	'''
	__odds_fukusyo_info = []

	@property
	def odds_fukusyo_info(self):
		return self.__odds_fukusyo_info

	@odds_fukusyo_info.setter
	def odds_fukusyo_info(self, value):
		self.__odds_fukusyo_info = value

	'''
	枠連票数オッズ
	'''
	__odds_wakuren_info = []

	@property
	def odds_wakuren_info(self):
		return self.__odds_wakuren_info

	@odds_wakuren_info.setter
	def odds_wakuren_info(self, value):
		self.__odds_wakuren_info = value

	'''
	単勝票数合計
	'''
	__total_hyosu_tansyo = bytes()

	@property
	def total_hyosu_tansyo(self):
		return self.__total_hyosu_tansyo

	@total_hyosu_tansyo.setter
	def total_hyosu_tansyo(self, value):
		self.__total_hyosu_tansyo = value

	'''
	複勝票数合計
	'''
	__total_hyosu_fukusyo = bytes()

	@property
	def total_hyosu_fukusyo(self):
		return self.__total_hyosu_fukusyo

	@total_hyosu_fukusyo.setter
	def total_hyosu_fukusyo(self, value):
		self.__total_hyosu_fukusyo = value

	'''
	枠連票数合計
	'''
	__total_hyosu_wakuren = bytes()

	@property
	def total_hyosu_wakuren(self):
		return self.__total_hyosu_wakuren

	@total_hyosu_wakuren.setter
	def total_hyosu_wakuren(self, value):
		self.__total_hyosu_wakuren = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__toroku_tosu = source[35:37]
		self.__syusso_tosu = source[37:39]
		self.__tansyo_flag = source[39:40]
		self.__fukusyo_flag = source[40:41]
		self.__wakuren_flag = source[41:42]
		self.__fuku_chaku_barai_key = source[42:43]

		self.__odds_tansyo_info = []
		for i in range(28):
			self.__odds_tansyo_info.append(ODDS_TANSYO_INFO(source[43 + i * 8 :43 + i * 8 + 8]))

		self.__odds_fukusyo_info = []
		for i in range(28):
			self.__odds_fukusyo_info.append(ODDS_FUKUSYO_INFO(source[267 + i * 12 :267 + i * 12 + 12]))

		self.__odds_wakuren_info = []
		for i in range(36):
			self.__odds_wakuren_info.append(ODDS_WAKUREN_INFO(source[603 + i * 9 :603 + i * 9 + 9]))

		self.__total_hyosu_tansyo = source[927:938]
		self.__total_hyosu_fukusyo = source[938:949]
		self.__total_hyosu_wakuren = source[949:960]
		self.__crlf = source[960:962]

class ODDS_UMAREN_INFO:

	'''
	組番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	オッズ
	'''
	__odds = bytes()

	@property
	def odds(self):
		return self.__odds

	@odds.setter
	def odds(self, value):
		self.__odds = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:4]
		self.__odds = source[4:10]
		self.__ninki = source[10:13]

class JV_O2_ODDS_UMAREN:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	発売フラグ
	'''
	__umaren_flag = bytes()

	@property
	def umaren_flag(self):
		return self.__umaren_flag

	@umaren_flag.setter
	def umaren_flag(self, value):
		self.__umaren_flag = value

	'''
	馬連票数オッズ
	'''
	__odds_umaren_info = []

	@property
	def odds_umaren_info(self):
		return self.__odds_umaren_info

	@odds_umaren_info.setter
	def odds_umaren_info(self, value):
		self.__odds_umaren_info = value

	'''
	馬連票数合計
	'''
	__total_hyosu_umaren = bytes()

	@property
	def total_hyosu_umaren(self):
		return self.__total_hyosu_umaren

	@total_hyosu_umaren.setter
	def total_hyosu_umaren(self, value):
		self.__total_hyosu_umaren = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__toroku_tosu = source[35:37]
		self.__syusso_tosu = source[37:39]
		self.__umaren_flag = source[39:40]

		self.__odds_umaren_info = []
		for i in range(153):
			self.__odds_umaren_info.append(ODDS_UMAREN_INFO(source[40 + i * 13 :40 + i * 13 + 13]))

		self.__total_hyosu_umaren = source[2029:2040]
		self.__crlf = source[2040:2042]

class ODDS_WIDE_INFO:

	'''
	組番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	最低オッズ
	'''
	__odds_low = bytes()

	@property
	def odds_low(self):
		return self.__odds_low

	@odds_low.setter
	def odds_low(self, value):
		self.__odds_low = value

	'''
	最高オッズ
	'''
	__odds_high = bytes()

	@property
	def odds_high(self):
		return self.__odds_high

	@odds_high.setter
	def odds_high(self, value):
		self.__odds_high = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:4]
		self.__odds_low = source[4:9]
		self.__odds_high = source[9:14]
		self.__ninki = source[14:17]

class JV_O3_ODDS_WIDE:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	発売フラグ
	'''
	__wide_flag = bytes()

	@property
	def wide_flag(self):
		return self.__wide_flag

	@wide_flag.setter
	def wide_flag(self, value):
		self.__wide_flag = value

	'''
	ワイド票数オッズ
	'''
	__odds_wide_info = []

	@property
	def odds_wide_info(self):
		return self.__odds_wide_info

	@odds_wide_info.setter
	def odds_wide_info(self, value):
		self.__odds_wide_info = value

	'''
	ワイド票数合計
	'''
	__total_hyosu_wide = bytes()

	@property
	def total_hyosu_wide(self):
		return self.__total_hyosu_wide

	@total_hyosu_wide.setter
	def total_hyosu_wide(self, value):
		self.__total_hyosu_wide = value

	'''
	
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__toroku_tosu = source[35:37]
		self.__syusso_tosu = source[37:39]
		self.__wide_flag = source[39:40]

		self.__odds_wide_info = []
		for i in range(153):
			self.__odds_wide_info.append(ODDS_WIDE_INFO(source[40 + i * 17 :40 + i * 17 + 17]))

		self.__total_hyosu_wide = source[2641:2652]
		self.__crlf = source[2652:2654]

class ODDS_UMATAN_INFO:

	'''
	組番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	オッズ
	'''
	__odds = bytes()

	@property
	def odds(self):
		return self.__odds

	@odds.setter
	def odds(self, value):
		self.__odds = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:4]
		self.__odds = source[4:10]
		self.__ninki = source[10:13]

class JV_O4_ODDS_UMATAN:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	発売フラグ
	'''
	__umatan_flag = bytes()

	@property
	def umatan_flag(self):
		return self.__umatan_flag

	@umatan_flag.setter
	def umatan_flag(self, value):
		self.__umatan_flag = value

	'''
	馬単票数オッズ
	'''
	__odds_umatan_info = []

	@property
	def odds_umatan_info(self):
		return self.__odds_umatan_info

	@odds_umatan_info.setter
	def odds_umatan_info(self, value):
		self.__odds_umatan_info = value

	'''
	馬単票数合計
	'''
	__total_hyosu_umatan = bytes()

	@property
	def total_hyosu_umatan(self):
		return self.__total_hyosu_umatan

	@total_hyosu_umatan.setter
	def total_hyosu_umatan(self, value):
		self.__total_hyosu_umatan = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__toroku_tosu = source[35:37]
		self.__syusso_tosu = source[37:39]
		self.__umatan_flag = source[39:40]

		self.__odds_umatan_info = []
		for i in range(306):
			self.__odds_umatan_info.append(ODDS_UMATAN_INFO(source[40 + i * 13 :40 + i * 13 + 13]))

		self.__total_hyosu_umatan = source[4018:4029]
		self.__crlf = source[4029:4031]

class ODDS_SANREN_INFO:

	'''
	組番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	オッズ
	'''
	__odds = bytes()

	@property
	def odds(self):
		return self.__odds

	@odds.setter
	def odds(self, value):
		self.__odds = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:6]
		self.__odds = source[6:12]
		self.__ninki = source[12:15]

class JV_O5_ODDS_SANREN:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	発売フラグ
	'''
	__sanrenpuku_flag = bytes()

	@property
	def sanrenpuku_flag(self):
		return self.__sanrenpuku_flag

	@sanrenpuku_flag.setter
	def sanrenpuku_flag(self, value):
		self.__sanrenpuku_flag = value

	'''
	3連複票数オッズ
	'''
	__odds_sanren_info = []

	@property
	def odds_sanren_info(self):
		return self.__odds_sanren_info

	@odds_sanren_info.setter
	def odds_sanren_info(self, value):
		self.__odds_sanren_info = value

	'''
	3連複票数合計
	'''
	__total_hyosu_sanrenpuku = bytes()

	@property
	def total_hyosu_sanrenpuku(self):
		return self.__total_hyosu_sanrenpuku

	@total_hyosu_sanrenpuku.setter
	def total_hyosu_sanrenpuku(self, value):
		self.__total_hyosu_sanrenpuku = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__toroku_tosu = source[35:37]
		self.__syusso_tosu = source[37:39]
		self.__sanrenpuku_flag = source[39:40]

		self.__odds_sanren_info = []
		for i in range(816):
			self.__odds_sanren_info.append(ODDS_SANREN_INFO(source[40 + i * 15 :40 + i * 15 + 15]))

		self.__total_hyosu_sanrenpuku = source[12280:12291]
		self.__crlf = source[12291:12293]

class ODDS_SANRENTAN_INFO:

	'''
	組番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	オッズ
	'''
	__odds = bytes()

	@property
	def odds(self):
		return self.__odds

	@odds.setter
	def odds(self, value):
		self.__odds = value

	'''
	人気順
	'''
	__ninki = bytes()

	@property
	def ninki(self):
		return self.__ninki

	@ninki.setter
	def ninki(self, value):
		self.__ninki = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:6]
		self.__odds = source[6:13]
		self.__ninki = source[13:17]

class JV_O6_ODDS_SANRENTAN:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	登録頭数
	'''
	__toroku_tosu = bytes()

	@property
	def toroku_tosu(self):
		return self.__toroku_tosu

	@toroku_tosu.setter
	def toroku_tosu(self, value):
		self.__toroku_tosu = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	発売フラグ
	'''
	__sanrentan_flag = bytes()

	@property
	def sanrentan_flag(self):
		return self.__sanrentan_flag

	@sanrentan_flag.setter
	def sanrentan_flag(self, value):
		self.__sanrentan_flag = value

	'''
	3連単票数オッズ
	'''
	__odds_sanrentan_info = []

	@property
	def odds_sanrentan_info(self):
		return self.__odds_sanrentan_info

	@odds_sanrentan_info.setter
	def odds_sanrentan_info(self, value):
		self.__odds_sanrentan_info = value

	'''
	3連単票数合計
	'''
	__total_hyosu_sanrentan = bytes()

	@property
	def total_hyosu_sanrentan(self):
		return self.__total_hyosu_sanrentan

	@total_hyosu_sanrentan.setter
	def total_hyosu_sanrentan(self, value):
		self.__total_hyosu_sanrentan = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__toroku_tosu = source[35:37]
		self.__syusso_tosu = source[37:39]
		self.__sanrentan_flag = source[39:40]

		self.__odds_sanrentan_info = []
		for i in range(4896):
			self.__odds_sanrentan_info.append(ODDS_SANRENTAN_INFO(source[40 + i * 17 :40 + i * 17 + 17]))

		self.__total_hyosu_sanrentan = source[83272:83283]
		self.__crlf = source[83283:83285]

class KETTO3_INFO:

	'''
	繁殖登録番号
	'''
	__hansyoku_num = bytes()

	@property
	def hansyoku_num(self):
		return self.__hansyoku_num

	@hansyoku_num.setter
	def hansyoku_num(self, value):
		self.__hansyoku_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	def __init__(self, source : bytes) -> None:

		self.__hansyoku_num = source[0:8]
		self.__bamei = source[8:44]

class JV_UM_UMA:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	競走馬抹消区分
	'''
	__del_kubun = bytes()

	@property
	def del_kubun(self):
		return self.__del_kubun

	@del_kubun.setter
	def del_kubun(self, value):
		self.__del_kubun = value

	'''
	競走馬登録年月日
	'''
	__reg_date = None

	@property
	def reg_date(self):
		return self.__reg_date

	@reg_date.setter
	def reg_date(self, value):
		self.__reg_date = value

	'''
	競走馬抹消年月日
	'''
	__del_date = None

	@property
	def del_date(self):
		return self.__del_date

	@del_date.setter
	def del_date(self, value):
		self.__del_date = value

	'''
	生年月日
	'''
	__birth_date = None

	@property
	def birth_date(self):
		return self.__birth_date

	@birth_date.setter
	def birth_date(self, value):
		self.__birth_date = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	馬名半角カナ
	'''
	__bamei_kana = bytes()

	@property
	def bamei_kana(self):
		return self.__bamei_kana

	@bamei_kana.setter
	def bamei_kana(self, value):
		self.__bamei_kana = value

	'''
	馬名欧字
	'''
	__bamei_eng = bytes()

	@property
	def bamei_eng(self):
		return self.__bamei_eng

	@bamei_eng.setter
	def bamei_eng(self, value):
		self.__bamei_eng = value

	'''
	JRA施設在きゅうフラグ
	'''
	__zaikyu_flag = bytes()

	@property
	def zaikyu_flag(self):
		return self.__zaikyu_flag

	@zaikyu_flag.setter
	def zaikyu_flag(self, value):
		self.__zaikyu_flag = value

	'''
	予備
	'''
	__reserved = bytes()

	@property
	def reserved(self):
		return self.__reserved

	@reserved.setter
	def reserved(self, value):
		self.__reserved = value

	'''
	馬記号コード
	'''
	__uma_kigo_cd = bytes()

	@property
	def uma_kigo_cd(self):
		return self.__uma_kigo_cd

	@uma_kigo_cd.setter
	def uma_kigo_cd(self, value):
		self.__uma_kigo_cd = value

	'''
	性別コード
	'''
	__sex_cd = bytes()

	@property
	def sex_cd(self):
		return self.__sex_cd

	@sex_cd.setter
	def sex_cd(self, value):
		self.__sex_cd = value

	'''
	品種コード
	'''
	__hinsyu_cd = bytes()

	@property
	def hinsyu_cd(self):
		return self.__hinsyu_cd

	@hinsyu_cd.setter
	def hinsyu_cd(self, value):
		self.__hinsyu_cd = value

	'''
	毛色コード
	'''
	__keiro_cd = bytes()

	@property
	def keiro_cd(self):
		return self.__keiro_cd

	@keiro_cd.setter
	def keiro_cd(self, value):
		self.__keiro_cd = value

	'''
	3代血統情報
	'''
	__ketto3_info = []

	@property
	def ketto3_info(self):
		return self.__ketto3_info

	@ketto3_info.setter
	def ketto3_info(self, value):
		self.__ketto3_info = value

	'''
	東西所属コード
	'''
	__tozai_cd = bytes()

	@property
	def tozai_cd(self):
		return self.__tozai_cd

	@tozai_cd.setter
	def tozai_cd(self, value):
		self.__tozai_cd = value

	'''
	調教師コード
	'''
	__chokyosi_cd = bytes()

	@property
	def chokyosi_cd(self):
		return self.__chokyosi_cd

	@chokyosi_cd.setter
	def chokyosi_cd(self, value):
		self.__chokyosi_cd = value

	'''
	調教師名略称
	'''
	__chokyosi_ryakusyo = bytes()

	@property
	def chokyosi_ryakusyo(self):
		return self.__chokyosi_ryakusyo

	@chokyosi_ryakusyo.setter
	def chokyosi_ryakusyo(self, value):
		self.__chokyosi_ryakusyo = value

	'''
	招待地域名
	'''
	__syotai = bytes()

	@property
	def syotai(self):
		return self.__syotai

	@syotai.setter
	def syotai(self, value):
		self.__syotai = value

	'''
	生産者コード
	'''
	__breeder_cd = bytes()

	@property
	def breeder_cd(self):
		return self.__breeder_cd

	@breeder_cd.setter
	def breeder_cd(self, value):
		self.__breeder_cd = value

	'''
	生産者名
	'''
	__breeder_name = bytes()

	@property
	def breeder_name(self):
		return self.__breeder_name

	@breeder_name.setter
	def breeder_name(self, value):
		self.__breeder_name = value

	'''
	産地名
	'''
	__sanchi_name = bytes()

	@property
	def sanchi_name(self):
		return self.__sanchi_name

	@sanchi_name.setter
	def sanchi_name(self, value):
		self.__sanchi_name = value

	'''
	馬主コード
	'''
	__banusi_cd = bytes()

	@property
	def banusi_cd(self):
		return self.__banusi_cd

	@banusi_cd.setter
	def banusi_cd(self, value):
		self.__banusi_cd = value

	'''
	馬主名
	'''
	__banusi_name = bytes()

	@property
	def banusi_name(self):
		return self.__banusi_name

	@banusi_name.setter
	def banusi_name(self, value):
		self.__banusi_name = value

	'''
	平地本賞金累計
	'''
	__ruikei_honsyo_heiti = bytes()

	@property
	def ruikei_honsyo_heiti(self):
		return self.__ruikei_honsyo_heiti

	@ruikei_honsyo_heiti.setter
	def ruikei_honsyo_heiti(self, value):
		self.__ruikei_honsyo_heiti = value

	'''
	障害本賞金累計
	'''
	__ruikei_honsyo_syogai = bytes()

	@property
	def ruikei_honsyo_syogai(self):
		return self.__ruikei_honsyo_syogai

	@ruikei_honsyo_syogai.setter
	def ruikei_honsyo_syogai(self, value):
		self.__ruikei_honsyo_syogai = value

	'''
	平地付加賞金累計
	'''
	__ruikei_fuka_heichi = bytes()

	@property
	def ruikei_fuka_heichi(self):
		return self.__ruikei_fuka_heichi

	@ruikei_fuka_heichi.setter
	def ruikei_fuka_heichi(self, value):
		self.__ruikei_fuka_heichi = value

	'''
	障害付加賞金累計
	'''
	__ruikei_fuka_syogai = bytes()

	@property
	def ruikei_fuka_syogai(self):
		return self.__ruikei_fuka_syogai

	@ruikei_fuka_syogai.setter
	def ruikei_fuka_syogai(self, value):
		self.__ruikei_fuka_syogai = value

	'''
	平地収得賞金累計
	'''
	__ruikei_syutoku_heichi = bytes()

	@property
	def ruikei_syutoku_heichi(self):
		return self.__ruikei_syutoku_heichi

	@ruikei_syutoku_heichi.setter
	def ruikei_syutoku_heichi(self, value):
		self.__ruikei_syutoku_heichi = value

	'''
	障害収得賞金累計
	'''
	__ruikei_syutoku_syogai = bytes()

	@property
	def ruikei_syutoku_syogai(self):
		return self.__ruikei_syutoku_syogai

	@ruikei_syutoku_syogai.setter
	def ruikei_syutoku_syogai(self, value):
		self.__ruikei_syutoku_syogai = value

	'''
	総合着回数
	'''
	__chaku_sogo = None

	@property
	def chaku_sogo(self):
		return self.__chaku_sogo

	@chaku_sogo.setter
	def chaku_sogo(self, value):
		self.__chaku_sogo = value

	'''
	中央合計着回数
	'''
	__chaku_chuo = None

	@property
	def chaku_chuo(self):
		return self.__chaku_chuo

	@chaku_chuo.setter
	def chaku_chuo(self, value):
		self.__chaku_chuo = value

	'''
	馬場別着回数
	'''
	__chaku_kaisu_ba = []

	@property
	def chaku_kaisu_ba(self):
		return self.__chaku_kaisu_ba

	@chaku_kaisu_ba.setter
	def chaku_kaisu_ba(self, value):
		self.__chaku_kaisu_ba = value

	'''
	馬場状態別着回数
	'''
	__chaku_kaisu_jyotai = []

	@property
	def chaku_kaisu_jyotai(self):
		return self.__chaku_kaisu_jyotai

	@chaku_kaisu_jyotai.setter
	def chaku_kaisu_jyotai(self, value):
		self.__chaku_kaisu_jyotai = value

	'''
	距離別着回数
	'''
	__chaku_kaisu_kyori = []

	@property
	def chaku_kaisu_kyori(self):
		return self.__chaku_kaisu_kyori

	@chaku_kaisu_kyori.setter
	def chaku_kaisu_kyori(self, value):
		self.__chaku_kaisu_kyori = value

	'''
	脚質傾向
	'''
	__kyakusitu = []

	@property
	def kyakusitu(self):
		return self.__kyakusitu

	@kyakusitu.setter
	def kyakusitu(self, value):
		self.__kyakusitu = value

	'''
	登録レース数
	'''
	__race_count = bytes()

	@property
	def race_count(self):
		return self.__race_count

	@race_count.setter
	def race_count(self, value):
		self.__race_count = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__ketto_num = source[11:21]
		self.__del_kubun = source[21:22]
		self.__reg_date = YMD(source[22:30])
		self.__del_date = YMD(source[30:38])
		self.__birth_date = YMD(source[38:46])
		self.__bamei = source[46:82]
		self.__bamei_kana = source[82:118]
		self.__bamei_eng = source[118:178]
		self.__zaikyu_flag = source[178:179]
		self.__reserved = source[179:198]
		self.__uma_kigo_cd = source[198:200]
		self.__sex_cd = source[200:201]
		self.__hinsyu_cd = source[201:202]
		self.__keiro_cd = source[202:204]

		self.__ketto3_info = []
		for i in range(14):
			self.__ketto3_info.append(KETTO3_INFO(source[204 + i * 44 :204 + i * 44 + 44]))

		self.__tozai_cd = source[820:821]
		self.__chokyosi_cd = source[821:826]
		self.__chokyosi_ryakusyo = source[826:834]
		self.__syotai = source[834:854]
		self.__breeder_cd = source[854:860]
		self.__breeder_name = source[860:930]
		self.__sanchi_name = source[930:950]
		self.__banusi_cd = source[950:956]
		self.__banusi_name = source[956:1020]
		self.__ruikei_honsyo_heiti = source[1020:1029]
		self.__ruikei_honsyo_syogai = source[1029:1038]
		self.__ruikei_fuka_heichi = source[1038:1047]
		self.__ruikei_fuka_syogai = source[1047:1056]
		self.__ruikei_syutoku_heichi = source[1056:1065]
		self.__ruikei_syutoku_syogai = source[1065:1074]
		self.__chaku_sogo = CHAKUKAISU3_INFO(source[1074:1092])
		self.__chaku_chuo = CHAKUKAISU3_INFO(source[1092:1110])

		self.__chaku_kaisu_ba = []
		for i in range(7):
			self.__chaku_kaisu_ba.append(CHAKUKAISU3_INFO(source[1110 + i * 18 :1110 + i * 18 + 18]))

		self.__chaku_kaisu_jyotai = []
		for i in range(12):
			self.__chaku_kaisu_jyotai.append(CHAKUKAISU3_INFO(source[1236 + i * 18 :1236 + i * 18 + 18]))

		self.__chaku_kaisu_kyori = []
		for i in range(6):
			self.__chaku_kaisu_kyori.append(CHAKUKAISU3_INFO(source[1452 + i * 18 :1452 + i * 18 + 18]))

		self.__kyakusitu = []
		for i in range(4):
			self.__kyakusitu.append(source[1560 + i * 3:1560 + i * 3 + 3])
		self.__race_count = source[1572:1575]
		self.__crlf = source[1575:1577]

class HATUKIJYO_INFO:

	'''
	年月日場回日R
	'''
	__hatukijyo_id = None

	@property
	def hatukijyo_id(self):
		return self.__hatukijyo_id

	@hatukijyo_id.setter
	def hatukijyo_id(self, value):
		self.__hatukijyo_id = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	確定着順
	'''
	__kakutei_jyuni = bytes()

	@property
	def kakutei_jyuni(self):
		return self.__kakutei_jyuni

	@kakutei_jyuni.setter
	def kakutei_jyuni(self, value):
		self.__kakutei_jyuni = value

	'''
	異常区分コード
	'''
	__ijyo_cd = bytes()

	@property
	def ijyo_cd(self):
		return self.__ijyo_cd

	@ijyo_cd.setter
	def ijyo_cd(self, value):
		self.__ijyo_cd = value

	def __init__(self, source : bytes) -> None:

		self.__hatukijyo_id = RACE_ID(source[0:16])
		self.__syusso_tosu = source[16:18]
		self.__ketto_num = source[18:28]
		self.__bamei = source[28:64]
		self.__kakutei_jyuni = source[64:66]
		self.__ijyo_cd = source[66:67]

class HATUSYORI_INFO:

	'''
	年月日場回日R
	'''
	__hatukijyo_id = None

	@property
	def hatukijyo_id(self):
		return self.__hatukijyo_id

	@hatukijyo_id.setter
	def hatukijyo_id(self, value):
		self.__hatukijyo_id = value

	'''
	出走頭数
	'''
	__syusso_tosu = bytes()

	@property
	def syusso_tosu(self):
		return self.__syusso_tosu

	@syusso_tosu.setter
	def syusso_tosu(self, value):
		self.__syusso_tosu = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	def __init__(self, source : bytes) -> None:

		self.__hatukijyo_id = RACE_ID(source[0:16])
		self.__syusso_tosu = source[16:18]
		self.__ketto_num = source[18:28]
		self.__bamei = source[28:64]

class JV_KS_KISYU:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	騎手コード
	'''
	__kisyu_cd = bytes()

	@property
	def kisyu_cd(self):
		return self.__kisyu_cd

	@kisyu_cd.setter
	def kisyu_cd(self, value):
		self.__kisyu_cd = value

	'''
	騎手抹消区分
	'''
	__del_kubun = bytes()

	@property
	def del_kubun(self):
		return self.__del_kubun

	@del_kubun.setter
	def del_kubun(self, value):
		self.__del_kubun = value

	'''
	騎手免許交付年月日
	'''
	__issue_date = None

	@property
	def issue_date(self):
		return self.__issue_date

	@issue_date.setter
	def issue_date(self, value):
		self.__issue_date = value

	'''
	騎手免許抹消年月日
	'''
	__del_date = None

	@property
	def del_date(self):
		return self.__del_date

	@del_date.setter
	def del_date(self, value):
		self.__del_date = value

	'''
	生年月日
	'''
	__birth_date = None

	@property
	def birth_date(self):
		return self.__birth_date

	@birth_date.setter
	def birth_date(self, value):
		self.__birth_date = value

	'''
	騎手名漢字
	'''
	__kisyu_name = bytes()

	@property
	def kisyu_name(self):
		return self.__kisyu_name

	@kisyu_name.setter
	def kisyu_name(self, value):
		self.__kisyu_name = value

	'''
	予備
	'''
	__reserved = bytes()

	@property
	def reserved(self):
		return self.__reserved

	@reserved.setter
	def reserved(self, value):
		self.__reserved = value

	'''
	騎手名半角カナ
	'''
	__kisyu_name_kana = bytes()

	@property
	def kisyu_name_kana(self):
		return self.__kisyu_name_kana

	@kisyu_name_kana.setter
	def kisyu_name_kana(self, value):
		self.__kisyu_name_kana = value

	'''
	騎手名略称
	'''
	__kisyu_ryakusyo = bytes()

	@property
	def kisyu_ryakusyo(self):
		return self.__kisyu_ryakusyo

	@kisyu_ryakusyo.setter
	def kisyu_ryakusyo(self, value):
		self.__kisyu_ryakusyo = value

	'''
	騎手名欧字
	'''
	__kisyu_name_eng = bytes()

	@property
	def kisyu_name_eng(self):
		return self.__kisyu_name_eng

	@kisyu_name_eng.setter
	def kisyu_name_eng(self, value):
		self.__kisyu_name_eng = value

	'''
	性別区分
	'''
	__sex_cd = bytes()

	@property
	def sex_cd(self):
		return self.__sex_cd

	@sex_cd.setter
	def sex_cd(self, value):
		self.__sex_cd = value

	'''
	騎乗資格コード
	'''
	__sikaku_cd = bytes()

	@property
	def sikaku_cd(self):
		return self.__sikaku_cd

	@sikaku_cd.setter
	def sikaku_cd(self, value):
		self.__sikaku_cd = value

	'''
	騎手見習コード
	'''
	__minarai_cd = bytes()

	@property
	def minarai_cd(self):
		return self.__minarai_cd

	@minarai_cd.setter
	def minarai_cd(self, value):
		self.__minarai_cd = value

	'''
	騎手東西所属コード
	'''
	__tozai_cd = bytes()

	@property
	def tozai_cd(self):
		return self.__tozai_cd

	@tozai_cd.setter
	def tozai_cd(self, value):
		self.__tozai_cd = value

	'''
	招待地域名
	'''
	__syotai = bytes()

	@property
	def syotai(self):
		return self.__syotai

	@syotai.setter
	def syotai(self, value):
		self.__syotai = value

	'''
	所属調教師コード
	'''
	__chokyosi_cd = bytes()

	@property
	def chokyosi_cd(self):
		return self.__chokyosi_cd

	@chokyosi_cd.setter
	def chokyosi_cd(self, value):
		self.__chokyosi_cd = value

	'''
	所属調教師名略称
	'''
	__chokyosi_ryakusyo = bytes()

	@property
	def chokyosi_ryakusyo(self):
		return self.__chokyosi_ryakusyo

	@chokyosi_ryakusyo.setter
	def chokyosi_ryakusyo(self, value):
		self.__chokyosi_ryakusyo = value

	'''
	初騎乗情報
	'''
	__hatu_ki_jyo = []

	@property
	def hatu_ki_jyo(self):
		return self.__hatu_ki_jyo

	@hatu_ki_jyo.setter
	def hatu_ki_jyo(self, value):
		self.__hatu_ki_jyo = value

	'''
	初勝利情報
	'''
	__hatu_syori = []

	@property
	def hatu_syori(self):
		return self.__hatu_syori

	@hatu_syori.setter
	def hatu_syori(self, value):
		self.__hatu_syori = value

	'''
	最近重賞勝利情報
	'''
	__saikin_jyusyo = []

	@property
	def saikin_jyusyo(self):
		return self.__saikin_jyusyo

	@saikin_jyusyo.setter
	def saikin_jyusyo(self, value):
		self.__saikin_jyusyo = value

	'''
	本年・前年・累計成績情報
	'''
	__hon_zen_ruikei = []

	@property
	def hon_zen_ruikei(self):
		return self.__hon_zen_ruikei

	@hon_zen_ruikei.setter
	def hon_zen_ruikei(self, value):
		self.__hon_zen_ruikei = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__kisyu_cd = source[11:16]
		self.__del_kubun = source[16:17]
		self.__issue_date = YMD(source[17:25])
		self.__del_date = YMD(source[25:33])
		self.__birth_date = YMD(source[33:41])
		self.__kisyu_name = source[41:75]
		self.__reserved = source[75:109]
		self.__kisyu_name_kana = source[109:139]
		self.__kisyu_ryakusyo = source[139:147]
		self.__kisyu_name_eng = source[147:227]
		self.__sex_cd = source[227:228]
		self.__sikaku_cd = source[228:229]
		self.__minarai_cd = source[229:230]
		self.__tozai_cd = source[230:231]
		self.__syotai = source[231:251]
		self.__chokyosi_cd = source[251:256]
		self.__chokyosi_ryakusyo = source[256:264]

		self.__hatu_ki_jyo = []
		for i in range(2):
			self.__hatu_ki_jyo.append(HATUKIJYO_INFO(source[264 + i * 67 :264 + i * 67 + 67]))

		self.__hatu_syori = []
		for i in range(2):
			self.__hatu_syori.append(HATUSYORI_INFO(source[398 + i * 64 :398 + i * 64 + 64]))

		self.__saikin_jyusyo = []
		for i in range(3):
			self.__saikin_jyusyo.append(SAIKIN_JYUSYO_INFO(source[526 + i * 163 :526 + i * 163 + 163]))

		self.__hon_zen_ruikei = []
		for i in range(3):
			self.__hon_zen_ruikei.append(HON_ZEN_RUIKEISEI_INFO(source[1015 + i * 1052 :1015 + i * 1052 + 1052]))

		self.__crlf = source[4171:4173]

class JV_CH_CHOKYOSI:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	調教師コード
	'''
	__chokyosi_cd = bytes()

	@property
	def chokyosi_cd(self):
		return self.__chokyosi_cd

	@chokyosi_cd.setter
	def chokyosi_cd(self, value):
		self.__chokyosi_cd = value

	'''
	調教師抹消区分
	'''
	__del_kubun = bytes()

	@property
	def del_kubun(self):
		return self.__del_kubun

	@del_kubun.setter
	def del_kubun(self, value):
		self.__del_kubun = value

	'''
	調教師免許交付年月日
	'''
	__issue_date = None

	@property
	def issue_date(self):
		return self.__issue_date

	@issue_date.setter
	def issue_date(self, value):
		self.__issue_date = value

	'''
	調教師免許抹消年月日
	'''
	__del_date = None

	@property
	def del_date(self):
		return self.__del_date

	@del_date.setter
	def del_date(self, value):
		self.__del_date = value

	'''
	生年月日
	'''
	__birth_date = None

	@property
	def birth_date(self):
		return self.__birth_date

	@birth_date.setter
	def birth_date(self, value):
		self.__birth_date = value

	'''
	調教師名漢字
	'''
	__chokyosi_name = bytes()

	@property
	def chokyosi_name(self):
		return self.__chokyosi_name

	@chokyosi_name.setter
	def chokyosi_name(self, value):
		self.__chokyosi_name = value

	'''
	調教師名半角カナ
	'''
	__chokyosi_name_kana = bytes()

	@property
	def chokyosi_name_kana(self):
		return self.__chokyosi_name_kana

	@chokyosi_name_kana.setter
	def chokyosi_name_kana(self, value):
		self.__chokyosi_name_kana = value

	'''
	調教師名略称
	'''
	__chokyosi_ryakusyo = bytes()

	@property
	def chokyosi_ryakusyo(self):
		return self.__chokyosi_ryakusyo

	@chokyosi_ryakusyo.setter
	def chokyosi_ryakusyo(self, value):
		self.__chokyosi_ryakusyo = value

	'''
	調教師名欧字
	'''
	__chokyosi_name_eng = bytes()

	@property
	def chokyosi_name_eng(self):
		return self.__chokyosi_name_eng

	@chokyosi_name_eng.setter
	def chokyosi_name_eng(self, value):
		self.__chokyosi_name_eng = value

	'''
	性別区分
	'''
	__sex_cd = bytes()

	@property
	def sex_cd(self):
		return self.__sex_cd

	@sex_cd.setter
	def sex_cd(self, value):
		self.__sex_cd = value

	'''
	調教師東西所属コード
	'''
	__tozai_cd = bytes()

	@property
	def tozai_cd(self):
		return self.__tozai_cd

	@tozai_cd.setter
	def tozai_cd(self, value):
		self.__tozai_cd = value

	'''
	招待地域名
	'''
	__syotai = bytes()

	@property
	def syotai(self):
		return self.__syotai

	@syotai.setter
	def syotai(self, value):
		self.__syotai = value

	'''
	最近重賞勝利情報
	'''
	__saikin_jyusyo = []

	@property
	def saikin_jyusyo(self):
		return self.__saikin_jyusyo

	@saikin_jyusyo.setter
	def saikin_jyusyo(self, value):
		self.__saikin_jyusyo = value

	'''
	本年・前年・累計成績情報
	'''
	__hon_zen_ruikei = []

	@property
	def hon_zen_ruikei(self):
		return self.__hon_zen_ruikei

	@hon_zen_ruikei.setter
	def hon_zen_ruikei(self, value):
		self.__hon_zen_ruikei = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__chokyosi_cd = source[11:16]
		self.__del_kubun = source[16:17]
		self.__issue_date = YMD(source[17:25])
		self.__del_date = YMD(source[25:33])
		self.__birth_date = YMD(source[33:41])
		self.__chokyosi_name = source[41:75]
		self.__chokyosi_name_kana = source[75:105]
		self.__chokyosi_ryakusyo = source[105:113]
		self.__chokyosi_name_eng = source[113:193]
		self.__sex_cd = source[193:194]
		self.__tozai_cd = source[194:195]
		self.__syotai = source[195:215]

		self.__saikin_jyusyo = []
		for i in range(3):
			self.__saikin_jyusyo.append(SAIKIN_JYUSYO_INFO(source[215 + i * 163 :215 + i * 163 + 163]))

		self.__hon_zen_ruikei = []
		for i in range(3):
			self.__hon_zen_ruikei.append(HON_ZEN_RUIKEISEI_INFO(source[704 + i * 1052 :704 + i * 1052 + 1052]))

		self.__crlf = source[3860:3862]

class JV_BR_BREEDER:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	生産者コード
	'''
	__breeder_cd = bytes()

	@property
	def breeder_cd(self):
		return self.__breeder_cd

	@breeder_cd.setter
	def breeder_cd(self, value):
		self.__breeder_cd = value

	'''
	生産者名(法人格有)
	'''
	__breeder_name__co = bytes()

	@property
	def breeder_name__co(self):
		return self.__breeder_name__co

	@breeder_name__co.setter
	def breeder_name__co(self, value):
		self.__breeder_name__co = value

	'''
	生産者名(法人格無)
	'''
	__breeder_name = bytes()

	@property
	def breeder_name(self):
		return self.__breeder_name

	@breeder_name.setter
	def breeder_name(self, value):
		self.__breeder_name = value

	'''
	生産者名半角カナ
	'''
	__breeder_name_kana = bytes()

	@property
	def breeder_name_kana(self):
		return self.__breeder_name_kana

	@breeder_name_kana.setter
	def breeder_name_kana(self, value):
		self.__breeder_name_kana = value

	'''
	生産者名欧字
	'''
	__breeder_name_eng = bytes()

	@property
	def breeder_name_eng(self):
		return self.__breeder_name_eng

	@breeder_name_eng.setter
	def breeder_name_eng(self, value):
		self.__breeder_name_eng = value

	'''
	生産者住所自治省名
	'''
	__address = bytes()

	@property
	def address(self):
		return self.__address

	@address.setter
	def address(self, value):
		self.__address = value

	'''
	本年・累計成績情報
	'''
	__hon_ruikei = []

	@property
	def hon_ruikei(self):
		return self.__hon_ruikei

	@hon_ruikei.setter
	def hon_ruikei(self, value):
		self.__hon_ruikei = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__breeder_cd = source[11:17]
		self.__breeder_name__co = source[17:87]
		self.__breeder_name = source[87:157]
		self.__breeder_name_kana = source[157:227]
		self.__breeder_name_eng = source[227:395]
		self.__address = source[395:415]

		self.__hon_ruikei = []
		for i in range(2):
			self.__hon_ruikei.append(SEI_RUIKEI_INFO(source[415 + i * 60 :415 + i * 60 + 60]))

		self.__crlf = source[535:537]

class JV_BN_BANUSI:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	馬主コード
	'''
	__banusi_cd = bytes()

	@property
	def banusi_cd(self):
		return self.__banusi_cd

	@banusi_cd.setter
	def banusi_cd(self, value):
		self.__banusi_cd = value

	'''
	馬主名(法人格有)
	'''
	__banusi_name__co = bytes()

	@property
	def banusi_name__co(self):
		return self.__banusi_name__co

	@banusi_name__co.setter
	def banusi_name__co(self, value):
		self.__banusi_name__co = value

	'''
	馬主名(法人格無)
	'''
	__banusi_name = bytes()

	@property
	def banusi_name(self):
		return self.__banusi_name

	@banusi_name.setter
	def banusi_name(self, value):
		self.__banusi_name = value

	'''
	馬主名半角カナ
	'''
	__banusi_name_kana = bytes()

	@property
	def banusi_name_kana(self):
		return self.__banusi_name_kana

	@banusi_name_kana.setter
	def banusi_name_kana(self, value):
		self.__banusi_name_kana = value

	'''
	馬主名欧字
	'''
	__banusi_name_eng = bytes()

	@property
	def banusi_name_eng(self):
		return self.__banusi_name_eng

	@banusi_name_eng.setter
	def banusi_name_eng(self, value):
		self.__banusi_name_eng = value

	'''
	服色標示
	'''
	__fukusyoku = bytes()

	@property
	def fukusyoku(self):
		return self.__fukusyoku

	@fukusyoku.setter
	def fukusyoku(self, value):
		self.__fukusyoku = value

	'''
	本年・累計成績情報
	'''
	__hon_ruikei = []

	@property
	def hon_ruikei(self):
		return self.__hon_ruikei

	@hon_ruikei.setter
	def hon_ruikei(self, value):
		self.__hon_ruikei = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__banusi_cd = source[11:17]
		self.__banusi_name__co = source[17:81]
		self.__banusi_name = source[81:145]
		self.__banusi_name_kana = source[145:195]
		self.__banusi_name_eng = source[195:295]
		self.__fukusyoku = source[295:355]

		self.__hon_ruikei = []
		for i in range(2):
			self.__hon_ruikei.append(SEI_RUIKEI_INFO(source[355 + i * 60 :355 + i * 60 + 60]))

		self.__crlf = source[475:477]

class JV_HN_HANSYOKU:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	繁殖登録番号
	'''
	__hansyoku_num = bytes()

	@property
	def hansyoku_num(self):
		return self.__hansyoku_num

	@hansyoku_num.setter
	def hansyoku_num(self, value):
		self.__hansyoku_num = value

	'''
	予備
	'''
	__reserved = bytes()

	@property
	def reserved(self):
		return self.__reserved

	@reserved.setter
	def reserved(self, value):
		self.__reserved = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	繁殖馬抹消区分(現在は予備として使用)
	'''
	__del_kubun = bytes()

	@property
	def del_kubun(self):
		return self.__del_kubun

	@del_kubun.setter
	def del_kubun(self, value):
		self.__del_kubun = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	馬名半角カナ
	'''
	__bamei_kana = bytes()

	@property
	def bamei_kana(self):
		return self.__bamei_kana

	@bamei_kana.setter
	def bamei_kana(self, value):
		self.__bamei_kana = value

	'''
	馬名欧字
	'''
	__bamei_eng = bytes()

	@property
	def bamei_eng(self):
		return self.__bamei_eng

	@bamei_eng.setter
	def bamei_eng(self, value):
		self.__bamei_eng = value

	'''
	生年
	'''
	__birth_year = bytes()

	@property
	def birth_year(self):
		return self.__birth_year

	@birth_year.setter
	def birth_year(self, value):
		self.__birth_year = value

	'''
	性別コード
	'''
	__sex_cd = bytes()

	@property
	def sex_cd(self):
		return self.__sex_cd

	@sex_cd.setter
	def sex_cd(self, value):
		self.__sex_cd = value

	'''
	品種コード
	'''
	__hinsyu_cd = bytes()

	@property
	def hinsyu_cd(self):
		return self.__hinsyu_cd

	@hinsyu_cd.setter
	def hinsyu_cd(self, value):
		self.__hinsyu_cd = value

	'''
	毛色コード
	'''
	__keiro_cd = bytes()

	@property
	def keiro_cd(self):
		return self.__keiro_cd

	@keiro_cd.setter
	def keiro_cd(self, value):
		self.__keiro_cd = value

	'''
	繁殖馬持込区分
	'''
	__hansyoku_mochi_kubun = bytes()

	@property
	def hansyoku_mochi_kubun(self):
		return self.__hansyoku_mochi_kubun

	@hansyoku_mochi_kubun.setter
	def hansyoku_mochi_kubun(self, value):
		self.__hansyoku_mochi_kubun = value

	'''
	輸入年
	'''
	__import_year = bytes()

	@property
	def import_year(self):
		return self.__import_year

	@import_year.setter
	def import_year(self, value):
		self.__import_year = value

	'''
	産地名
	'''
	__sanchi_name = bytes()

	@property
	def sanchi_name(self):
		return self.__sanchi_name

	@sanchi_name.setter
	def sanchi_name(self, value):
		self.__sanchi_name = value

	'''
	父馬繁殖登録番号
	'''
	__hansyoku_f_num = bytes()

	@property
	def hansyoku_f_num(self):
		return self.__hansyoku_f_num

	@hansyoku_f_num.setter
	def hansyoku_f_num(self, value):
		self.__hansyoku_f_num = value

	'''
	母馬繁殖登録番号
	'''
	__hansyoku_m_num = bytes()

	@property
	def hansyoku_m_num(self):
		return self.__hansyoku_m_num

	@hansyoku_m_num.setter
	def hansyoku_m_num(self, value):
		self.__hansyoku_m_num = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__hansyoku_num = source[11:19]
		self.__reserved = source[19:27]
		self.__ketto_num = source[27:37]
		self.__del_kubun = source[37:38]
		self.__bamei = source[38:74]
		self.__bamei_kana = source[74:114]
		self.__bamei_eng = source[114:194]
		self.__birth_year = source[194:198]
		self.__sex_cd = source[198:199]
		self.__hinsyu_cd = source[199:200]
		self.__keiro_cd = source[200:202]
		self.__hansyoku_mochi_kubun = source[202:203]
		self.__import_year = source[203:207]
		self.__sanchi_name = source[207:227]
		self.__hansyoku_f_num = source[227:235]
		self.__hansyoku_m_num = source[235:243]
		self.__crlf = source[243:245]

class JV_SK_SANKU:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	生年月日
	'''
	__birth_date = None

	@property
	def birth_date(self):
		return self.__birth_date

	@birth_date.setter
	def birth_date(self, value):
		self.__birth_date = value

	'''
	性別コード
	'''
	__sex_cd = bytes()

	@property
	def sex_cd(self):
		return self.__sex_cd

	@sex_cd.setter
	def sex_cd(self, value):
		self.__sex_cd = value

	'''
	品種コード
	'''
	__hinsyu_cd = bytes()

	@property
	def hinsyu_cd(self):
		return self.__hinsyu_cd

	@hinsyu_cd.setter
	def hinsyu_cd(self, value):
		self.__hinsyu_cd = value

	'''
	毛色コード
	'''
	__keiro_cd = bytes()

	@property
	def keiro_cd(self):
		return self.__keiro_cd

	@keiro_cd.setter
	def keiro_cd(self, value):
		self.__keiro_cd = value

	'''
	産駒持込区分
	'''
	__sanku_mochi_kubun = bytes()

	@property
	def sanku_mochi_kubun(self):
		return self.__sanku_mochi_kubun

	@sanku_mochi_kubun.setter
	def sanku_mochi_kubun(self, value):
		self.__sanku_mochi_kubun = value

	'''
	輸入年
	'''
	__import_year = bytes()

	@property
	def import_year(self):
		return self.__import_year

	@import_year.setter
	def import_year(self, value):
		self.__import_year = value

	'''
	生産者コード
	'''
	__breeder_cd = bytes()

	@property
	def breeder_cd(self):
		return self.__breeder_cd

	@breeder_cd.setter
	def breeder_cd(self, value):
		self.__breeder_cd = value

	'''
	産地名
	'''
	__sanchi_name = bytes()

	@property
	def sanchi_name(self):
		return self.__sanchi_name

	@sanchi_name.setter
	def sanchi_name(self, value):
		self.__sanchi_name = value

	'''
	3代血統
	'''
	__hansyoku_num = []

	@property
	def hansyoku_num(self):
		return self.__hansyoku_num

	@hansyoku_num.setter
	def hansyoku_num(self, value):
		self.__hansyoku_num = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__ketto_num = source[11:21]
		self.__birth_date = YMD(source[21:29])
		self.__sex_cd = source[29:30]
		self.__hinsyu_cd = source[30:31]
		self.__keiro_cd = source[31:33]
		self.__sanku_mochi_kubun = source[33:34]
		self.__import_year = source[34:38]
		self.__breeder_cd = source[38:44]
		self.__sanchi_name = source[44:64]
		self.__hansyoku_num = []
		for i in range(14):
			self.__hansyoku_num.append(source[64 + i * 8:64 + i * 8 + 8])
		self.__crlf = source[176:178]

class RECUMA_INFO:

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	馬記号コード
	'''
	__uma_kigo_cd = bytes()

	@property
	def uma_kigo_cd(self):
		return self.__uma_kigo_cd

	@uma_kigo_cd.setter
	def uma_kigo_cd(self, value):
		self.__uma_kigo_cd = value

	'''
	性別コード
	'''
	__sex_cd = bytes()

	@property
	def sex_cd(self):
		return self.__sex_cd

	@sex_cd.setter
	def sex_cd(self, value):
		self.__sex_cd = value

	'''
	調教師コード
	'''
	__chokyosi_cd = bytes()

	@property
	def chokyosi_cd(self):
		return self.__chokyosi_cd

	@chokyosi_cd.setter
	def chokyosi_cd(self, value):
		self.__chokyosi_cd = value

	'''
	調教師名
	'''
	__chokyosi_name = bytes()

	@property
	def chokyosi_name(self):
		return self.__chokyosi_name

	@chokyosi_name.setter
	def chokyosi_name(self, value):
		self.__chokyosi_name = value

	'''
	負担重量
	'''
	__futan = bytes()

	@property
	def futan(self):
		return self.__futan

	@futan.setter
	def futan(self, value):
		self.__futan = value

	'''
	騎手コード
	'''
	__kisyu_cd = bytes()

	@property
	def kisyu_cd(self):
		return self.__kisyu_cd

	@kisyu_cd.setter
	def kisyu_cd(self, value):
		self.__kisyu_cd = value

	'''
	騎手名
	'''
	__kisyu_name = bytes()

	@property
	def kisyu_name(self):
		return self.__kisyu_name

	@kisyu_name.setter
	def kisyu_name(self, value):
		self.__kisyu_name = value

	def __init__(self, source : bytes) -> None:

		self.__ketto_num = source[0:10]
		self.__bamei = source[10:46]
		self.__uma_kigo_cd = source[46:48]
		self.__sex_cd = source[48:49]
		self.__chokyosi_cd = source[49:54]
		self.__chokyosi_name = source[54:88]
		self.__futan = source[88:91]
		self.__kisyu_cd = source[91:96]
		self.__kisyu_name = source[96:130]

class JV_RC_RECORD:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	レコード識別区分
	'''
	__rec_info_kubun = bytes()

	@property
	def rec_info_kubun(self):
		return self.__rec_info_kubun

	@rec_info_kubun.setter
	def rec_info_kubun(self, value):
		self.__rec_info_kubun = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	特別競走番号
	'''
	__toku_num = bytes()

	@property
	def toku_num(self):
		return self.__toku_num

	@toku_num.setter
	def toku_num(self, value):
		self.__toku_num = value

	'''
	競走名本題
	'''
	__hondai = bytes()

	@property
	def hondai(self):
		return self.__hondai

	@hondai.setter
	def hondai(self, value):
		self.__hondai = value

	'''
	グレードコード
	'''
	__grade_cd = bytes()

	@property
	def grade_cd(self):
		return self.__grade_cd

	@grade_cd.setter
	def grade_cd(self, value):
		self.__grade_cd = value

	'''
	競走種別コード
	'''
	__syubetu_cd = bytes()

	@property
	def syubetu_cd(self):
		return self.__syubetu_cd

	@syubetu_cd.setter
	def syubetu_cd(self, value):
		self.__syubetu_cd = value

	'''
	距離
	'''
	__kyori = bytes()

	@property
	def kyori(self):
		return self.__kyori

	@kyori.setter
	def kyori(self, value):
		self.__kyori = value

	'''
	トラックコード
	'''
	__track_cd = bytes()

	@property
	def track_cd(self):
		return self.__track_cd

	@track_cd.setter
	def track_cd(self, value):
		self.__track_cd = value

	'''
	レコード区分
	'''
	__rec_kubun = bytes()

	@property
	def rec_kubun(self):
		return self.__rec_kubun

	@rec_kubun.setter
	def rec_kubun(self, value):
		self.__rec_kubun = value

	'''
	レコードタイム
	'''
	__rec_time = bytes()

	@property
	def rec_time(self):
		return self.__rec_time

	@rec_time.setter
	def rec_time(self, value):
		self.__rec_time = value

	'''
	天候・馬場状態
	'''
	__tenko_baba = None

	@property
	def tenko_baba(self):
		return self.__tenko_baba

	@tenko_baba.setter
	def tenko_baba(self, value):
		self.__tenko_baba = value

	'''
	レコード保持馬情報
	'''
	__rec_uma_info = []

	@property
	def rec_uma_info(self):
		return self.__rec_uma_info

	@rec_uma_info.setter
	def rec_uma_info(self, value):
		self.__rec_uma_info = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__rec_info_kubun = source[11:12]
		self.__id = RACE_ID(source[12:28])
		self.__toku_num = source[28:32]
		self.__hondai = source[32:92]
		self.__grade_cd = source[92:93]
		self.__syubetu_cd = source[93:95]
		self.__kyori = source[95:99]
		self.__track_cd = source[99:101]
		self.__rec_kubun = source[101:102]
		self.__rec_time = source[102:106]
		self.__tenko_baba = TENKO_BABA_INFO(source[106:109])

		self.__rec_uma_info = []
		for i in range(3):
			self.__rec_uma_info.append(RECUMA_INFO(source[109 + i * 130 :109 + i * 130 + 130]))

		self.__crlf = source[499:501]

class JV_HC_HANRO:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	トレセン区分
	'''
	__tresen_kubun = bytes()

	@property
	def tresen_kubun(self):
		return self.__tresen_kubun

	@tresen_kubun.setter
	def tresen_kubun(self, value):
		self.__tresen_kubun = value

	'''
	調教年月日
	'''
	__chokyo_date = None

	@property
	def chokyo_date(self):
		return self.__chokyo_date

	@chokyo_date.setter
	def chokyo_date(self, value):
		self.__chokyo_date = value

	'''
	調教時刻
	'''
	__chokyo_time = bytes()

	@property
	def chokyo_time(self):
		return self.__chokyo_time

	@chokyo_time.setter
	def chokyo_time(self, value):
		self.__chokyo_time = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	4ハロンタイム合計(800M-0M)
	'''
	__haron_time4 = bytes()

	@property
	def haron_time4(self):
		return self.__haron_time4

	@haron_time4.setter
	def haron_time4(self, value):
		self.__haron_time4 = value

	'''
	ラップタイム(800M-600M)
	'''
	__lap_time4 = bytes()

	@property
	def lap_time4(self):
		return self.__lap_time4

	@lap_time4.setter
	def lap_time4(self, value):
		self.__lap_time4 = value

	'''
	3ハロンタイム合計(600M-0M)
	'''
	__haron_time3 = bytes()

	@property
	def haron_time3(self):
		return self.__haron_time3

	@haron_time3.setter
	def haron_time3(self, value):
		self.__haron_time3 = value

	'''
	ラップタイム(600M-400M)
	'''
	__lap_time3 = bytes()

	@property
	def lap_time3(self):
		return self.__lap_time3

	@lap_time3.setter
	def lap_time3(self, value):
		self.__lap_time3 = value

	'''
	2ハロンタイム合計(400M-0M)
	'''
	__haron_time2 = bytes()

	@property
	def haron_time2(self):
		return self.__haron_time2

	@haron_time2.setter
	def haron_time2(self, value):
		self.__haron_time2 = value

	'''
	ラップタイム(400M-200M)
	'''
	__lap_time2 = bytes()

	@property
	def lap_time2(self):
		return self.__lap_time2

	@lap_time2.setter
	def lap_time2(self, value):
		self.__lap_time2 = value

	'''
	ラップタイム(200M-0M)
	'''
	__lap_time1 = bytes()

	@property
	def lap_time1(self):
		return self.__lap_time1

	@lap_time1.setter
	def lap_time1(self, value):
		self.__lap_time1 = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__tresen_kubun = source[11:12]
		self.__chokyo_date = YMD(source[12:20])
		self.__chokyo_time = source[20:24]
		self.__ketto_num = source[24:34]
		self.__haron_time4 = source[34:38]
		self.__lap_time4 = source[38:41]
		self.__haron_time3 = source[41:45]
		self.__lap_time3 = source[45:48]
		self.__haron_time2 = source[48:52]
		self.__lap_time2 = source[52:55]
		self.__lap_time1 = source[55:58]
		self.__crlf = source[58:60]

class BATAIJYU_INFO:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	馬体重
	'''
	__ba_taijyu = bytes()

	@property
	def ba_taijyu(self):
		return self.__ba_taijyu

	@ba_taijyu.setter
	def ba_taijyu(self, value):
		self.__ba_taijyu = value

	'''
	増減符号
	'''
	__zogen_fugo = bytes()

	@property
	def zogen_fugo(self):
		return self.__zogen_fugo

	@zogen_fugo.setter
	def zogen_fugo(self, value):
		self.__zogen_fugo = value

	'''
	増減差
	'''
	__zogen_sa = bytes()

	@property
	def zogen_sa(self):
		return self.__zogen_sa

	@zogen_sa.setter
	def zogen_sa(self, value):
		self.__zogen_sa = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:2]
		self.__bamei = source[2:38]
		self.__ba_taijyu = source[38:41]
		self.__zogen_fugo = source[41:42]
		self.__zogen_sa = source[42:45]

class JV_WH_BATAIJYU:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	馬体重情報
	'''
	__bataijyu_info = []

	@property
	def bataijyu_info(self):
		return self.__bataijyu_info

	@bataijyu_info.setter
	def bataijyu_info(self, value):
		self.__bataijyu_info = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])

		self.__bataijyu_info = []
		for i in range(18):
			self.__bataijyu_info.append(BATAIJYU_INFO(source[35 + i * 45 :35 + i * 45 + 45]))

		self.__crlf = source[845:847]

class JV_WE_WEATHER:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報２
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	変更識別
	'''
	__henko_i_d = bytes()

	@property
	def henko_i_d(self):
		return self.__henko_i_d

	@henko_i_d.setter
	def henko_i_d(self, value):
		self.__henko_i_d = value

	'''
	現在状態情報
	'''
	__tenko_baba = None

	@property
	def tenko_baba(self):
		return self.__tenko_baba

	@tenko_baba.setter
	def tenko_baba(self, value):
		self.__tenko_baba = value

	'''
	変更前状態情報
	'''
	__tenko_baba_before = None

	@property
	def tenko_baba_before(self):
		return self.__tenko_baba_before

	@tenko_baba_before.setter
	def tenko_baba_before(self, value):
		self.__tenko_baba_before = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID2(source[11:25])
		self.__happyo_time = MDHM(source[25:33])
		self.__henko_i_d = source[33:34]
		self.__tenko_baba = TENKO_BABA_INFO(source[34:37])
		self.__tenko_baba_before = TENKO_BABA_INFO(source[37:40])
		self.__crlf = source[40:42]

class JV_AV_INFO:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	事由区分
	'''
	__jiyu_kubun = bytes()

	@property
	def jiyu_kubun(self):
		return self.__jiyu_kubun

	@jiyu_kubun.setter
	def jiyu_kubun(self, value):
		self.__jiyu_kubun = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__umaban = source[35:37]
		self.__bamei = source[37:73]
		self.__jiyu_kubun = source[73:76]
		self.__crlf = source[76:78]

class JC_INFO:

	'''
	負担重量
	'''
	__futan = bytes()

	@property
	def futan(self):
		return self.__futan

	@futan.setter
	def futan(self, value):
		self.__futan = value

	'''
	騎手コード
	'''
	__kisyu_cd = bytes()

	@property
	def kisyu_cd(self):
		return self.__kisyu_cd

	@kisyu_cd.setter
	def kisyu_cd(self, value):
		self.__kisyu_cd = value

	'''
	騎手名
	'''
	__kisyu_name = bytes()

	@property
	def kisyu_name(self):
		return self.__kisyu_name

	@kisyu_name.setter
	def kisyu_name(self, value):
		self.__kisyu_name = value

	'''
	騎手見習コード
	'''
	__minarai_cd = bytes()

	@property
	def minarai_cd(self):
		return self.__minarai_cd

	@minarai_cd.setter
	def minarai_cd(self, value):
		self.__minarai_cd = value

	def __init__(self, source : bytes) -> None:

		self.__futan = source[0:3]
		self.__kisyu_cd = source[3:8]
		self.__kisyu_name = source[8:42]
		self.__minarai_cd = source[42:43]

class JV_JC_INFO:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	変更後情報
	'''
	__j_c_info_after = None

	@property
	def j_c_info_after(self):
		return self.__j_c_info_after

	@j_c_info_after.setter
	def j_c_info_after(self, value):
		self.__j_c_info_after = value

	'''
	変更前情報
	'''
	__j_c_info_before = None

	@property
	def j_c_info_before(self):
		return self.__j_c_info_before

	@j_c_info_before.setter
	def j_c_info_before(self, value):
		self.__j_c_info_before = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__umaban = source[35:37]
		self.__bamei = source[37:73]
		self.__j_c_info_after = JC_INFO(source[73:116])
		self.__j_c_info_before = JC_INFO(source[116:159])
		self.__crlf = source[159:161]

class TC_INFO:

	'''
	時
	'''
	__ji = bytes()

	@property
	def ji(self):
		return self.__ji

	@ji.setter
	def ji(self, value):
		self.__ji = value

	'''
	分
	'''
	__fun = bytes()

	@property
	def fun(self):
		return self.__fun

	@fun.setter
	def fun(self, value):
		self.__fun = value

	def __init__(self, source : bytes) -> None:

		self.__ji = source[0:2]
		self.__fun = source[2:4]

class JV_TC_INFO:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	変更後情報
	'''
	__t_c_info_after = None

	@property
	def t_c_info_after(self):
		return self.__t_c_info_after

	@t_c_info_after.setter
	def t_c_info_after(self, value):
		self.__t_c_info_after = value

	'''
	変更前情報
	'''
	__t_c_info_before = None

	@property
	def t_c_info_before(self):
		return self.__t_c_info_before

	@t_c_info_before.setter
	def t_c_info_before(self, value):
		self.__t_c_info_before = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__t_c_info_after = TC_INFO(source[35:39])
		self.__t_c_info_before = TC_INFO(source[39:43])
		self.__crlf = source[43:45]

class CC_INFO:

	'''
	距離
	'''
	__kyori = bytes()

	@property
	def kyori(self):
		return self.__kyori

	@kyori.setter
	def kyori(self, value):
		self.__kyori = value

	'''
	トラックコード
	'''
	__truck_cd = bytes()

	@property
	def truck_cd(self):
		return self.__truck_cd

	@truck_cd.setter
	def truck_cd(self, value):
		self.__truck_cd = value

	def __init__(self, source : bytes) -> None:

		self.__kyori = source[0:4]
		self.__truck_cd = source[4:6]

class JV_CC_INFO:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	発表月日時分
	'''
	__happyo_time = None

	@property
	def happyo_time(self):
		return self.__happyo_time

	@happyo_time.setter
	def happyo_time(self, value):
		self.__happyo_time = value

	'''
	変更後情報
	'''
	__c_c_info_after = None

	@property
	def c_c_info_after(self):
		return self.__c_c_info_after

	@c_c_info_after.setter
	def c_c_info_after(self, value):
		self.__c_c_info_after = value

	'''
	変更前情報
	'''
	__c_c_info_before = None

	@property
	def c_c_info_before(self):
		return self.__c_c_info_before

	@c_c_info_before.setter
	def c_c_info_before(self, value):
		self.__c_c_info_before = value

	'''
	
	'''
	__jiyu_cd = bytes()

	@property
	def jiyu_cd(self):
		return self.__jiyu_cd

	@jiyu_cd.setter
	def jiyu_cd(self, value):
		self.__jiyu_cd = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__happyo_time = MDHM(source[27:35])
		self.__c_c_info_after = CC_INFO(source[35:41])
		self.__c_c_info_before = CC_INFO(source[41:47])
		self.__jiyu_cd = source[47:48]
		self.__crlf = source[48:50]

class DM_INFO:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	予想走破タイム
	'''
	__d_m_time = bytes()

	@property
	def d_m_time(self):
		return self.__d_m_time

	@d_m_time.setter
	def d_m_time(self, value):
		self.__d_m_time = value

	'''
	予想誤差(信頼度)＋
	'''
	__d_m_gosa_p = bytes()

	@property
	def d_m_gosa_p(self):
		return self.__d_m_gosa_p

	@d_m_gosa_p.setter
	def d_m_gosa_p(self, value):
		self.__d_m_gosa_p = value

	'''
	予想誤差(信頼度)－
	'''
	__d_m_gosa_m = bytes()

	@property
	def d_m_gosa_m(self):
		return self.__d_m_gosa_m

	@d_m_gosa_m.setter
	def d_m_gosa_m(self, value):
		self.__d_m_gosa_m = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:2]
		self.__d_m_time = source[2:7]
		self.__d_m_gosa_p = source[7:11]
		self.__d_m_gosa_m = source[11:15]

class JV_DM_INFO:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	データ作成時分
	'''
	__make_h_m = None

	@property
	def make_h_m(self):
		return self.__make_h_m

	@make_h_m.setter
	def make_h_m(self, value):
		self.__make_h_m = value

	'''
	マイニング予想
	'''
	__d_m_info = []

	@property
	def d_m_info(self):
		return self.__d_m_info

	@d_m_info.setter
	def d_m_info(self, value):
		self.__d_m_info = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__make_h_m = HM(source[27:31])

		self.__d_m_info = []
		for i in range(18):
			self.__d_m_info.append(DM_INFO(source[31 + i * 15 :31 + i * 15 + 15]))

		self.__crlf = source[301:303]

class JYUSYO_INFO:

	'''
	特別競走番号
	'''
	__toku_num = bytes()

	@property
	def toku_num(self):
		return self.__toku_num

	@toku_num.setter
	def toku_num(self, value):
		self.__toku_num = value

	'''
	競走名本題
	'''
	__hondai = bytes()

	@property
	def hondai(self):
		return self.__hondai

	@hondai.setter
	def hondai(self, value):
		self.__hondai = value

	'''
	競走名略称10字
	'''
	__ryakusyo10 = bytes()

	@property
	def ryakusyo10(self):
		return self.__ryakusyo10

	@ryakusyo10.setter
	def ryakusyo10(self, value):
		self.__ryakusyo10 = value

	'''
	競走名略称6字
	'''
	__ryakusyo6 = bytes()

	@property
	def ryakusyo6(self):
		return self.__ryakusyo6

	@ryakusyo6.setter
	def ryakusyo6(self, value):
		self.__ryakusyo6 = value

	'''
	競走名略称3字
	'''
	__ryakusyo3 = bytes()

	@property
	def ryakusyo3(self):
		return self.__ryakusyo3

	@ryakusyo3.setter
	def ryakusyo3(self, value):
		self.__ryakusyo3 = value

	'''
	重賞回次[第N回]
	'''
	__nkai = bytes()

	@property
	def nkai(self):
		return self.__nkai

	@nkai.setter
	def nkai(self, value):
		self.__nkai = value

	'''
	グレードコード
	'''
	__grade_cd = bytes()

	@property
	def grade_cd(self):
		return self.__grade_cd

	@grade_cd.setter
	def grade_cd(self, value):
		self.__grade_cd = value

	'''
	競走種別コード
	'''
	__syubetu_cd = bytes()

	@property
	def syubetu_cd(self):
		return self.__syubetu_cd

	@syubetu_cd.setter
	def syubetu_cd(self, value):
		self.__syubetu_cd = value

	'''
	競走記号コード
	'''
	__kigo_cd = bytes()

	@property
	def kigo_cd(self):
		return self.__kigo_cd

	@kigo_cd.setter
	def kigo_cd(self, value):
		self.__kigo_cd = value

	'''
	重量種別コード
	'''
	__jyuryo_cd = bytes()

	@property
	def jyuryo_cd(self):
		return self.__jyuryo_cd

	@jyuryo_cd.setter
	def jyuryo_cd(self, value):
		self.__jyuryo_cd = value

	'''
	距離
	'''
	__kyori = bytes()

	@property
	def kyori(self):
		return self.__kyori

	@kyori.setter
	def kyori(self, value):
		self.__kyori = value

	'''
	トラックコード
	'''
	__track_cd = bytes()

	@property
	def track_cd(self):
		return self.__track_cd

	@track_cd.setter
	def track_cd(self, value):
		self.__track_cd = value

	def __init__(self, source : bytes) -> None:

		self.__toku_num = source[0:4]
		self.__hondai = source[4:64]
		self.__ryakusyo10 = source[64:84]
		self.__ryakusyo6 = source[84:96]
		self.__ryakusyo3 = source[96:102]
		self.__nkai = source[102:105]
		self.__grade_cd = source[105:106]
		self.__syubetu_cd = source[106:108]
		self.__kigo_cd = source[108:111]
		self.__jyuryo_cd = source[111:112]
		self.__kyori = source[112:116]
		self.__track_cd = source[116:118]

class JV_YS_SCHEDULE:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報２
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	曜日コード
	'''
	__youbi_cd = bytes()

	@property
	def youbi_cd(self):
		return self.__youbi_cd

	@youbi_cd.setter
	def youbi_cd(self, value):
		self.__youbi_cd = value

	'''
	重賞案内
	'''
	__jyusyo_info = []

	@property
	def jyusyo_info(self):
		return self.__jyusyo_info

	@jyusyo_info.setter
	def jyusyo_info(self, value):
		self.__jyusyo_info = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID2(source[11:25])
		self.__youbi_cd = source[25:26]

		self.__jyusyo_info = []
		for i in range(3):
			self.__jyusyo_info.append(JYUSYO_INFO(source[26 + i * 118 :26 + i * 118 + 118]))

		self.__crlf = source[380:382]

class JV_HS_SALE:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	父馬繁殖登録番号
	'''
	__hansyoku_f_num = bytes()

	@property
	def hansyoku_f_num(self):
		return self.__hansyoku_f_num

	@hansyoku_f_num.setter
	def hansyoku_f_num(self, value):
		self.__hansyoku_f_num = value

	'''
	母馬繁殖登録番号
	'''
	__hansyoku_m_num = bytes()

	@property
	def hansyoku_m_num(self):
		return self.__hansyoku_m_num

	@hansyoku_m_num.setter
	def hansyoku_m_num(self, value):
		self.__hansyoku_m_num = value

	'''
	生年
	'''
	__birth_year = bytes()

	@property
	def birth_year(self):
		return self.__birth_year

	@birth_year.setter
	def birth_year(self, value):
		self.__birth_year = value

	'''
	主催者・市場コード
	'''
	__sale_cd = bytes()

	@property
	def sale_cd(self):
		return self.__sale_cd

	@sale_cd.setter
	def sale_cd(self, value):
		self.__sale_cd = value

	'''
	主催者名称
	'''
	__sale_host_name = bytes()

	@property
	def sale_host_name(self):
		return self.__sale_host_name

	@sale_host_name.setter
	def sale_host_name(self, value):
		self.__sale_host_name = value

	'''
	市場の名称
	'''
	__sale_name = bytes()

	@property
	def sale_name(self):
		return self.__sale_name

	@sale_name.setter
	def sale_name(self, value):
		self.__sale_name = value

	'''
	市場の開催期間(開始日)
	'''
	__from_date = None

	@property
	def from_date(self):
		return self.__from_date

	@from_date.setter
	def from_date(self, value):
		self.__from_date = value

	'''
	市場の開催期間(終了日)
	'''
	__to_date = None

	@property
	def to_date(self):
		return self.__to_date

	@to_date.setter
	def to_date(self, value):
		self.__to_date = value

	'''
	取引時の競走馬の年齢
	'''
	__barei = bytes()

	@property
	def barei(self):
		return self.__barei

	@barei.setter
	def barei(self, value):
		self.__barei = value

	'''
	取引価格
	'''
	__price = bytes()

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, value):
		self.__price = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__ketto_num = source[11:21]
		self.__hansyoku_f_num = source[21:29]
		self.__hansyoku_m_num = source[29:37]
		self.__birth_year = source[37:41]
		self.__sale_cd = source[41:47]
		self.__sale_host_name = source[47:87]
		self.__sale_name = source[87:167]
		self.__from_date = YMD(source[167:175])
		self.__to_date = YMD(source[175:183])
		self.__barei = source[183:184]
		self.__price = source[184:194]
		self.__crlf = source[194:196]

class JV_HY_BAMEIORIGIN:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	馬名の意味由来
	'''
	__origin = bytes()

	@property
	def origin(self):
		return self.__origin

	@origin.setter
	def origin(self, value):
		self.__origin = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__ketto_num = source[11:21]
		self.__bamei = source[21:57]
		self.__origin = source[57:121]
		self.__crlf = source[121:123]

class JV_CK_UMA:

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	平地本賞金累計
	'''
	__ruikei_honsyo_heiti = bytes()

	@property
	def ruikei_honsyo_heiti(self):
		return self.__ruikei_honsyo_heiti

	@ruikei_honsyo_heiti.setter
	def ruikei_honsyo_heiti(self, value):
		self.__ruikei_honsyo_heiti = value

	'''
	障害本賞金累計
	'''
	__ruikei_honsyo_syogai = bytes()

	@property
	def ruikei_honsyo_syogai(self):
		return self.__ruikei_honsyo_syogai

	@ruikei_honsyo_syogai.setter
	def ruikei_honsyo_syogai(self, value):
		self.__ruikei_honsyo_syogai = value

	'''
	平地付加賞金累計
	'''
	__ruikei_fuka_heichi = bytes()

	@property
	def ruikei_fuka_heichi(self):
		return self.__ruikei_fuka_heichi

	@ruikei_fuka_heichi.setter
	def ruikei_fuka_heichi(self, value):
		self.__ruikei_fuka_heichi = value

	'''
	障害付加賞金累計
	'''
	__ruikei_fuka_syogai = bytes()

	@property
	def ruikei_fuka_syogai(self):
		return self.__ruikei_fuka_syogai

	@ruikei_fuka_syogai.setter
	def ruikei_fuka_syogai(self, value):
		self.__ruikei_fuka_syogai = value

	'''
	平地収得賞金累計
	'''
	__ruikei_syutoku_heichi = bytes()

	@property
	def ruikei_syutoku_heichi(self):
		return self.__ruikei_syutoku_heichi

	@ruikei_syutoku_heichi.setter
	def ruikei_syutoku_heichi(self, value):
		self.__ruikei_syutoku_heichi = value

	'''
	障害収得賞金累計
	'''
	__ruikei_syutoku_syogai = bytes()

	@property
	def ruikei_syutoku_syogai(self):
		return self.__ruikei_syutoku_syogai

	@ruikei_syutoku_syogai.setter
	def ruikei_syutoku_syogai(self, value):
		self.__ruikei_syutoku_syogai = value

	'''
	総合着回数
	'''
	__chaku_sogo = None

	@property
	def chaku_sogo(self):
		return self.__chaku_sogo

	@chaku_sogo.setter
	def chaku_sogo(self, value):
		self.__chaku_sogo = value

	'''
	中央合計着回数
	'''
	__chaku_chuo = None

	@property
	def chaku_chuo(self):
		return self.__chaku_chuo

	@chaku_chuo.setter
	def chaku_chuo(self, value):
		self.__chaku_chuo = value

	'''
	馬場別着回数
	'''
	__chaku_kaisu_ba = []

	@property
	def chaku_kaisu_ba(self):
		return self.__chaku_kaisu_ba

	@chaku_kaisu_ba.setter
	def chaku_kaisu_ba(self, value):
		self.__chaku_kaisu_ba = value

	'''
	馬場状態別着回数
	'''
	__chaku_kaisu_jyotai = []

	@property
	def chaku_kaisu_jyotai(self):
		return self.__chaku_kaisu_jyotai

	@chaku_kaisu_jyotai.setter
	def chaku_kaisu_jyotai(self, value):
		self.__chaku_kaisu_jyotai = value

	'''
	芝距離別着回数
	'''
	__chaku_kaisu_siba_kyori = []

	@property
	def chaku_kaisu_siba_kyori(self):
		return self.__chaku_kaisu_siba_kyori

	@chaku_kaisu_siba_kyori.setter
	def chaku_kaisu_siba_kyori(self, value):
		self.__chaku_kaisu_siba_kyori = value

	'''
	ダート距離別着回数
	'''
	__chaku_kaisu_dirt_kyori = []

	@property
	def chaku_kaisu_dirt_kyori(self):
		return self.__chaku_kaisu_dirt_kyori

	@chaku_kaisu_dirt_kyori.setter
	def chaku_kaisu_dirt_kyori(self, value):
		self.__chaku_kaisu_dirt_kyori = value

	'''
	競馬場別芝着回数
	'''
	__chaku_kaisu_jyo_siba = []

	@property
	def chaku_kaisu_jyo_siba(self):
		return self.__chaku_kaisu_jyo_siba

	@chaku_kaisu_jyo_siba.setter
	def chaku_kaisu_jyo_siba(self, value):
		self.__chaku_kaisu_jyo_siba = value

	'''
	競馬場別ダート着回数
	'''
	__chaku_kaisu_jyo_dirt = []

	@property
	def chaku_kaisu_jyo_dirt(self):
		return self.__chaku_kaisu_jyo_dirt

	@chaku_kaisu_jyo_dirt.setter
	def chaku_kaisu_jyo_dirt(self, value):
		self.__chaku_kaisu_jyo_dirt = value

	'''
	競馬場別障害着回数
	'''
	__chaku_kaisu_jyo_syogai = []

	@property
	def chaku_kaisu_jyo_syogai(self):
		return self.__chaku_kaisu_jyo_syogai

	@chaku_kaisu_jyo_syogai.setter
	def chaku_kaisu_jyo_syogai(self, value):
		self.__chaku_kaisu_jyo_syogai = value

	'''
	脚質傾向
	'''
	__kyakusitu = []

	@property
	def kyakusitu(self):
		return self.__kyakusitu

	@kyakusitu.setter
	def kyakusitu(self, value):
		self.__kyakusitu = value

	'''
	登録レース数
	'''
	__race_count = bytes()

	@property
	def race_count(self):
		return self.__race_count

	@race_count.setter
	def race_count(self, value):
		self.__race_count = value

	def __init__(self, source : bytes) -> None:

		self.__ketto_num = source[0:10]
		self.__bamei = source[10:46]
		self.__ruikei_honsyo_heiti = source[46:55]
		self.__ruikei_honsyo_syogai = source[55:64]
		self.__ruikei_fuka_heichi = source[64:73]
		self.__ruikei_fuka_syogai = source[73:82]
		self.__ruikei_syutoku_heichi = source[82:91]
		self.__ruikei_syutoku_syogai = source[91:100]
		self.__chaku_sogo = CHAKUKAISU3_INFO(source[100:118])
		self.__chaku_chuo = CHAKUKAISU3_INFO(source[118:136])

		self.__chaku_kaisu_ba = []
		for i in range(7):
			self.__chaku_kaisu_ba.append(CHAKUKAISU3_INFO(source[136 + i * 18 :136 + i * 18 + 18]))

		self.__chaku_kaisu_jyotai = []
		for i in range(12):
			self.__chaku_kaisu_jyotai.append(CHAKUKAISU3_INFO(source[262 + i * 18 :262 + i * 18 + 18]))

		self.__chaku_kaisu_siba_kyori = []
		for i in range(9):
			self.__chaku_kaisu_siba_kyori.append(CHAKUKAISU3_INFO(source[478 + i * 18 :478 + i * 18 + 18]))

		self.__chaku_kaisu_dirt_kyori = []
		for i in range(9):
			self.__chaku_kaisu_dirt_kyori.append(CHAKUKAISU3_INFO(source[640 + i * 18 :640 + i * 18 + 18]))

		self.__chaku_kaisu_jyo_siba = []
		for i in range(10):
			self.__chaku_kaisu_jyo_siba.append(CHAKUKAISU3_INFO(source[802 + i * 18 :802 + i * 18 + 18]))

		self.__chaku_kaisu_jyo_dirt = []
		for i in range(10):
			self.__chaku_kaisu_jyo_dirt.append(CHAKUKAISU3_INFO(source[982 + i * 18 :982 + i * 18 + 18]))

		self.__chaku_kaisu_jyo_syogai = []
		for i in range(10):
			self.__chaku_kaisu_jyo_syogai.append(CHAKUKAISU3_INFO(source[1162 + i * 18 :1162 + i * 18 + 18]))

		self.__kyakusitu = []
		for i in range(4):
			self.__kyakusitu.append(source[1342 + i * 3:1342 + i * 3 + 3])
		self.__race_count = source[1354:1357]

class JV_CK_HON_RUIKEISEI_INFO:

	'''
	設定年
	'''
	__set_year = bytes()

	@property
	def set_year(self):
		return self.__set_year

	@set_year.setter
	def set_year(self, value):
		self.__set_year = value

	'''
	平地本賞金合計
	'''
	__hon_syokin_heichi = bytes()

	@property
	def hon_syokin_heichi(self):
		return self.__hon_syokin_heichi

	@hon_syokin_heichi.setter
	def hon_syokin_heichi(self, value):
		self.__hon_syokin_heichi = value

	'''
	障害本賞金合計
	'''
	__hon_syokin_syogai = bytes()

	@property
	def hon_syokin_syogai(self):
		return self.__hon_syokin_syogai

	@hon_syokin_syogai.setter
	def hon_syokin_syogai(self, value):
		self.__hon_syokin_syogai = value

	'''
	平地付加賞金合計
	'''
	__fuka_syokin_heichi = bytes()

	@property
	def fuka_syokin_heichi(self):
		return self.__fuka_syokin_heichi

	@fuka_syokin_heichi.setter
	def fuka_syokin_heichi(self, value):
		self.__fuka_syokin_heichi = value

	'''
	障害付加賞金合計
	'''
	__fuka_syokin_syogai = bytes()

	@property
	def fuka_syokin_syogai(self):
		return self.__fuka_syokin_syogai

	@fuka_syokin_syogai.setter
	def fuka_syokin_syogai(self, value):
		self.__fuka_syokin_syogai = value

	'''
	芝着回数
	'''
	__chaku_kaisu_siba = None

	@property
	def chaku_kaisu_siba(self):
		return self.__chaku_kaisu_siba

	@chaku_kaisu_siba.setter
	def chaku_kaisu_siba(self, value):
		self.__chaku_kaisu_siba = value

	'''
	ダート着回数
	'''
	__chaku_kaisu_dirt = None

	@property
	def chaku_kaisu_dirt(self):
		return self.__chaku_kaisu_dirt

	@chaku_kaisu_dirt.setter
	def chaku_kaisu_dirt(self, value):
		self.__chaku_kaisu_dirt = value

	'''
	障害着回数
	'''
	__chaku_kaisu_syogai = None

	@property
	def chaku_kaisu_syogai(self):
		return self.__chaku_kaisu_syogai

	@chaku_kaisu_syogai.setter
	def chaku_kaisu_syogai(self, value):
		self.__chaku_kaisu_syogai = value

	'''
	芝距離別着回数
	'''
	__chaku_kaisu_siba_kyori = []

	@property
	def chaku_kaisu_siba_kyori(self):
		return self.__chaku_kaisu_siba_kyori

	@chaku_kaisu_siba_kyori.setter
	def chaku_kaisu_siba_kyori(self, value):
		self.__chaku_kaisu_siba_kyori = value

	'''
	ダート距離別着回数
	'''
	__chaku_kaisu_dirt_kyori = []

	@property
	def chaku_kaisu_dirt_kyori(self):
		return self.__chaku_kaisu_dirt_kyori

	@chaku_kaisu_dirt_kyori.setter
	def chaku_kaisu_dirt_kyori(self, value):
		self.__chaku_kaisu_dirt_kyori = value

	'''
	競馬場別芝着回数
	'''
	__chaku_kaisu_jyo_siba = []

	@property
	def chaku_kaisu_jyo_siba(self):
		return self.__chaku_kaisu_jyo_siba

	@chaku_kaisu_jyo_siba.setter
	def chaku_kaisu_jyo_siba(self, value):
		self.__chaku_kaisu_jyo_siba = value

	'''
	競馬場別ダート着回数
	'''
	__chaku_kaisu_jyo_dirt = []

	@property
	def chaku_kaisu_jyo_dirt(self):
		return self.__chaku_kaisu_jyo_dirt

	@chaku_kaisu_jyo_dirt.setter
	def chaku_kaisu_jyo_dirt(self, value):
		self.__chaku_kaisu_jyo_dirt = value

	'''
	競馬場別障害着回数
	'''
	__chaku_kaisu_jyo_syogai = []

	@property
	def chaku_kaisu_jyo_syogai(self):
		return self.__chaku_kaisu_jyo_syogai

	@chaku_kaisu_jyo_syogai.setter
	def chaku_kaisu_jyo_syogai(self, value):
		self.__chaku_kaisu_jyo_syogai = value

	def __init__(self, source : bytes) -> None:

		self.__set_year = source[0:4]
		self.__hon_syokin_heichi = source[4:14]
		self.__hon_syokin_syogai = source[14:24]
		self.__fuka_syokin_heichi = source[24:34]
		self.__fuka_syokin_syogai = source[34:44]
		self.__chaku_kaisu_siba = CHAKUKAISU5_INFO(source[44:74])
		self.__chaku_kaisu_dirt = CHAKUKAISU5_INFO(source[74:104])
		self.__chaku_kaisu_syogai = CHAKUKAISU4_INFO(source[104:128])

		self.__chaku_kaisu_siba_kyori = []
		for i in range(9):
			self.__chaku_kaisu_siba_kyori.append(CHAKUKAISU4_INFO(source[128 + i * 24 :128 + i * 24 + 24]))

		self.__chaku_kaisu_dirt_kyori = []
		for i in range(9):
			self.__chaku_kaisu_dirt_kyori.append(CHAKUKAISU4_INFO(source[344 + i * 24 :344 + i * 24 + 24]))

		self.__chaku_kaisu_jyo_siba = []
		for i in range(10):
			self.__chaku_kaisu_jyo_siba.append(CHAKUKAISU4_INFO(source[560 + i * 24 :560 + i * 24 + 24]))

		self.__chaku_kaisu_jyo_dirt = []
		for i in range(10):
			self.__chaku_kaisu_jyo_dirt.append(CHAKUKAISU4_INFO(source[800 + i * 24 :800 + i * 24 + 24]))

		self.__chaku_kaisu_jyo_syogai = []
		for i in range(10):
			self.__chaku_kaisu_jyo_syogai.append(CHAKUKAISU3_INFO(source[1040 + i * 18 :1040 + i * 18 + 18]))

class JV_CK_KISYU:

	'''
	騎手コード
	'''
	__kisyu_cd = bytes()

	@property
	def kisyu_cd(self):
		return self.__kisyu_cd

	@kisyu_cd.setter
	def kisyu_cd(self, value):
		self.__kisyu_cd = value

	'''
	騎手名漢字
	'''
	__kisyu_name = bytes()

	@property
	def kisyu_name(self):
		return self.__kisyu_name

	@kisyu_name.setter
	def kisyu_name(self, value):
		self.__kisyu_name = value

	'''
	本年・累計成績情報
	'''
	__hon_ruikei = []

	@property
	def hon_ruikei(self):
		return self.__hon_ruikei

	@hon_ruikei.setter
	def hon_ruikei(self, value):
		self.__hon_ruikei = value

	def __init__(self, source : bytes) -> None:

		self.__kisyu_cd = source[0:5]
		self.__kisyu_name = source[5:39]

		self.__hon_ruikei = []
		for i in range(2):
			self.__hon_ruikei.append(JV_CK_HON_RUIKEISEI_INFO(source[39 + i * 1220 :39 + i * 1220 + 1220]))

class JV_CK_CHOKYOSI:

	'''
	調教師コード
	'''
	__chokyosi_cd = bytes()

	@property
	def chokyosi_cd(self):
		return self.__chokyosi_cd

	@chokyosi_cd.setter
	def chokyosi_cd(self, value):
		self.__chokyosi_cd = value

	'''
	調教師名漢字
	'''
	__chokyosi_name = bytes()

	@property
	def chokyosi_name(self):
		return self.__chokyosi_name

	@chokyosi_name.setter
	def chokyosi_name(self, value):
		self.__chokyosi_name = value

	'''
	本年・累計成績情報
	'''
	__hon_ruikei = []

	@property
	def hon_ruikei(self):
		return self.__hon_ruikei

	@hon_ruikei.setter
	def hon_ruikei(self, value):
		self.__hon_ruikei = value

	def __init__(self, source : bytes) -> None:

		self.__chokyosi_cd = source[0:5]
		self.__chokyosi_name = source[5:39]

		self.__hon_ruikei = []
		for i in range(2):
			self.__hon_ruikei.append(JV_CK_HON_RUIKEISEI_INFO(source[39 + i * 1220 :39 + i * 1220 + 1220]))

class JV_CK_BANUSI:

	'''
	馬主コード
	'''
	__banusi_cd = bytes()

	@property
	def banusi_cd(self):
		return self.__banusi_cd

	@banusi_cd.setter
	def banusi_cd(self, value):
		self.__banusi_cd = value

	'''
	馬主名（法人格有）
	'''
	__banusi_name__co = bytes()

	@property
	def banusi_name__co(self):
		return self.__banusi_name__co

	@banusi_name__co.setter
	def banusi_name__co(self, value):
		self.__banusi_name__co = value

	'''
	馬主名（法人格無）
	'''
	__banusi_name = bytes()

	@property
	def banusi_name(self):
		return self.__banusi_name

	@banusi_name.setter
	def banusi_name(self, value):
		self.__banusi_name = value

	'''
	本年・累計成績情報
	'''
	__hon_ruikei = []

	@property
	def hon_ruikei(self):
		return self.__hon_ruikei

	@hon_ruikei.setter
	def hon_ruikei(self, value):
		self.__hon_ruikei = value

	def __init__(self, source : bytes) -> None:

		self.__banusi_cd = source[0:6]
		self.__banusi_name__co = source[6:70]
		self.__banusi_name = source[70:134]

		self.__hon_ruikei = []
		for i in range(2):
			self.__hon_ruikei.append(SEI_RUIKEI_INFO(source[134 + i * 60 :134 + i * 60 + 60]))

class JV_CK_BREEDER:

	'''
	生産者コード
	'''
	__breeder_cd = bytes()

	@property
	def breeder_cd(self):
		return self.__breeder_cd

	@breeder_cd.setter
	def breeder_cd(self, value):
		self.__breeder_cd = value

	'''
	生産者（法人格有）
	'''
	__breeder_name__co = bytes()

	@property
	def breeder_name__co(self):
		return self.__breeder_name__co

	@breeder_name__co.setter
	def breeder_name__co(self, value):
		self.__breeder_name__co = value

	'''
	生産者（法人格無）
	'''
	__breeder_name = bytes()

	@property
	def breeder_name(self):
		return self.__breeder_name

	@breeder_name.setter
	def breeder_name(self, value):
		self.__breeder_name = value

	'''
	本年・累計成績情報
	'''
	__hon_ruikei = []

	@property
	def hon_ruikei(self):
		return self.__hon_ruikei

	@hon_ruikei.setter
	def hon_ruikei(self, value):
		self.__hon_ruikei = value

	def __init__(self, source : bytes) -> None:

		self.__breeder_cd = source[0:6]
		self.__breeder_name__co = source[6:76]
		self.__breeder_name = source[76:146]

		self.__hon_ruikei = []
		for i in range(2):
			self.__hon_ruikei.append(SEI_RUIKEI_INFO(source[146 + i * 60 :146 + i * 60 + 60]))

class JV_CK_CHAKU:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報１
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	出走別着度数
	'''
	__uma_chaku = None

	@property
	def uma_chaku(self):
		return self.__uma_chaku

	@uma_chaku.setter
	def uma_chaku(self, value):
		self.__uma_chaku = value

	'''
	出走別着度数
	'''
	__kisyu_chaku = None

	@property
	def kisyu_chaku(self):
		return self.__kisyu_chaku

	@kisyu_chaku.setter
	def kisyu_chaku(self, value):
		self.__kisyu_chaku = value

	'''
	出走別着度数
	'''
	__chokyo_chaku = None

	@property
	def chokyo_chaku(self):
		return self.__chokyo_chaku

	@chokyo_chaku.setter
	def chokyo_chaku(self, value):
		self.__chokyo_chaku = value

	'''
	出走別着度数
	'''
	__banusi_chaku = None

	@property
	def banusi_chaku(self):
		return self.__banusi_chaku

	@banusi_chaku.setter
	def banusi_chaku(self, value):
		self.__banusi_chaku = value

	'''
	出走別着度数
	'''
	__breeder_chaku = None

	@property
	def breeder_chaku(self):
		return self.__breeder_chaku

	@breeder_chaku.setter
	def breeder_chaku(self, value):
		self.__breeder_chaku = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__uma_chaku = JV_CK_UMA(source[27:1384])
		self.__kisyu_chaku = JV_CK_KISYU(source[1384:3863])
		self.__chokyo_chaku = JV_CK_CHOKYOSI(source[3863:6342])
		self.__banusi_chaku = JV_CK_BANUSI(source[6342:6596])
		self.__breeder_chaku = JV_CK_BREEDER(source[6596:6862])
		self.__crlf = source[6862:6864]

class JV_BT_KEITO:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	繁殖登録番号
	'''
	__hansyoku_num = bytes()

	@property
	def hansyoku_num(self):
		return self.__hansyoku_num

	@hansyoku_num.setter
	def hansyoku_num(self, value):
		self.__hansyoku_num = value

	'''
	系統ID
	'''
	__keito_id = bytes()

	@property
	def keito_id(self):
		return self.__keito_id

	@keito_id.setter
	def keito_id(self, value):
		self.__keito_id = value

	'''
	系統名
	'''
	__keito_name = bytes()

	@property
	def keito_name(self):
		return self.__keito_name

	@keito_name.setter
	def keito_name(self, value):
		self.__keito_name = value

	'''
	系統説明
	'''
	__keito_ex = bytes()

	@property
	def keito_ex(self):
		return self.__keito_ex

	@keito_ex.setter
	def keito_ex(self, value):
		self.__keito_ex = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__hansyoku_num = source[11:19]
		self.__keito_id = source[19:49]
		self.__keito_name = source[49:85]
		self.__keito_ex = source[85:6885]
		self.__crlf = source[6885:6887]

class JV_CS_COURSE:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競馬場コード
	'''
	__jyo_cd = bytes()

	@property
	def jyo_cd(self):
		return self.__jyo_cd

	@jyo_cd.setter
	def jyo_cd(self, value):
		self.__jyo_cd = value

	'''
	距離
	'''
	__kyori = bytes()

	@property
	def kyori(self):
		return self.__kyori

	@kyori.setter
	def kyori(self, value):
		self.__kyori = value

	'''
	トラックコード
	'''
	__track_cd = bytes()

	@property
	def track_cd(self):
		return self.__track_cd

	@track_cd.setter
	def track_cd(self, value):
		self.__track_cd = value

	'''
	コース改修年月日
	'''
	__kaishu_date = None

	@property
	def kaishu_date(self):
		return self.__kaishu_date

	@kaishu_date.setter
	def kaishu_date(self, value):
		self.__kaishu_date = value

	'''
	コース説明
	'''
	__course_ex = bytes()

	@property
	def course_ex(self):
		return self.__course_ex

	@course_ex.setter
	def course_ex(self, value):
		self.__course_ex = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__jyo_cd = source[11:13]
		self.__kyori = source[13:17]
		self.__track_cd = source[17:19]
		self.__kaishu_date = YMD(source[19:27])
		self.__course_ex = source[27:6827]
		self.__crlf = source[6827:6829]

class TM_INFO:

	'''
	馬番
	'''
	__umaban = bytes()

	@property
	def umaban(self):
		return self.__umaban

	@umaban.setter
	def umaban(self, value):
		self.__umaban = value

	'''
	予測スコア
	'''
	__t_m_score = bytes()

	@property
	def t_m_score(self):
		return self.__t_m_score

	@t_m_score.setter
	def t_m_score(self, value):
		self.__t_m_score = value

	def __init__(self, source : bytes) -> None:

		self.__umaban = source[0:2]
		self.__t_m_score = source[2:6]

class JV_TM_INFO:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	データ作成時分
	'''
	__make_h_m = None

	@property
	def make_h_m(self):
		return self.__make_h_m

	@make_h_m.setter
	def make_h_m(self, value):
		self.__make_h_m = value

	'''
	マイニング予想
	'''
	__t_m_info = []

	@property
	def t_m_info(self):
		return self.__t_m_info

	@t_m_info.setter
	def t_m_info(self, value):
		self.__t_m_info = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__make_h_m = HM(source[27:31])

		self.__t_m_info = []
		for i in range(18):
			self.__t_m_info.append(TM_INFO(source[31 + i * 6 :31 + i * 6 + 6]))

		self.__crlf = source[139:141]

class WF_RACE_INFO:

	'''
	競馬場コード
	'''
	__jyo_cd = bytes()

	@property
	def jyo_cd(self):
		return self.__jyo_cd

	@jyo_cd.setter
	def jyo_cd(self, value):
		self.__jyo_cd = value

	'''
	開催回[第N回]
	'''
	__kaiji = bytes()

	@property
	def kaiji(self):
		return self.__kaiji

	@kaiji.setter
	def kaiji(self, value):
		self.__kaiji = value

	'''
	開催日目[N日目]
	'''
	__nichiji = bytes()

	@property
	def nichiji(self):
		return self.__nichiji

	@nichiji.setter
	def nichiji(self, value):
		self.__nichiji = value

	'''
	レース番号
	'''
	__race_num = bytes()

	@property
	def race_num(self):
		return self.__race_num

	@race_num.setter
	def race_num(self, value):
		self.__race_num = value

	def __init__(self, source : bytes) -> None:

		self.__jyo_cd = source[0:2]
		self.__kaiji = source[2:4]
		self.__nichiji = source[4:6]
		self.__race_num = source[6:8]

class WF_YUKO_HYO_INFO:

	'''
	有効票数
	'''
	__yuko__hyo = bytes()

	@property
	def yuko__hyo(self):
		return self.__yuko__hyo

	@yuko__hyo.setter
	def yuko__hyo(self, value):
		self.__yuko__hyo = value

	def __init__(self, source : bytes) -> None:

		self.__yuko__hyo = source[0:11]

class WF_PAY_INFO:

	'''
	組番
	'''
	__umabanban = bytes()

	@property
	def umabanban(self):
		return self.__umabanban

	@umabanban.setter
	def umabanban(self, value):
		self.__umabanban = value

	'''
	重勝式払戻金
	'''
	__pay = bytes()

	@property
	def pay(self):
		return self.__pay

	@pay.setter
	def pay(self, value):
		self.__pay = value

	'''
	的中票数
	'''
	__tekichu__hyo = bytes()

	@property
	def tekichu__hyo(self):
		return self.__tekichu__hyo

	@tekichu__hyo.setter
	def tekichu__hyo(self, value):
		self.__tekichu__hyo = value

	def __init__(self, source : bytes) -> None:

		self.__umabanban = source[0:10]
		self.__pay = source[10:19]
		self.__tekichu__hyo = source[19:29]

class JV_WF_INFO:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	開催年月日
	'''
	__kaisai_date = None

	@property
	def kaisai_date(self):
		return self.__kaisai_date

	@kaisai_date.setter
	def kaisai_date(self, value):
		self.__kaisai_date = value

	'''
	予備
	'''
	__reserved1 = bytes()

	@property
	def reserved1(self):
		return self.__reserved1

	@reserved1.setter
	def reserved1(self, value):
		self.__reserved1 = value

	'''
	重勝式対象レース情報
	'''
	__w_f_race_info = []

	@property
	def w_f_race_info(self):
		return self.__w_f_race_info

	@w_f_race_info.setter
	def w_f_race_info(self, value):
		self.__w_f_race_info = value

	'''
	予備
	'''
	__reserved2 = bytes()

	@property
	def reserved2(self):
		return self.__reserved2

	@reserved2.setter
	def reserved2(self, value):
		self.__reserved2 = value

	'''
	重勝式発売票数
	'''
	__hatsubai__hyo = bytes()

	@property
	def hatsubai__hyo(self):
		return self.__hatsubai__hyo

	@hatsubai__hyo.setter
	def hatsubai__hyo(self, value):
		self.__hatsubai__hyo = value

	'''
	有効票数情報
	'''
	__w_f_yuko_hyo_info = []

	@property
	def w_f_yuko_hyo_info(self):
		return self.__w_f_yuko_hyo_info

	@w_f_yuko_hyo_info.setter
	def w_f_yuko_hyo_info(self, value):
		self.__w_f_yuko_hyo_info = value

	'''
	返還フラグ
	'''
	__henkan_flag = bytes()

	@property
	def henkan_flag(self):
		return self.__henkan_flag

	@henkan_flag.setter
	def henkan_flag(self, value):
		self.__henkan_flag = value

	'''
	不成立フラグ
	'''
	__fuseiritsu_flag = bytes()

	@property
	def fuseiritsu_flag(self):
		return self.__fuseiritsu_flag

	@fuseiritsu_flag.setter
	def fuseiritsu_flag(self, value):
		self.__fuseiritsu_flag = value

	'''
	的中無フラグ
	'''
	__tekichunashi_flag = bytes()

	@property
	def tekichunashi_flag(self):
		return self.__tekichunashi_flag

	@tekichunashi_flag.setter
	def tekichunashi_flag(self, value):
		self.__tekichunashi_flag = value

	'''
	キャリーオーバー金額初期
	'''
	__c_o_shoki = bytes()

	@property
	def c_o_shoki(self):
		return self.__c_o_shoki

	@c_o_shoki.setter
	def c_o_shoki(self, value):
		self.__c_o_shoki = value

	'''
	キャリーオーバー金額残高
	'''
	__c_o_zan_daka = bytes()

	@property
	def c_o_zan_daka(self):
		return self.__c_o_zan_daka

	@c_o_zan_daka.setter
	def c_o_zan_daka(self, value):
		self.__c_o_zan_daka = value

	'''
	重勝式払戻情報
	'''
	__w_f_pay_info = []

	@property
	def w_f_pay_info(self):
		return self.__w_f_pay_info

	@w_f_pay_info.setter
	def w_f_pay_info(self, value):
		self.__w_f_pay_info = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__kaisai_date = YMD(source[11:19])
		self.__reserved1 = source[19:21]

		self.__w_f_race_info = []
		for i in range(5):
			self.__w_f_race_info.append(WF_RACE_INFO(source[21 + i * 8 :21 + i * 8 + 8]))

		self.__reserved2 = source[61:67]
		self.__hatsubai__hyo = source[67:78]

		self.__w_f_yuko_hyo_info = []
		for i in range(5):
			self.__w_f_yuko_hyo_info.append(WF_YUKO_HYO_INFO(source[78 + i * 11 :78 + i * 11 + 11]))

		self.__henkan_flag = source[133:134]
		self.__fuseiritsu_flag = source[134:135]
		self.__tekichunashi_flag = source[135:136]
		self.__c_o_shoki = source[136:151]
		self.__c_o_zan_daka = source[151:166]

		self.__w_f_pay_info = []
		for i in range(243):
			self.__w_f_pay_info.append(WF_PAY_INFO(source[166 + i * 29 :166 + i * 29 + 29]))

		self.__crlf = source[139:141]

class JV_JG_JOGAIBA:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	競走識別情報
	'''
	__id = None

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	馬名
	'''
	__bamei = bytes()

	@property
	def bamei(self):
		return self.__bamei

	@bamei.setter
	def bamei(self, value):
		self.__bamei = value

	'''
	出馬投票受付順番
	'''
	__shutsuba_tohyo_jun = bytes()

	@property
	def shutsuba_tohyo_jun(self):
		return self.__shutsuba_tohyo_jun

	@shutsuba_tohyo_jun.setter
	def shutsuba_tohyo_jun(self, value):
		self.__shutsuba_tohyo_jun = value

	'''
	出走区分
	'''
	__shusso_kubun = bytes()

	@property
	def shusso_kubun(self):
		return self.__shusso_kubun

	@shusso_kubun.setter
	def shusso_kubun(self, value):
		self.__shusso_kubun = value

	'''
	除外状態区分
	'''
	__jogai_jotai_kubun = bytes()

	@property
	def jogai_jotai_kubun(self):
		return self.__jogai_jotai_kubun

	@jogai_jotai_kubun.setter
	def jogai_jotai_kubun(self, value):
		self.__jogai_jotai_kubun = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__id = RACE_ID(source[11:27])
		self.__ketto_num = source[27:37]
		self.__bamei = source[37:73]
		self.__shutsuba_tohyo_jun = source[73:76]
		self.__shusso_kubun = source[76:77]
		self.__jogai_jotai_kubun = source[77:78]
		self.__crlf = source[78:80]

class JV_WC_WOOD:

	'''
	レコードヘッダー
	'''
	__head = None

	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, value):
		self.__head = value

	'''
	トレセン区分
	'''
	__tresen_kubun = bytes()

	@property
	def tresen_kubun(self):
		return self.__tresen_kubun

	@tresen_kubun.setter
	def tresen_kubun(self, value):
		self.__tresen_kubun = value

	'''
	調教年月日
	'''
	__chokyo_date = None

	@property
	def chokyo_date(self):
		return self.__chokyo_date

	@chokyo_date.setter
	def chokyo_date(self, value):
		self.__chokyo_date = value

	'''
	調教時刻
	'''
	__chokyo_time = bytes()

	@property
	def chokyo_time(self):
		return self.__chokyo_time

	@chokyo_time.setter
	def chokyo_time(self, value):
		self.__chokyo_time = value

	'''
	血統登録番号
	'''
	__ketto_num = bytes()

	@property
	def ketto_num(self):
		return self.__ketto_num

	@ketto_num.setter
	def ketto_num(self, value):
		self.__ketto_num = value

	'''
	コース
	'''
	__course = bytes()

	@property
	def course(self):
		return self.__course

	@course.setter
	def course(self, value):
		self.__course = value

	'''
	馬場周り
	'''
	__baba_around = bytes()

	@property
	def baba_around(self):
		return self.__baba_around

	@baba_around.setter
	def baba_around(self, value):
		self.__baba_around = value

	'''
	予備
	'''
	__reserved = bytes()

	@property
	def reserved(self):
		return self.__reserved

	@reserved.setter
	def reserved(self, value):
		self.__reserved = value

	'''
	10ハロンタイム合計(2000M-0M)
	'''
	__haron_time10 = bytes()

	@property
	def haron_time10(self):
		return self.__haron_time10

	@haron_time10.setter
	def haron_time10(self, value):
		self.__haron_time10 = value

	'''
	ラップタイム(2000M-1800M)
	'''
	__lap_time10 = bytes()

	@property
	def lap_time10(self):
		return self.__lap_time10

	@lap_time10.setter
	def lap_time10(self, value):
		self.__lap_time10 = value

	'''
	9ハロンタイム合計(1800M-0M)
	'''
	__haron_time9 = bytes()

	@property
	def haron_time9(self):
		return self.__haron_time9

	@haron_time9.setter
	def haron_time9(self, value):
		self.__haron_time9 = value

	'''
	ラップタイム(1800M-1600M)
	'''
	__lap_time9 = bytes()

	@property
	def lap_time9(self):
		return self.__lap_time9

	@lap_time9.setter
	def lap_time9(self, value):
		self.__lap_time9 = value

	'''
	8ハロンタイム合計(1600M-0M)
	'''
	__haron_time8 = bytes()

	@property
	def haron_time8(self):
		return self.__haron_time8

	@haron_time8.setter
	def haron_time8(self, value):
		self.__haron_time8 = value

	'''
	ラップタイム(1600M-1400M)
	'''
	__lap_time8 = bytes()

	@property
	def lap_time8(self):
		return self.__lap_time8

	@lap_time8.setter
	def lap_time8(self, value):
		self.__lap_time8 = value

	'''
	7ハロンタイム合計(1400M-0M)
	'''
	__haron_time7 = bytes()

	@property
	def haron_time7(self):
		return self.__haron_time7

	@haron_time7.setter
	def haron_time7(self, value):
		self.__haron_time7 = value

	'''
	ラップタイム(1400M-1200M)
	'''
	__lap_time7 = bytes()

	@property
	def lap_time7(self):
		return self.__lap_time7

	@lap_time7.setter
	def lap_time7(self, value):
		self.__lap_time7 = value

	'''
	6ハロンタイム合計(1200M-0M)
	'''
	__haron_time6 = bytes()

	@property
	def haron_time6(self):
		return self.__haron_time6

	@haron_time6.setter
	def haron_time6(self, value):
		self.__haron_time6 = value

	'''
	ラップタイム(1200M-1000M)
	'''
	__lap_time6 = bytes()

	@property
	def lap_time6(self):
		return self.__lap_time6

	@lap_time6.setter
	def lap_time6(self, value):
		self.__lap_time6 = value

	'''
	5ハロンタイム合計(1000M-0M)
	'''
	__haron_time5 = bytes()

	@property
	def haron_time5(self):
		return self.__haron_time5

	@haron_time5.setter
	def haron_time5(self, value):
		self.__haron_time5 = value

	'''
	ラップタイム(1000M-800M)
	'''
	__lap_time5 = bytes()

	@property
	def lap_time5(self):
		return self.__lap_time5

	@lap_time5.setter
	def lap_time5(self, value):
		self.__lap_time5 = value

	'''
	4ハロンタイム合計(800M-0M)
	'''
	__haron_time4 = bytes()

	@property
	def haron_time4(self):
		return self.__haron_time4

	@haron_time4.setter
	def haron_time4(self, value):
		self.__haron_time4 = value

	'''
	ラップタイム(800M-600M)
	'''
	__lap_time4 = bytes()

	@property
	def lap_time4(self):
		return self.__lap_time4

	@lap_time4.setter
	def lap_time4(self, value):
		self.__lap_time4 = value

	'''
	3ハロンタイム合計(600M-0M)
	'''
	__haron_time3 = bytes()

	@property
	def haron_time3(self):
		return self.__haron_time3

	@haron_time3.setter
	def haron_time3(self, value):
		self.__haron_time3 = value

	'''
	ラップタイム(600M-400M)
	'''
	__lap_time3 = bytes()

	@property
	def lap_time3(self):
		return self.__lap_time3

	@lap_time3.setter
	def lap_time3(self, value):
		self.__lap_time3 = value

	'''
	2ハロンタイム合計(400M-0M)
	'''
	__haron_time2 = bytes()

	@property
	def haron_time2(self):
		return self.__haron_time2

	@haron_time2.setter
	def haron_time2(self, value):
		self.__haron_time2 = value

	'''
	ラップタイム(400M-200M)
	'''
	__lap_time2 = bytes()

	@property
	def lap_time2(self):
		return self.__lap_time2

	@lap_time2.setter
	def lap_time2(self, value):
		self.__lap_time2 = value

	'''
	ラップタイム(200M-0M)
	'''
	__lap_time1 = bytes()

	@property
	def lap_time1(self):
		return self.__lap_time1

	@lap_time1.setter
	def lap_time1(self, value):
		self.__lap_time1 = value

	'''
	レコード区切り
	'''
	__crlf = bytes()

	@property
	def crlf(self):
		return self.__crlf

	@crlf.setter
	def crlf(self, value):
		self.__crlf = value

	def __init__(self, source : bytes) -> None:

		self.__head = RECORD_ID(source[0:11])
		self.__tresen_kubun = source[11:12]
		self.__chokyo_date = YMD(source[12:20])
		self.__chokyo_time = source[20:24]
		self.__ketto_num = source[24:34]
		self.__course = source[34:35]
		self.__baba_around = source[35:36]
		self.__reserved = source[36:37]
		self.__haron_time10 = source[37:41]
		self.__lap_time10 = source[41:44]
		self.__haron_time9 = source[44:48]
		self.__lap_time9 = source[48:51]
		self.__haron_time8 = source[51:55]
		self.__lap_time8 = source[55:58]
		self.__haron_time7 = source[58:62]
		self.__lap_time7 = source[62:65]
		self.__haron_time6 = source[65:69]
		self.__lap_time6 = source[69:72]
		self.__haron_time5 = source[72:76]
		self.__lap_time5 = source[76:79]
		self.__haron_time4 = source[79:83]
		self.__lap_time4 = source[83:86]
		self.__haron_time3 = source[86:90]
		self.__lap_time3 = source[90:93]
		self.__haron_time2 = source[93:97]
		self.__lap_time2 = source[97:100]
		self.__lap_time1 = source[100:103]
		self.__crlf = source[103:105]

