from flask import Flask, request
import json

app = Flask(__name__)

data_buffer = []


@app.route('/<path:dest_path>', methods=['POST'])
def handle_post_all(dest_path):
    global data_buffer
    echo(dest_path, request)
    data_buffer.append(json.loads(request.data))
    return '', 200


@app.route('/dump', methods=['GET'])
def dump_data():
    global data_buffer
    return json.dumps(data_buffer), 200


def echo(path, req):
    print(request.data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
