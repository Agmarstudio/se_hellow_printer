from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request # noqa

msg = "Hello World!"
moje_imie = "Marcin"


@app.route('/')
def index():
    output = request.args.get('output')
    name = request.args.get('name')
    if not output:
        output = PLAIN
    if not name:
        name = moje_imie
    return get_formatted(msg, name,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
