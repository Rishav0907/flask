from flask import Flask,render_template,session,url_for,redirect
from flask_wtf import FlaskForm
from wtforms import (
                    StringField,BooleanField,DateTimeField,
                    SubmitField,RadioField,SelectField,TextAreaField
                    )
from wtforms.validators import DataRequired                    

app=Flask(__name__)
app.config['SECRET_KEY']='my secret'

class infoForm(FlaskForm):
    #subject = StringField("what's your favourite subject?")
    operating_system=SelectField('What is your operating system :',
                                choices=[('Linux', 'Linux'),('Windows', 'Windows'),('Mac','Mac')])
    coding=BooleanField('Do you like programming?')
    laptop=RadioField('Which computerWhich brand laptop are you using',choices=[('Hp','Hp'),('Asus','Asus'),('Mac','Mac')])
    feedback=TextAreaField()
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():

    form=infoForm()

    if form.validate_on_submit():
        #session['subject'] = form.subject.data
        session['operating_system'] = form.operating_system.data
        session['coding']= form.coding.data
        session['laptop']= form.laptop.data
        session['feedback']= form.feedback.data

        return render_template('thankyou.html')

    return render_template('index.html',form=form)

if __name__=='__main__':
    app.run(debug=True)
