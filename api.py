import flask
import json
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])
def home():
    #return html file with flask
    return flask.render_template('index.html')


@app.route('/api', methods=['GET'])
def api_single():
    with open('list.json', encoding='utf8') as json_file:
        data = json.load(json_file)
    random_thing=data[random.choice(list(data))]
    return json.dumps(random_thing, ensure_ascii=False)

@app.route('/api/all', methods=['GET'])
def api_all():
    with open('list.json', encoding='utf8') as json_file:
        data = json.load(json_file)
    return json.dumps(data, ensure_ascii=False)

@app.errorhandler(404)
def page_not_found(x):
    return flask.render_template('404.html'), 404


app.run(host="127.0.0.1")