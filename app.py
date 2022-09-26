from flask import Flask, Blueprint, render_template, jsonify, request # Flask 서버 객체 import
from app_devday import devday
from app_user import user
from app_mydev import mydev

# port
port = 8899

# Flask로 app 객체 선언 및 blueprint로 개별 파일 연동
app = Flask(__name__)
app.register_blueprint(devday)
app.register_blueprint(user)
app.register_blueprint(mydev)


# 404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('DevDay/404.html'), 404

# 서버 시작
if __name__ == '__main__':
    app.run('0.0.0.0', port=port, debug=True)