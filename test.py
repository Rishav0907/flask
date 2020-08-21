from flask import Flask

app=Flask(__name__)

@app.route('/')
def root():
    return '<h1>Welcome</h1>'


@app.route('/user/<name>')
def puppy(name):
    if name[-1]=='y':
        return name[:-1] +'iful'
    elif name[-1]!='y':
        return name[:-1]+'y'

if __name__=='__main__':
    app.run(debug=True)