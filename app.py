from flask import Flask, request
from os import environ

app = Flask(__name__)

def get_ip(request):
    if 'PROD' in environ:
        # Heroku routing layers masks the original IP, fetch it from the custom header
        # And make sure we just take the first IP in case other proxies were in the way
        ips = request.headers.get('X-Forwarded-For')
        return ips.split(',')[0]
    else:
        return request.remote_addr

@app.route('/')
def index():
    return get_ip(request)
