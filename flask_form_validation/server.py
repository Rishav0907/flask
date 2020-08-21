from flask import Flask,render_template
from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField

app=Flask(__name__)

app.config['SECRET_KEY'] ='mysecretkey'

class Infoform(FlaskForm):
    os_name =StringField('What is your operating system')
    #lang=StringField("What's your favourite programming language")
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    os_name=False
    form =Infoform()

    if form.validate_on_submit():
        os_name = form.os_name.data
        form.os_name.data=''

    return render_template('index.html',forms=form,os_name=os_name)




# @app.route('/',methods=['GET','POST'])
# def index():
#     os_name=False
#     #lang=False
#     form=Infoform()
#     if form.validate_on_submit():
#         os_name=form.os_name.data
#         #lang=form.lang.data
#         form.os_name.data=''
#         #form.lang.data=''
#         return '<h1>Welcome</h1>'

if __name__=='__main__':
    app.run(debug=True)


# <h1>Welcome to My Website</h1>

# <p>
#     {% if os_name %}
#         <h3>The os_name you entered is {{os_name}}</h3>
#     {% else %}
#         <h3>Some of your inputs are missing</h3>
#     {% endif %}    
# </p>

# <form method="POST">

#     {{ form.hidden_tag() }}
#     {{ form.os_name.label }} {{ form.os_name() }}
#     {{ form.submit() }}

# </form>