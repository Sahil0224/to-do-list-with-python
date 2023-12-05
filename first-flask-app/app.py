from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def Login():
    return render_template("login.html")

@app.route('/index')
def index():
    return render_template("index.html")

app.run(debug=True)