import flask, subprocess, markupsafe 
from flask import request, jsonify, escape
from flask_cors import CORS
 
app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

attacks = ["DDOS","SQLI","RANSOMWARE","NMAP","BRUTEFORCE"]


def command_runner(cmd):
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    out = out.decode()
    return out

@app.route('/', methods=['GET'])
def home():
    cmd = ["python3","main.py", "-d"]
    print(command_runner(cmd)) 
    return jsonify(command="list", output=command_runner(cmd))

# Default route
@app.route('/<attack>/<host>')
def attackRouter(attack, host="192.168.2.35"):
    cmd = ["python3","main.py", "-p", attack, "--host", host]
    return jsonify(command=attack, consoleCommand=f'python3 main.py -p {attack} --host {host}',  output=command_runner(cmd))

#Error 
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not found 404'}), 404
if __name__ == "__main__":
    app.run(host='0.0.0.0')
