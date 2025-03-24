from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("sample.html")

@app.route("/consultation")
def consult():
    return render_template("consultation.html")

if __name__ == "__main__":
    app.run(debug=True)