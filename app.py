import flask

app = flask.Flask(__name__)
@app.route('/')
def main():
    return "<p>Hello World from Nicholas McGonigle<p>"