# 고급 스크레이핑
1. 로그인이 필요한 사이트에서 다운받기
2. 웹 브라우저를 이용한 스크레이핑
	- http://phantomjs.org
3. 웹 API로 데이터 추출하기 (생략)
4. cron을 이용한 정기적인 크롤링
	- https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_%EB%B0%98%EB%B3%B5_%EC%98%88%EC%95%BD%EC%9E%91%EC%97%85_cron,_crond,_crontab


# Docker 에서 Selenium + PhantomJS 실행환경 준비
## Docker 설치 (https://docs.docker.com/)
- docker for mac, docker for windows 는 최신 OS 만을 지원한다
- 최신 OS가 아닌 경우, docker toolbox 를 사용하자

```
# Ubuntu 이미지 가져오기
docker pull unbuntu:16.04

# Ubuntu 이미지를 실행하고 셸에 들어가기
docker run -it ubuntu:16.04

# python3 설치
apt-get update
apt-get install -y python3 python3-pip

# selenium, beautifulSoup 모듈 설치
pip3 install selenium
pip3 install beautilfulSoup4메

# PhantomJs 설치
apt-get install -y wget libfontconfig
mkdir -p /home/root/src && cd $_
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
cd phantomjs-2.1.1-linux-x86_64/bin/
cp phantomjs /usr/local/bin

# 한글폰트 설치
apt-get install -y fonts-nanum*

# 셸에서 나오기
eixt

# 컨테이너 저장
docker ps -a
<컨테이너 ID>
docker commit <컨테이너 ID> ubuntu-phantomjs

# 컨테이너 실행
docker run -it -v $HOME:$HOME -e ko_KR.UTF-8 -e PYTHONIOENCODING=utf_8 c /bin/bash
```
