import json
from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hell world'


@app.route('/testJson', methods=['POST'])
def testJson():
    data = json.loads(request.form.get('data'))
    lesson = data['lesson']
    score = data['score']
    info = dict()
    info['name'] = 'testuser'
    info['lesson'] = lesson
    info['score'] = score
    return jsonify(info)


@app.route('/testJson1', methods=['POST'])
def testJson1():
    data = json.loads(request.get_data())
    lesson = data['lesson']
    score = data['score']
    info = dict()
    info['name'] = 'testuser'
    info['lesson'] = lesson
    info['score'] = score
    return jsonify(info)

if __name__ == '__main__':
    '''
    host='0.0.0.0'
    app.run(debug=True)
    '''
    app.run(host='0.0.0.0',debug=True)
