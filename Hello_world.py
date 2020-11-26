import flask, subprocess
from flask import request, jsonify
 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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

# Return the possible atacks 
@app.route('/api/v1/resources/attacks/all', methods=['GET'])
def api_all():
    cmd = ["python3","main.py", "-l"]
    return jsonify(command="list", consoleCommand='python3 main.py -l', output=command_runner(cmd))

# Runs GetHostname attack
@app.route('/api/v1/resources/attacks/gethostname', methods=['GET'])
def api_gethostname():
    cmd = ["python3","main.py", "-p", "GetHostname"]
    return jsonify(command="gethostname", consoleCommand='python3 main.py -p GetHostname',  output=command_runner(cmd))

#Error 
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not found 404'}), 404

app.run(host='0.0.0.0')
