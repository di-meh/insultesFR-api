import flask
import json
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<meta charset='UTF-8'><h1>API d'insultes françaises</h1><p>Fais pas chier maintenant.</p>"


@app.route('/api', methods=['GET'])
def api_all():
    with open('list.json', encoding='utf8') as json_file:
        data = json.load(json_file)
    random_thing=data[random.choice(list(data))]
    return json.dumps(random_thing, ensure_ascii=False)


@app.errorhandler(404)
def page_not_found(aaa):
    return '<meta charset="UTF-8"><h1>404</h1><p>Eh oui connard faut savoir écrire</p>', 404


app.run(host="127.0.0.1")