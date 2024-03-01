from flask import Flask , redirect , url_for, render_template,request,flash
app = Flask(__name__)
app.secret_key='random_string'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form["username"] != "admin" or \
            request.form["password"] != "admin":
            error="Invalid Credentials. Please try again."
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template("login.html",error=error)

if __name__ == "__main__":
    app.run(debug=True)

