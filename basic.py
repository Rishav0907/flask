from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/land')
def landing():
    return '<h1>Welcome to Landing Page</h1>'
if __name__=='__main__':
    app.run()
