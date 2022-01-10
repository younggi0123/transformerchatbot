from flask import Flask
# Flask라는 클래스의 객체를 생성하고 인자로 __name__ 을 입력합니다. 
# 만약, 패키지를 사용하는 경우라면 일반적으로 패키지 이름으로 작성하는 것이 좋습니다.
# 때문에 인자로는 모듈이나 패키지의 이름을 넣습니다.
# 이는 플라스크(Flask)에서 템플릿이나 정적파일을 찾을 때 필요합니다.
app = Flask(__name__)

# route( ) 데코레이터를 사용해서 Flask에게 어떤 URL이 우리가 작성한 함수를 실행시키는지 알려줍니다.
# 즉, 생성한 객체의 route를 설정합니다. 이는 URL을 설정하는 것을 의미합니다.
@app.route('/')

# 그리고 함수를 생성하고 함수의 기능을 설명합니다.
# hello_world()는 사용자 브라우저에 보여줄 메시지를 리턴합니다.
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	app.run()

