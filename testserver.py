from flask import Flask, request
import urllib
import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello World</p>"

@app.route('/submit', methods = ['GET','POST'])
def submission():
    info = []
    if request.method == 'POST':
        data = request.form['url']
        information = urllib.urlopen(data).read()
        soup = BeautifulSoup.BeautifulSoup(information)
        return str(soup.findAll('p'))
    return "Hi."

if __name__ == "__main__":
    app.run()
