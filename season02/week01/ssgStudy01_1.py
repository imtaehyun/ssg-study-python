# 딱 두 가지만 알자
# urllib => urllib.request 모듈의 urlretrieve()함수, urlopen()함수

# #01 urllib.request를 이용한 파일 다운로드(웹에 있는 PNG파일 다운받기)
# #   urllib.request 모듈의 urlretrieve 함수 사용
# import urllib.request
#
# # url과 저장경로 지정
# url = "http://uta.pw/shodou/img/28/214.png"
# savename = "test.png"
#
# # 다운로드
# urllib.request.urlretrieve(url, savename)
# print("저장되었습니다...!")
#
# url = "https://i.pinimg.com/236x/2d/13/81/2d138195418a5bf5f142e838ccc5f0bf--cancer-pinterest.jpg"
# savenameSsg = "ssg.jpg"
#
# # 다운로드
# urllib.request.urlretrieve(url, savenameSsg)
# print("저장되었습니다...!")
#
# ######################################################################################################
# #
# #02 urlopen()으로 파일에 저장
# #   urlopen()을 이용하여 곧바로 저장하는 것이 아닌 데이터를 파이썬 메모리 위에 올려놓음.
# import urllib.request
#
# url = "https://lh3.googleusercontent.com/XfUEyTOAQpeLj6c32aB2egbNZ2v8n7KcvAJ3NJtkpa1FTGCdxLHzQTqgR7j3UxAPCoA=w300" #"http://uta.pw/shodou/img/28/214.png"
# savename = "test011.png"
#
# # 다운로드
# mem = urllib.request.urlopen(url).read()
#
# # 파일로 저장
# with open(savename, mode="wb") as f:
#     f.write(mem)  # 다운로드한 바이너리 데이터를 파일에 저장
#     print("저장되었습니다...!")
# #
# ######################################################################################################
#
# #03 웹에서 데이터 추출하기 - (시간 없으면 pass)
# #   클라이언트 접속 정보 출력
# import urllib.request
#
# url = "http://api.aoikujira.com/ip/ini"
# res = urllib.request.urlopen(url)
# data = res.read()
#
# # 바이너리 -> 문자열
# text = data.decode("utf-8")
# print(text)
#
# ######################################################################################################
# # XML // HTML
# #04 매개변수 추가해서 요청하기 - 기상청 RSS 서비스 : 지역번호 => `108, 109...'
# #   매개변수를 만들기 위해 urllib.parse 모듈의 urlencode() 함수로 매개변수를 URL 인코딩
# import urllib.request
# import urllib.parse
#
# API = "http://movie.naver.com/movie/bi/mi/point.nhn"
#     #"http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# #매개변수를 url 인코딩하기
# values = {
#     'code' : '161242'
#     #'stnId' : '109'
# }
# params = urllib.parse.urlencode(values)
# # 요청 전용 URL 생성
# url = API + "?" + params
# print("url=",url)
# print(params)
# # 다운로드
# data = urllib.request.urlopen(url).read()
# text = data.decode("utf-8")
# print(text)
#
# ######################################################################################################
# # #05 <매개변수를 명령줄에서 지정하기>
# # sys 모듈  // as alias
# import sys
# import urllib.request as req
# import urllib.parse as parse
#
# # 명령줄 매개변수 추출 - sys.argv에 리스트형태로 들어옴 // sys.argv[0] : 스크립트 이름 , [1]부터 명령줄 매개변수 설정
# # if len(sys.argv)<=1:
# #     print("USAGE: download-forecast-argv <Region Number>")
# #     sys.exit()
# # regionNumber = sys.argv[1]
#
# regionNumber = input("입력 : ")
# # 매개변수를 URL 인코딩합니다.
# API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# values = {
#     'stnId' : regionNumber
# }
# params = parse.urlencode(values)
# url = API + "?" + params
# print ("url=", url)
#
# #다운로드
# data = req.urlopen(url).read()
# text = data.decode("utf-8")
# print(text)
#
# ######################################################################################################
#
# # 파이썬 입력 : sys
# import sys
#
# for i in sys.argv:
#     print(i)
#
# var1 = sys.argv[1]
# var2 = sys.argv[2]
#
# print ("var1 = ", var1)
# print ("var2 = ", var2)
# print (sys.argv[0])

# ######################################################################################################

# # 파이썬 입력 : input
# name = input("이름을 입력하세요 : ")
# print("이름 : ", name)