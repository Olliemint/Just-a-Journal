
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    message= '<h1>Hello world</h2>'
    
    return message