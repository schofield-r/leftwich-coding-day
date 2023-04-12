import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    # Your code for fetching the API data goes here
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()
