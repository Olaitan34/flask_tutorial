from flask import Flask, jsonify, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "hello World"

@app.route("/about")
def about():
    date = datetime.datetime.now()
    return jsonify({
        "key" : "value",
        "number": 12,
        "date": date
        })

@app.route("/contact")
def contact():
    
    return render_template("contact.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 3000, debug=True)