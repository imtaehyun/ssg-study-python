# # #01 상대경로를 절대경로로 바꾸기
# from urllib.parse import urljoin
#
# base = "http://example.com/html/a.html"
#
# print( urljoin(base, "b.html") )
# print( urljoin(base, "sub/c.html"))
# print( urljoin(base, "sub/c.png"))
# print( urljoin(base, "/sub/c.png"))
# print( urljoin(base, "../index.html"))
# print( urljoin(base, "../img/hoge.png"))
# print( urljoin(base, "../css/hoge.css"))
# print( urljoin(base, "http://otherExample.com/css/hoge.css"))
# print( urljoin(base, "//otherExample.com/css/hoge.css"))


#02 재귀적으로 처리하기. -> 모든 페이지를 한꺼번에 다운받기 위해서.
#파이썬 매뉴얼을 재귀적으로 다운받는 프로그램
#모듈 읽어 들이기 1
from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

# 2
proc_files = {}

#3 HTML 내부에 있는 링크를 추출하는 함수
def enum_links(html, base):
    soup  = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")  # CSS
    links += soup.select("a[href]")  # 링크
    result = []
    #4 href 속성을 추출하고, 링크를 절대 경로로 변환
    for a in links:
        href = a.attrs['href']
        url  = urljoin(base, href)
        result.append(url)
    return result

#5 파일을 다운받고 저장하는 함수
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath): # 폴더라면 index.html
       savepath += "index.html"
    savedir = os.path.dirname(savepath)

    # 모두 다운됐는지 확인
    if os.path.exists(savepath): return savepath
    # 다운받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)
    #6 파일다운받기
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1) #7 1초 휴식
        return savepath
    except:
        print("다운 실패: ", url)
        return None

#8 HTML을 분석하고 다운받는 함수
def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return #9 이미 처리된거면 실행하지 않음
    proc_files[savepath] =  True
    print("analyze_html=",url)
    #링크 추출
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)

    for link_url in links:
        #11 링크가 루트 이외의 경로를 나타낸다면 무시
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url): continue
        # HTML이라면
        if re.search(r".(html|html)$", link_url):
            # 재귀적으로 HTML 파일 분석하기
            analyze_html(link_url, root_url)
            continue
        # 기타 파일
        download_file(link_url)

if __name__ == "__main__":
    # URL에 있는 모든 것 다운 받기
    url = "http://docs.python.org/3.5/library/"
    analyze_html(url, url)



