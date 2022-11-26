from flask import Flask,render_template,jsonify,json, request
from app import get_title, get_release_year, get_rating_children,get_rating_adult,get_rating_family,get_genre
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_PRETTYPRINT_REGULAR'] = True


@app.route('/movie/<title>')
def movie(title):
    data = get_title(title)
    return jsonify(data)


@app.route('/movie')
def film():
    from_value = request.args.get('from')
    to_value = request.args.get('to')
    data = get_release_year(from_value, to_value)
    return jsonify(data)


@app.route('/rating/children')
def children():
    data = get_rating_children()
    return data


@app.route('/rating/family')
def family():
    data = get_rating_family()
    return data


@app.route('/rating/adult')
def adult():
    data = get_rating_adult()
    return data

@app.route('/genre/<genre>')
def get_genre_up(genre):
    data = get_genre(genre)
    return jsonify(data)

app.run()