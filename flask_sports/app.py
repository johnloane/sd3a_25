from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from dotenv import load_dotenv, find_dotenv
import os

SPORTS = ["Karate", "Football", "Basketball"]

app = Flask(__name__)

_ = load_dotenv(find_dotenv())

app.config['MYSQL_HOST'] = os.environ.get("MYSQL_HOST")
app.config['MYSQL_USER'] = os.environ.get("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("MYSQL_DB")

mysql = MySQL(app)

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
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT into registrant(name, sport) values (%s, %s )", (name, sport))
    mysql.connection.commit()
    
    cursor.execute("select * from registrant")
    rv = cursor.fetchall()
    cursor.close()
    return render_template("registrants.html", registrants = rv )


@app.route("/deregister", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        cursor = mysql.connection.cursor()
        cursor.execute("delete from registrant where id = %s", (id,))
        mysql.connection.commit()
        cursor.execute("select * from registrant")
        rv = cursor.fetchall()
        cursor.close()
        return render_template("registrants.html", registrants = rv )

