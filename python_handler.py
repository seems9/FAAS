import imp
import json
import sys

configs = json.loads(sys.argv[1])


def load_python(func=None):

    return imp.load_source('external_function', '{}.py'.format(func))


calls = [(getattr(load_python(c['function']), c['function']), c['args']) for c in configs]

results = [call[0](*call[1]) for call in calls]

sys.stdout.write(str(results))
sys.stdout.flush()
