from flask import Flask,redirect, url_for, render_template

app=Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The result is passed</h1></body></html>"
@app.route('/fail/<int:score>')
def fail(score):
    return "<html><body><h1>The result is failed</h1></body></html>"
@app.route('/results/<int:score>')
def results(score):
    result=''
    if score<35:
        result='fail'
    else:
        result='pass'
    return result



if __name__=="__main__":
    app.run(debug=True)