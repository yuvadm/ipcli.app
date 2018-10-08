from flask import Flask, request
from os import environ

app = Flask(__name__)

def get_ip(request):
    if 'PROD' in environ:
        return request.headers.get('X-Forwarded-For')
    else:
        return request.remote_addr

@app.route('/')
def index():
    return get_ip(request)
