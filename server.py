from flask import Flask, request, jsonify
from subprocess import check_output
import json

app = Flask(__name__)


def handle_dispatch(calls=None):

    results = []

    for call in calls:

        print(call)

        if call['lang'] == 'python':

            results.append(('python', check_output('python python_handler.py \'[{}]\''.format(json.dumps(call)), shell=True).decode("utf-8")))

        elif call['lang'] == 'node':

            results.append(('node', check_output('node \'{}\'.js \'{}\''.format(call['function'], call['args']), shell=True).decode("utf-8")))

    return results


@app.route('/fn', methods=['GET', 'POST'])
def dispatch():

    return jsonify(handle_dispatch(request.json))


if __name__ == '__main__':

    app.run(host='127.0.0.1', debug=True)
