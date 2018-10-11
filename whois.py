from subprocess import run

def extract_field(field, response):
    for line in response:
        if line.startswith(field):
            return line.split('    ')[-1].strip()
    
def whois(ip):
    cp = run(['whois', ip], capture_output=True)
    lines = cp.stdout.decode().split('\n')
    fields = ['route', 'origin', 'descr']
    res = {f: extract_field(f, lines) for f in fields}
    return res
