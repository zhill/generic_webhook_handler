from flask import Flask, request
import json

app = Flask(__name__)

data_buffer = []

@app.route('/', methods=['POST', 'GET'])
def handle_base():
    return add_data('/', request), 200

@app.route('/<path:dest_path>', methods=['GET'])
def handle_non_post(dest_path):
    return 'ok', 200

@app.route('/<path:dest_path>', methods=['POST'])
def handle_post_all(dest_path):
    return add_data(dest_path, request), 200

def add_data(dest_path, request):
    global data_buffer
    echo(dest_path, request)
    if request.content_type == 'application/json':
        data_buffer.append(json.loads(request.data))
    else:
        data_buffer.append(str(request.data))
    return 'ok'


@app.route('/dump', methods=['GET'])
def dump_data():
    global data_buffer
    return json.dumps(data_buffer), 200


def echo(path, req):
    print(request.data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
