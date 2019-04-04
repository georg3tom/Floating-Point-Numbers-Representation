from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
@app.route("/introduction")
def hello():
    return render_template("introduction.html")

if __name__ == "__main__":
    app.run(debug=True)
