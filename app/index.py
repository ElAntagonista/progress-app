from flask import Flask, render_template
import os


name = os.getenv("NAME")

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
