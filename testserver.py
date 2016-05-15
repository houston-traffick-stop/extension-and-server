from flask import Flask, request
from analyze import analyzeText

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello World</p>"

@app.route('/submit', methods = ['GET','POST'])
def submission():
    info = []
    if request.method == 'POST':
        data = request.form['url']
        information = analyzeText(data)
        return str(information)
    return "Hi."

if __name__ == "__main__":
    app.run()
