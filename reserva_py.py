
from flask import Flask

app = Flask(__name__)


@app.route('/')
def reserva_py():
    return 'App para el Comedor Universitario UNFV'
