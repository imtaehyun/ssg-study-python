# 설치하기
## Virtualenv 설치
```
pip install virtualenv
```

## Virtualenv 실행
```
mkdir myproject
cd myproject
virtualenv venv
venv\scripts\activate
```

venv를 가상환경으로 설정하면, pyCharm에서 가상환경을 자동으로 인식한다.
가상환경 비활성화는 deactivate

## Flask 설치
```
pip install Flask
```

# 빠르게 시작하기
## 기본 어플리케이션
```python
#hello.py 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	app.debug = True
	app.run()
```
* hello.py 실행 후 http:127.0.0.1:5000/ 으로 접근

pyCharm 에서 unresolved reference flask가 나오는 이슈가 있을 경우
1. File > Invalidate Caches/Restart 선택 후 Invalidate Restart
2. File > Settings 에서 Project Interpreter를 확인하여 venv 경로인지 확인

## Flask 라우팅
* app.route() 를 통해 URL 패턴과 POST Method 정의하며 하단의 함수에서 action을 처리한다.
* app.debug가 True일 때 코드가 변경될 경우 자동으로 서버가 재실행된다.
* 현재 로컬에서만 접근 가능하며 외부에서 접근 가능하도록 하기 위해서 app.run(host='0.0.0.0') 으로 실행부를 변경하여야 한다. 웹 상에서 python 코드를 변경 할 수 있으므로 운영환경에서 사용을 유의해야 한다.

## 라우팅 변수 처리
```python
@app.route('/user/<userName>')
def showUserId(userName):
	return 'User ID: {}'.format(userName)

@app.route('/user/<int:userId>')
def showUserId(userId):
	return 'User ID: {}'.format(userId)
```
* <>을 사용하여 변수를 라우팅 패턴 정의에 사용할 수 있다.

## HTTP Method 설정
```python
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()
```
* defualt는 GET 방식이며 사용할 method를 설정할 수 있다.
* request.method 에 따라 처리할 수 있다.

## 템플릿 보여주기
Flask는 HTML 문서의 동적으로 변환되는 값을 위하여 Jinja2를 템플릿 엔진으로 구성하여 사용한다.
Jinja2에 대한 자세한 문서는 Jinja2(http://jinja.pocoo.org/docs/2.9/templates/)을 참조하자.
템플릿을 보여주기 위해 render_template() 메소드를 사용한다. 
아래의 예를 보자.

```python
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)
```

위의 코드에서 Flask는 template 폴더에서 hello.html 이라는 이름의 템플릿을 찾는다. 
hello.html은 아래와 같이 작성했다.
```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```
Jinja2 문법을 사용하여 작성하였을 경우 문서 내에서 {{ name }} 과 같이 동적 변수의 값을 가져와 페이지를 구성한다.

## 요청 데이터 접근하기
Flask의 요청객체를 이용해 요청 데이터를 가져올 수 있다. 아래의 예시를 보자.

```python
from flask import request

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST
```

요청객체를 통해 request path와 method를 확인할 수 있다.
form 데이터에 접근하기 위해 form 속성을 사용할 수 있으며 URL로 넘겨진 파라미터 접근하기 위해(?key=value 형식)에 접근하기 위해 args 속성을 사용할 수 있다.

```python
requset.form['username']
request.form['password']
request.args.get('key')	
```

요청 데이터에 접근할 때 해당 key를 갖는 데이터가 없으면 KeyError가 발생한다. 따라서 KeyError 예외 처리하거나 default 값을 지정하도록 하자.

```python
requset.args.get('key', '') #defualt 값
```

쿠키 데이터 접근을 위해 cookies 속성을 사용할 수 있다. 아래의 예시에서는 username을 key로 가지는 쿠키를 가져올 수 있다. 

```python
requset.cookies.get('username')
```

## Flask 로깅
Flask는 app에서 사용할 loger가 미리 설정되어 있다. 아래는 로그를 출력하는 예시이다.
```python
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```

## 참고문서
* http://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html
