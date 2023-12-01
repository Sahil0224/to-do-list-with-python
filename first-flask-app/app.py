from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Hello():
    return render_template("index.html")

@app.route("/hello")
def NewRoute():
    return "Hello World"

@app.route('/html')
def html_response():
    return """
            <html>
            <p>Hello World Text</p>
            </html>
            """
app.run(debug=True)