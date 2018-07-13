from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET', 'PUT', 'HEAD'])
def handle_base():
    echo('', request)
    return '', 200

@app.route('/<path:dest_path>', methods=['POST', 'GET', 'PUT', 'HEAD'])
def handle_all(dest_path):
    echo(dest_path, request)
    return '', 200

def echo(path, req):
    print('{} {}'.format(request.method, request.path))
    print('{}'.format(request.headers))
    print(request.data)

if __name__ == '__main__':
    app.run(port='8000')
