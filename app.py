from flask import Flask, request
import sys

app = Flask(__name__)

@app.route('/', defaults={'p': ''}, methods=['GET','POST','PUT','DELETE','HEAD'])
@app.route('/<path:p>', methods=['GET','POST','PUT','DELETE','HEAD'])
def log(p):
    print('REQ', request.method, request.full_path, flush=True)
    print('HDR', dict(request.headers), flush=True)
    print('BODY', request.get_data(as_text=True)[:2000], flush=True)
    return '{}', 200, {'Content-Type': 'application/json'}
