from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')


        if username == 'admin' and password == 'admin':
            return redirect(url_for('admin'))
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render_template('Login.html', error_message=error_message)

    return render_template('Login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
