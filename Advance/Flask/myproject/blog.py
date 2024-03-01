from flask import Flask , redirect , url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello():
        return 'Hi'

def about():
    return ' about page '
app.add_url_rule("/about","about",about)


@app.route('/admin')
def hello_admin():
      return 'Welcome Admin'

#To Display via DataTypes

@app.route('/blog/<int:postID>')
def show_blog(postID):
      return 'Blog Number %d' % postID

@app.route('/guest/<guest>')
def hello_guest(guest):
      return 'Hello %s as Guest' % guest

@app.route('/rev/<float:revNo>')
def revision(revNo):
      return 'Revision Number %f' % revNo


@app.route('/user/<name>')
def hello_user(name):
      if name=='admin':
            return redirect(url_for('hello_admin'))
      else :
            return redirect(url_for('hello_guest',guest = name))
      



@app.route('/index')
def show_index():
      return render_template("index.html")

@app.route('/submit')
def show_submit():
      return render_template("result.html")


if __name__ == "__main__":
     app.run()


