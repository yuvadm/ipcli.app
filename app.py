from flask import Flask, request
from os import environ
from whois import whois

app = Flask(__name__)

env = 'PROD' if 'PROD' in environ else 'DEV'

TEMPLATE = '''
/----------------------------------------\\
| {ip:39}|
|                                        |
| {route:39}|
| {origin:39}|
| {descr:39}|
|                                        |
| Created by Yuval Adam                  |
| https://github.com/yuvadm/ipcli.app    |
| Comments welcome at hello@ipcli.app    |
\\----------------------------------------/
'''

def get_ip(request):
    FOWARDED_FOR_HEADER = 'X-Forwarded-For'
    if FOWARDED_FOR_HEADER in request.headers:
        # Routing layers and proxies along the way might mask the original IP
        # So fetch it from the custom header
        # And make sure we just take the first (source) IP address
        ips = request.headers.get(FOWARDED_FOR_HEADER)
        return ips.split(',')[0]
    return request.remote_addr

@app.route('/')
def index():
    ip = get_ip(request)
    w = whois(ip)
    return TEMPLATE.format(ip=ip, route=w['route'], origin=w['origin'], descr=w['descr'])

@app.route('/p')
def plain():
    return get_ip(request)
