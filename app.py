from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "very_epic_secret_key300"  # super secret key


@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)
