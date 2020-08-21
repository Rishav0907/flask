from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    my_name='Rishav'
    my_list=[1,2,3,4,7]
    return render_template('basic.html',my_list=my_list)

if __name__=='__main__':
    app.run(debug=True)