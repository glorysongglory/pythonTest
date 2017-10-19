from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hell world'


if __name__ == '__main__':
    '''
    host='0.0.0.0' 对外网开放
    app.run(debug=True) 开启调试,自动加载
    '''
    app.run(host='0.0.0.0')
