from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

app = Flask(__name__)


#@app.route("/")
"""def hello_world():
    return '<Hello World>'"""


@app.route("/")
def index():
    return '<a href="/calc">calc</a>'

"""def do_get():
    return '''<form method="POST" action="/calc"><input name="a"><input name="b"><input type="submit" value="Compute"></form>'''"""



@app.route("/calc",methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return '''<form method="POST" action="/calc"><input name="a"><input name="b"><input type="submit" value="Compute"></form>'''
    
    elif request.method== "POST":
        a=request.form["a"]
        b=request.form["b"]

        return str(int(a)+ int(b))
        






if __name__ == '__main__':
    app.run()

