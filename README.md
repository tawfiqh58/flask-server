# Flask App

My first flask app

You have to manually create this application using python3

Step:

```shell
mkdir myproject
cd myproject
python3 -m venv .venv

. .venv/bin/activate

pip install Flask

```

Note: You have to have python or python3 and pip or pip3 installed  

Then you have to create `server.py` file  
and import `Flask`

`@app.route("/")` is a decorator to create API

That's it!

Run this app  
$ . .venv/bin/activate
$ flask --app server run

Debug ON  
$ flask --app main.py --debug run

Note: Flask will automatically reload you app.
