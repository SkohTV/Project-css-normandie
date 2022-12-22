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


@app.route('/incontournables')
def lieux():
    return render_template("incontournables.html")


@app.route('/credits')
def credits():
    return render_template("credits.html")


@app.route('/lieux/mont-st-michel')
def lieu1():
    return render_template("lieux/mont-st-michel.html")

@app.route('/lieux/chateau-de-caen')
def lieu2():
    return render_template("lieux/chateau-de-caen.html")

@app.route('/lieux/abbaye-aux-hommes')
def lieu3():
    return render_template("lieux/abbaye-aux-hommes.html")

@app.route('/lieux/plages-du-debarquement')
def lieu4():
    return render_template("lieux/plages-du-debarquement.html")

if __name__ == "__main__":
    app.run(debug=True ,port=8080,use_reloader=False)