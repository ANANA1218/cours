from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.form['data']
    result = eval(data)
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
