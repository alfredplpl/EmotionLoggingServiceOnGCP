__author__ = "Alfred Increment"
__version__ = "0.0.1"
__license__ = "Apache License 2.0"

from flask import Flask, request
import main

app = Flask(__name__)

# ファイルを受け取る方法の指定
@app.route('/',methods=["GET","POST"])
def serve():
    return main.checkEmotion(request)


if __name__ == '__main__':
    app.run('127.0.0.1', 8000, debug=True)

