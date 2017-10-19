# Virtualenv
독립적인 가상의 파이썬 실행환경을 위한 tool

## python packages
pip install <module> 을 하면 프로젝트 구분없이 아래의 경로에 설치됨 (파이썬 버전 및 환경에 따라 다를수 있음)
```
>>> import sys
>>> print(sys.path)
['', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35-32\\python35.zip', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35-32\\DLLs', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35-32\\lib', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35-32', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\site-packages', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\site-packages\\win32', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\site-packages\\win32\\lib', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\site-packages\\Pythonwin']
```
> - PC: `C:\Users\user\AppData\Local\Programs\Python\Python36-32\Lib`
> - Mac: `/Library/Frameworks/Python.framework/Versions/3.6/lib/site-packages`

## pip freeze
pip install로 설치한 package 들을 list로 보여준다.

보통 배포를 위해서 `pip freeze > requirements.txt` 로 의존관리 파일을 생성한다.

이때 해당 프로젝트와 관련이 없는 package 들도 list로 나열된다.

```console
> pip freeze
aiohttp==2.2.5
APScheduler==3.3.1
asn1crypto==0.22.0
astroid==1.5.3
async-timeout==1.2.1
attrs==17.2.0
Automat==0.6.0
beautifulsoup4==4.5.1
bidict==0.13.0
bleach==1.5.0
...
중략
...
```

이때 A 프로젝트와 B 프로젝트에서 각각 다른 버전의 package를 쓰려고 하면 문제가 발생한다.
또한 각각의 프로젝트에서 의존성을 관리하기도 힘들다.

## virtualenv 설치
```
> pip install virtualenv
```
> [Installation](https://virtualenv.pypa.io/en/stable/installation/) 참고

## 사용방법

### 초기화
특정 프로젝트에서 독립된 파이썬 환경 구성해준다.
```
virtualenv <project folder name>
```
위 명령 실행을 실행하면 아래와 같이 파일 및 디렉토리가 생성된다.
> - `lib (Lib)`, `include (Include)` - Python 기본 라이브러리 및 신규 설치될 라이브러리
> - `bin (Scripts)` -  독립된 Python 실행파일들이 위치

### 적용
```
> (unix) source bin/activate
> (pc) Scripts/activate
```

### 해제
```
> deactivate
```

## 참고
* [virtualenv](https://virtualenv.pypa.io)
* [pip freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/)
* [The Environment Variables Pattern](https://medium.com/@gitudaniel/the-environment-variables-pattern-be73e6e0e5b7)