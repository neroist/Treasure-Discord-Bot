from flask import Flask
from flask import render_template_string
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return '''<html><head><title>500 Internal Server Error</title>
</head><body data-new-gr-c-s-check-loaded="14.998.0" data-gr-ext-installed=""><h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
</body></html>'''

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
    