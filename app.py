## Flask App Routing

from flask import Flask,render_template,request,redirect,url_for

## create a simple flask application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>Welcome to the app</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h2>Welcome to the Index Page</h2>"

## Variable rule
@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the score is:"+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the score is:"+ str(score)

@ app.route('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        res=""
        if average_marks>=50:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res,score=average_marks))

        #return render_template('form.html',score=average_marks)


if __name__ =="__main__":
    app.run(debug=True)