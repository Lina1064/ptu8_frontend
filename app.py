from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/destytojas/')
def destytojas():
    return render_template("destytojas.html")

@app.route('/lina/')
def lina():
    return render_template("lina.html")


if __name__ == "__main__":
    app.run(debug=True)
