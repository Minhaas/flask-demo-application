from flask import Flask, render_template

mi = Flask(__name__)

@mi.route('/')
def home():
    return render_template("index.html")

@mi.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    mi.run()
