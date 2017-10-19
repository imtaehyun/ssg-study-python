# # CSS 선택자
# # Copy -> Copy Selector 유용 // page35 CSS선택자 상세
# #01 작품 목록 가져오기
#
# from bs4 import BeautifulSoup
# import urllib.request as req
#
# url = "https://ko.wikipedia.org/wiki/%EC%95%8C%EB%9E%AD_%EB%93%9C_%EB%B3%B4%ED%86%B5#.EC.A0.80.EC.84.9C"
# res = req.urlopen(url)
# soup = BeautifulSoup(res, "html.parser")
#
# #   카피 셀렉터
# #   #mw-content-text > div > ul:nth-child(9) > li:nth-child(1)
# #  #mw-content-text > div > ul > li
# a_list = soup.select("#mw-content-text > div > ul > li")
#
# for a in a_list:
#     name = a.string
#     print("-", name)
#
######################################################################################################
#
# #02 CSS 선택자 추출
# from bs4 import BeautifulSoup
#
# html = """
#     <ul id="infra">
#         <li id="sd">dong</li>
#         <li id="han">taehyun</li>
#         <li id="woo">jin</li>
#         <li id="siwon">minjung</li>
#         <li id="hy">sy</li>
#     </ul>
#     """
# soup = BeautifulSoup(html, "html.parser")
#
# sel = lambda q : print(soup.select_one(q).string)   # 요소 하나 추출
# #print(soup.select_one("#woo").string)
# sel("#woo")
# sel("li#sd")
# sel("ul > li#sd")
# sel("#infra #sd")
# sel("#infra > #han")
# sel("ul#infra > li#siwon")
# sel("li[id='hy']")
# sel("li:nth-of-type(4)")        # BS는 위치 or 상태 지정 서식 중 이것만 제공
#
# # 메서드 사용
# print(soup.select("li")[3].string)
# print(soup.find_all("li")[3].string)
#
######################################################################################################
# # #03-1 네이버 영화 순위 가져오기
# import urllib.request as req
# from bs4 import BeautifulSoup
# url="http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
# soup = BeautifulSoup(req.urlopen(url).read())
# pkg_list=soup.findAll("div", "tit3")  # div tag의 tit3 속성
#
# count = 1
# for i in pkg_list:
#     title = i.findAll('a')
#     print (count, "위: ", str(title)[str(title).find('title="')+7:str(title).find('">')])
#     count=count+1
#
# ######################################################################################################
# #03-2 네이버 영화 순위 가져오기 - copy -> copy selector
import urllib.request as req
from bs4 import BeautifulSoup
url="http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
soup = BeautifulSoup(req.urlopen(url), "html.parser")

b_list = soup.select('#old_content > table > tbody > tr > td.title > div')

countName = 1
for b in b_list:
    name = b.find_all('a')[0]
    print(type(name))
    print(name.get("title"))
    #print(name.string)
    print(countName,"위",str(name)[str(name).find('title=')+7:str(name).find('">')])
    countName += 1
# #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# # #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
