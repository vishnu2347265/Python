from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
class RegistrationForm(FlaskForm):
username = StringField('Username')
password = PasswordField('Password')
submit = SubmitField('Register')
@app.route('/', methods=['GET', 'POST'])
def register():
form = RegistrationForm()
if form.validate_on_submit():
# Process the form data (e.g., save to database)
return f"Registration successful for {form.username.data}!"
return render_template('register.html', form=form)
if __name__ == '__main__':
app.run(debug=True)