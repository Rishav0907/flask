from flask import Flask,render_template,redirect,session,flash,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app=Flask(__name__)

app.config['SECRET_KEY']='mysecret'

class infoForm(FlaskForm):
    stream_name=StringField("Whats your chosen stream?")
    submit=SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():
    form=infoForm()

    if form.validate_on_submit():
        session['stream_name']=form.stream_name.data
        flash(f"Your entered stream is {session['stream_name']}")
    
        return redirect(url_for('index'))
    
    return render_template('index.html',form=form)

if __name__=='__main__':
    app.run(debug=True)