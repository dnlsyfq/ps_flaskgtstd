
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

### Model-Template-View components
MVC vs MTv

#### Jinja templates 

```
<html>
    <head>
        <title>{{name}} 's Page </title>
    </head>
    <body>
        <h1>{{name}}</h1>
    </body>

</html>
```

#### Calling a template from view

```
from flask import render_template
def welcome():
    return render_template(
        "welcome.html",
        name="Bob",
        age=35
    )
```

```
pip3 install -r requirements.txt
sudo apt install gunicorn3
gunicorn3 -D flashcards:app
CD /etc/nginx/sites-available
rm default

default 
copy paste gunicorn
sudo service nginx restart

```