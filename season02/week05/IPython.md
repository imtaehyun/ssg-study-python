# IPython

데이터 탐색, 실험, 오류판독, 반복 등을 빠르게 처리할 수 있는 대화형 파이썬 인터프리터

## IPython 기본

- 탭자동완성 

  - 지금까지 입력한 내용과 맞아 떨어지는 변수(객체, 함수 등)
  - 객체 및 모듈 속성
  - 파일 경로

- 자기관찰

  - ? - 변수 / 함수의 정보 출력
  - ?? - 함수의 소스코드 출력

- %run

  - 외부 python 파일을 실행

    ```
    > %run ipython_script_test.py [args]
    ```

- 클립보드 복사

  - Ctrl + Shift + V
  - 오류가 발생할때는 `%paste`나 `%cpaste`함수를 쓰면 클립보드의 텍스트를 단일 블록으로 실행

- 예외와 트레이스백

  - 일반 파이썬 인터프리터와는 다르게 오류발생시 추가 정보를 제공한다

- 매직 명령어

  - ?를 통해 추가옵션을 확인가능

    ```
    > %reset?
    ```

  - 매직 명령어와 동일한 이름의 변수가 선언되지 않은경우 % 기호없이 사용 가능 (%automagic으로 on/off)

  - 명령어 조회는 `%quickref`, `%magic`

- Qt기반의 GUI콘솔

  - 그림 삽입, 여러줄 편집, 리치텍스트위젯 기능 추가를 위해서는 GUI 콘솔을 실행

    ```
    > ipython qtconsole --pylab=inline
    ```

    ​

## 명령어 히스토리 사용하기

실행했던 명령어를 온-디스크 DB로 보관하며, 검색, 자동완성, 재실행 등에 사용된다. 

- 명령어 검색과 재사용
  - Ctrl + P (위)
  - Ctrl + N (아래)
  - Ctrl + R: 명령 검색
- 입출력 변수
  - _iX (X는 입력줄번호): 입력변수
  - _X (X는 출력줄 번호): 출력 변수
  - 입력변수는 문자열, 다시실행하기위해선 `exec _iX`
- 입출력 기록하기
  - `%logstart`를 통해 입출력을 포함한 전체 콘솔 세션의 로그를 기록 가능



## 운영체제와 함께 사용하기

IPython은 운영체제 셸과 강력하게 통합되어 있다. IPython 종료 없이 윈도우, 유닉스 셸을 실행 할 수 있다.

- 셀 명령어와 별칭

  - `!<cmd>`: cmd를 시스템 셸에서 실행

    ```
    > ip_info = !ifconfig eth0 | grep "inent "
    > ip_info[0].strip()
    'inet addr:192.168.1.137 Bcast:192.168.1.255'
    ```

  - 파이썬의 변수를 셸 변수로 대체 가능. (`$`를 사용)

    ```
    > foo = 'test*'
    > !ls $foo
    test4.py test.py
    ```

  - `%alias`: 셸 명령어에 대한 단축키 (세미콜론으로 구분하여 한번에 실행 가능)

    ```
    > %alias ll ls -l
    > %alias test_alias (cd ch08; ls; cd ..)
    ```

    ​

- 디렉터리 북마크 시스템

  - 자주 사용하는 디렉터리에 대한 별칭 저장 가능

    ```
    > %bookmark db /home/wesm/Dropbox/
    > cd db
    (bookmark:db) -> /home/wesm/Dropbox/
    /home/wesm/Dropbox
    > %bookmark -l
    Current bookmarks:
    db -> /home/wesm/Dropbox
    ```

  - 북마크는 IPython이 종료되더라도 유지된다



## 소프트웨어 개발 도구

- 인터랙티브 디버거
  - 에러가 발생한 후 `%debug` 명령어를 사용하면 사후처리 디버거가 실행, 예외가 발생한 시점의 스택프레임 정보를 출력
  - `u(up)`, `d(down)` 을 눌러서 스택 트레이스 사이를 이동
- 코드 시간 측정
  - `%time`: 한문장을 실행하고 소요된 전체 시간을 측정
  - `%timeit`: 한문장을 여러번 실행해보고 평균 실행 시간을 측정
- 기본적 프로파일링 - 임의의 파이썬 문장(함수)을 프로파일링
  - `%prun`
  - `%run -p`
  - `%lprun -f func1 -f func2 statement_to_profile`: 함수의 각 줄마다 프로파일링



## IPython HTML 노트북

Jupyter Notebook로 변경됨

```
> ipython notebook --pylab=inline 
[TerminalIPythonApp] WARNING | Subcommand `ipython notebook` is deprecated and will be removed in future versions.
[TerminalIPythonApp] WARNING | You likely want to use `jupyter notebook` in the future
[E 10:55:15.267 NotebookApp] Support for specifying --pylab on the command line has been removed.
[E 10:55:15.267 NotebookApp] Please use `%pylab inline` or `%matplotlib inline` in the notebook itself.
> jupyter notebook
```



## IPython을 사용한 제품 개발을 위한 팁

- 모듈의 의존성 리로딩하기
  - `reload(some_lib)`
    - 의존성이 깊어질수록 모든곳에 reload를 사용해야하는 번거로움
    - 이때는 import some_lib 대신 `dreload(some_lib)`을 사용
- 코드 설계 팁
  - 관련있는 객체와 데이터는 유지
  - 중첩을 피하자 - 결합도를 낮추고 모듈화하면 디버깅이 쉽고 대화형 방식으로 사용하기 쉽다
- 긴 파일에 대한 두려움을 버리자
  - 파일이 적다 = 리로드할 모듈이 적다



## IPython 고급 기능

- IPython 친화적인 클래스 만들기

  - `__repr__`

    ```python
    class Message:
      def __init__(self, msg):
        self.msg = msg
        
      def __repr__(self):
        return 'Message: {}'.format(self.msg)

    x = Message('I have a secret')
    x
    # Message: I have a secret
    ```

    ​

- 프로파일과 설정

  - 색상 스키마 변경
  - 입출력 프롬프트 모양 변경
  - 여러개의 임의의 파이썬 문장 실행 (항상 사용하는 모듈 import 등)
  - line_profiler의 매직함수 활성화
  - 사용자 매직 함수 정의, 시스템 별칭 정의
  - `~/.config/ipython/profile_default/ipython_config.py` 파일에서 설정 변경 가능