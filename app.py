from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
  # Your code for fetching the data goes here
    data={{user:'Alex', PetsName:'Fish'}, {user:'Faz', PetsName:'Kitty'}, {user:'Rhiannon', PetsName:'Rosie'}}
    # Renders the html and can insert the data with a second argument 'data='
    return render_template("index.html", data=data)
if __name__ == "__main__":
    app.run()
