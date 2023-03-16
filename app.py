from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Retrieve data from API
    response = requests.get('https://manchester-airport-flights.netlify.app')
    data = response.json()


    # Render data in HTML template
    return render_template("index.html",data=data)

@app.route("/filter/<airline>")
def filtered(airline):
    print()
    # Example of data being rendered in html
    response = requests.get('https://manchester-airport-flights.netlify.app')
    data = response.json()

    filtered_data = []

    for i in data:
        if i['Airline'] == airline:
            filtered_data.append(i)


    return render_template("index.html", data=filtered_data)

if __name__ == "__main__":
    app.run()
