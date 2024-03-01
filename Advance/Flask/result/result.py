
from flask import Flask , redirect , url_for, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    tot=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        tot=(science+maths+c+datascience)/4
    return redirect(url_for('success',score=tot))

@app.route('/success/<int:score>')
def success(score):
     res=''
     if score >=50:
          res ='pass'
     else:
          res ='fail'
          
     return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
     return 'person has failed and score is' + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks <50:
       result = 'fail'
    else:
       result ='pass'
    return redirect(url_for(result,score=marks))


if __name__ == "__main__":
     app.run()
