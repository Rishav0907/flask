from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome</h1>'

@app.route('/users/<name>')
def user(name):
    return f"This page is for {name.upper()}"

if __name__=='__main__':
    app.run()