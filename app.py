from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/year")
def year():
    return render_template("year.html")

@app.route("/ECE")
def ECE():
    return render_template("ECE.html")

@app.route("/CSE")
def CSE():
    return render_template("CSE.html")

@app.route("/IT")
def IT():
    return render_template("IT.html")

@app.route("/EEE")
def EEE():
    return render_template("EEE.html")

@app.route("/CIVIL")
def CIVIL():
    return render_template("CIVIL.html")

@app.route("/MECHANICAL")
def MECHANICAL():
    return render_template("MECHANICAL.html")

if __name__ == "__main__":
    app.run(debug=True)