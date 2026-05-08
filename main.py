from flask import Flask, render_template

app = Flask(__name__)  # Use double underscores here

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":  # Use double underscores for both name and main
    app.run(debug=True)