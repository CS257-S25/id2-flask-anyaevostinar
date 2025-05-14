'''Replace me with your flask app'''


from flask import Flask
from ProductionCode.core import get_column_names, get_pokemon_by_stat, get_pokemon_by_name

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Pokemon API!"

@app.route('/column_names')
def column_names():
    return get_column_names()

@app.route('/pokemon_by_name/<name>')
def pokemon_by_name(name):
    return get_pokemon_by_name(name)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development