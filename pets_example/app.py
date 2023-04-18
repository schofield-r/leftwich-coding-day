from flask import Flask, render_template


app = Flask(__name__)

data = [{"user": "Alex", "pets_name": "Fish", "animal": "fish"}, {
    "user": "Faz", "pets_name": "Kitty", "animal": "cat"}, {"user": "Rhiannon", "pets_name": "Rosie", "animal": "dog"}]


@app.route("/")
def index():

    return render_template("index.html", data=data)


@app.route("/filter/<animal>")
def filtered_pets(animal):

    filtered_data = []

    for i in data:
        if i['animal'] == animal:
            filtered_data.append(i)

    return render_template("index.html", data=filtered_data)


if __name__ == "__main__":
    app.run()
