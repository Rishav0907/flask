from flask import Flask,render_template,session,url_for,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,PasswordField,validators,SubmitField
from flask_mysqldb import MySQL
from hashlib import sha256

app =   Flask(__name__)

app.config['SECRET_KEY']    =   'I am Rishav'
app.config['MYSQL_HOST']    =   'localhost'
app.config['MYSQL_USER']    =   'root'
app.config['MYSQL_PASSWORD']=   '89018901'
app.config['MYSQL_DB']      =   'flask_auth'

mysql=MySQL(app)

class InfoForm(FlaskForm):
    email       =   StringField('Email',[validators.DataRequired()])
    username    =   StringField('Username',[validators.length(min=4,max=10)])
    first_name  =   StringField('First Name',[validators.DataRequired()])
    last_name   =   StringField('Last Name',[validators.DataRequired()])
    Password    =   PasswordField('Password',[validators.DataRequired()])
    submit      =   SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form=InfoForm()
    email=form.email.data
    username=form.username.data
    first_name=form.first_name.data
    last_name=form.last_name.data
    password=form.Password.data
    hashed_password=sha256(bytes(str(password),encoding='ascii')).hexdigest()
    if form.validate_on_submit():
        session['email']        =   form.email.data
        session['first_name']   =   form.first_name.data
        session['last_name']    =   form.last_name.data

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO  users (email, username, first_name, last_name, password) VALUES(%s,%s,%s,%s,%s)",(email,username,first_name,last_name,hashed_password))
        mysql.connection.commit()
        cur.close()
        return render_template('thankyou.html')
    return render_template('index.html',form=form)



if __name__=='__main__':
    app.run(debug=True)