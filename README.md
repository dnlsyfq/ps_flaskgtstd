
```
pip freeze > requirements.txt
```

```
//mac
export FLASK_APP=flashcards.py
export FLASK_ENV=development
flask run

//windows
set FLASK_APP=flashcards.py
set FLASK_ENV=development
$env:FLASK_APP="flashcards.py"
flask run
```


### FLask Map

```
>> import flashcards
>> flashcards.app.url_map
```
