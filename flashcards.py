from flask import Flask, render_template,abort,jsonify
# from datetime import datetime
from model import db


app = Flask(__name__)

@app.route("/")
def welcome():
    # return "Welcome to my Flash Cards application"
    
    # return render_template(
    #     "welcome.html",
    #     message="Here a message from view",
    #     x=42
    # )

    return render_template(
        "welcome.html",
        cards = db
    )


# @app.route("/card")
# def card_view():
#     card = db[0]
#     return render_template(
#         "card.html",
#         card=card
#     )

@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html",
                               card=card,
                               index=index,
                               max_index=len(db)-1)
    except IndexError:
        abort(404)

@app.route('/add_card')
def add_card():
    return render_template('add_card.html')
    

# @app.route("/date")    
# def date():
#     return "This page was served at " + str(datetime.now())

# counter = 0

# @app.route("/count_views")
# def count_views():
#     global counter
#     counter += 1
#     return "This page was views " + str(counter) + " times"

@app.route('/api/card/')
def api_card_list():
    return jsonify(db) 

@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)
        
        