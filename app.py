import json
from flask import Flask, render_template, send_file


app = Flask(__name__)


@app.route("/")
def index():

    # Your code for fetching the data goes here

    # Renders the html and can insert the data with a second argument 'data='
    return render_template("index.html")


@app.route("/pets")
def pets():
    # Example of data being rendered in html
    data_list = [{"user": "Alex", "pets_name": "Fish"}, {
        "user": "Faz", "pets_name": "Kitty"}, {"user": "Rhiannon", "pets_name": "Rosie"}]

    return render_template("petsExample.html", data=data_list)


if __name__ == "__main__":
    app.run()
