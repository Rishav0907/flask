from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/form/check')
def check():
    username=request.args.get('username')
    upper=False
    lower=False
    result=True
    print(username)
    for letter in username:
        print(letter)
        if letter==letter.isupper():
            upper=True
            print(upper)
            break
        if letter==letter.islower():
            lower=True
            break
    result=upper and lower
    return render_template('check.html',result=result,username=username)
if __name__=='__main__':
    app.run(debug=True)
    # upper=False
    # lower=False
    # result=False

    # lower=any(c.islower() for c in username)
    # capital=any(c.isupper() for c in username)

    # result=lower and capital