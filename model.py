import json

def load_db():
    with open("flashcards_db.json",errors='ignore') as f:
        return json.load(f)
    
db = load_db()    