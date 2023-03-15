from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
  # Your code for fetching the data goes here
  
    # Renders the html and can insert the data with a second argument 'data='
    return render_template("index.html")
if __name__ == "__main__":
    app.run()
