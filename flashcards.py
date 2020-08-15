from flask import Flask, render_template
# from datetime import datetime

app = Flask(__name__)

@app.route("/")
def welcome():
    # return "Welcome to my Flash Cards application"
    return render_template(
        "welcome.html",
        message="Here a message from view",
        x=42
    )


# @app.route("/date")    
# def date():
#     return "This page was served at " + str(datetime.now())

# counter = 0

# @app.route("/count_views")
# def count_views():
#     global counter
#     counter += 1
#     return "This page was views " + str(counter) + " times"

