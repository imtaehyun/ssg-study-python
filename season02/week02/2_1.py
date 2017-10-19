import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디와 비밀번호 지정
USER = "ID"
PASS = "password"

# 세션 시작
with requests.session() as session:
    # 로그인하기
    login_info = {
        "m_id": USER,
        "m_passwd": PASS
    }
    url = "http://www.hanbit.co.kr/member/login_proc.php"
    response = session.post(url, data=login_info)
    response.raise_for_status()

    # 마이페이지 접근하기
    url = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
    response = session.get(url)
    response.raise_for_status()

    # 마일리지와 이코인 가져오기
    soup = BeautifulSoup(response.text, "html.parser")
    mileage = soup.select_one(".mileage_section1 span").string
    ecoin = soup.select_one(".mileage_section2 span").string

    print("마일리지: " + mileage)
    print("이코인: " + ecoin)

# 데이터 가져오기
res = requests.get("http://movie.naver.com/movie/bi/mi/basic.nhn?code=161242")
text = res.text
print(text)

res = requests.get("http://movie.phinf.naver.net/20170915_299/1505458505658vbKcN_JPEG/movie_image.jpg?type=f125")
binary = res.content
with open("test.png", "wb") as f:
    f.write(binary)
