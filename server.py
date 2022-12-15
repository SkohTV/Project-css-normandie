from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def accueil():
	return render_template("accueil.html")
@app.route('/accueil')
def accueilR1():
    return redirect("/")

@app.route('/histoire')
def histoire():
    return render_template("histoire.html")

@app.route('/lieux')
def lieux():
    return render_template("lieux.html")

@app.route('/lieux/1')
def lieu1():
    return render_template("lieux/1.html")
@app.route('/lieux/2')
def lieu2():
    return render_template("lieux/2.html")
@app.route('/lieux/3')
def lieu3():
    return render_template("lieux/3.html")
@app.route('/lieux/4')
def lieu4():
    return render_template("lieux/4.html")

if __name__ == "__main__":
    app.run(debug=True ,port=8080,use_reloader=False)