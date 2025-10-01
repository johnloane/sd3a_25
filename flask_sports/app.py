from flask import Flask, render_template, request, redirect

SPORTS = ["Karate", "Football", "Basketball"]

app = Flask(__name__)

REGISTRANTS = {}

@app.route("/")
def index():
    return render_template("index.html", sports = SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name: 
        return render_template("error.html", message = "Missing name") 
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message = "Missing Sport")
    if not sport in SPORTS:
        return render_template("error.html", message = "Invalid Sport")
    REGISTRANTS[name] = sport
    return render_template("registrants.html", registrants = REGISTRANTS)

