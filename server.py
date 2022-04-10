from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'i used to be an adventurer like you, until i took an arrow to the knee'

@app.route('/')
def main_form():
    session.clear()
    return render_template("index.html")

@app.route('/middleman', methods = ['POST'])
def monkey_in_the_middle():
    for key in request.form:
        session[key] = request.form[key]
    return redirect('/result')

@app.route('/result')
def form_result():
    return render_template("result.html", session = session)

if __name__ == "__main__":
    app.run(debug = True)