import flask
import json
import random


app = flask.Flask(__name__)
app.config["DEBUG"] = False
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def home():
    return flask.render_template('index.html')


@app.errorhandler(404)
def page_not_found(x):
    return flask.render_template('404.html'), 404


@app.route('/api/random', methods=['GET'])
def api_single():
    with open('list.json', encoding='utf8') as json_file:
        data = json.load(json_file)

    random_thing=data[random.choice(list(data))]
    return flask.jsonify(insulte=random_thing)


@app.route('/api/all', methods=['GET'])
def api_all():
    with open('list.json', encoding='utf8') as json_file:
        data = json.load(json_file)

    return flask.jsonify(data)


@app.route('/api/id/<string:id>', methods=['GET'])
def api_id(id):
    with open('list.json', encoding='utf8') as json_file:
        data = json.load(json_file)

    if id not in data:
        return flask.jsonify({"error": "Not found"}), 404

    return flask.jsonify(insulte=data[id])


app.run(host="127.0.0.1")