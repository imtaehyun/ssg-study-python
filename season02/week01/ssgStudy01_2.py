# ######################################################################################################
# BeautifulSoup 기본 - 스크레이퓡~
# html, xml 분석 라이브러리 => ** BS4 자체에는 다운로드 기능없음
# pip3 install beautifulsoup4 설치
#
# # #01 기본
# from bs4 import BeautifulSoup
#
# # 분석할 HTML
# html = """
# <html><body>
#     <h1>스크레이핑이란?</h1>
#     <p>웹 페이지를 분석하는 것</p><p id="body">원하는 부분을 추출하는 것</p>
# </body></html>
# """
# # HTML 분석
# soup = BeautifulSoup(html, 'html.parser')
#
# # 추출
# h1 = soup.html.body.h1
# p1 = soup.html.body.p
# p2 = p1.next_sibling#.next_sibling  # 한번만 하면 줄바꿈or 공백이 선택됨
#
# # 출력
# print("h1 = "+h1.string)
# print("p = "+p1.string)
# print("p = "+p2.string)
#
# ######################################################################################################
#
#02 id(속성)로 요소찾기 - find 메서드(bs4에서 제공하는 요소찾는 함수)

# from bs4 import BeautifulSoup
# html = """
# <html><body>
#     <h1 id="title">스크레이핑이란?</h1>
#     <p>웹 페이지를 분석하는 것</p>
#     <p id="body">원하는 부분을 추출하는 것</p>
# </body></html>
# """
#
# # HTML 분석
# soup = BeautifulSoup(html, 'html.parser')
#
# # find() 메서드로 원하는 부분 추출
# title = soup.find(id="title")
# body = soup.find(id="body")
#
# # 출력
# print("#title = "+title.string)
# print("#body=" + body.string)
#
# ######################################################################################################
#
# #03 id로 요소찾기 - find_all() 메서드 (여러개의 요소 추출)
# from bs4 import BeautifulSoup
# html = """
# <html><body>
#     <ul>
#       <li><a href= "http://www.naver.com">naver</a></li>
#       <li><a href= "http://www.daum.com">daum</a></li>
#     </ul>
# </body></html>
# """
#
# # HTML 분석
# soup = BeautifulSoup(html, 'html.parser')
#
# # find() 메서드로 원하는 부분 추출
# links = soup.find_all("a")
#
# # 링크목록 출력
# for a in links:
#       href = a.attrs['href']      # 속성(href)값 : http://www.naver.com ...
#       text = a.string             # 내용값 naver, daum
#       print(text, ">", href)

# ######################################################################################################
#
# #04 urlopen과 BeautifulSoup 조합 : urlopen() 함수로 데이터 가져오기.
# import urllib.request as req
# from bs4 import BeautifulSoup
#
# url = "http://movie.naver.com/movie/bi/mi/point.nhn?code=161242"     #"http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
#
# # urlopen()으로 데이터 가져오기
# resKma = req.urlopen(url)
#
# soupKma = BeautifulSoup(resKma, "html.parser")
#
# # 데이터 추출 title
# titleKma = soupKma.find("title").string
# print(titleKma)
#
# ######################################################################################################

#05 네이버 금융에서 환율 정보 추출
# import urllib.request as req
# from bs4 import BeautifulSoup
#
# # HTML 가져옴
# url = "http://info.finance.naver.com/marketindex"
# res = req.urlopen(url)
#
# # 분석
# soup = BeautifulSoup(res, "html.parser")
#
# # 추출
# price = soup.select_one("div.head_info > span.value").string
# print("usd/krw =", price)

# CSS 선택자 사용하기
# soup.select_one(선택자) : 요소 하나 추출
# soup.select(선택자)     : 요소 여러 개 리스트로 추출


