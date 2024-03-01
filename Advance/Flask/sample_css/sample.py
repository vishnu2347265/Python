from flask import Flask , redirect , url_for, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('impcss.html')

@app.route('/page')
def nextpage():
     courses=['c','python']
     return render_template('page2.html',courses=courses)

if __name__ == "__main__":
     app.run(debug=True)
