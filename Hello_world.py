import flask, subprocess, markupsafe 
from flask import request, jsonify, escape
from flask_cors import CORS
 
app = flask.Flask(__name__)
CORS(app)
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

# Return the possible attacks 
@app.route('/api/v1/resources/attacks/all', methods=['GET'])
def api_all():
    cmd = ["python3","main.py", "-l"]
    return jsonify(command="list", consoleCommand='python3 main.py -l', output=command_runner(cmd))

# Runs GetHostname attack
@app.route('/api/v1/resources/attacks/gethostname', methods=['GET'])
def api_gethostname():
    cmd = ["python3","main.py", "-p", "GetHostname"]
    return jsonify(command="gethostname", consoleCommand='python3 main.py -p GetHostname',  output=command_runner(cmd))


# With parameter

# NIDS
# NIDS_Mock1
@app.route('/api/v1/resources/attacks/NIDS_Mock1/<host>')
def api_nids1_attack(host):
    # return 'User %s' % escape(username)
    cmd = ["python3","main.py", "-p", "NIDS_Mock1", "--host", host]
    print(cmd)
    return jsonify(command="NIDS_Mock1", consoleCommand='python3 main.py -p NIDS_Mock1 --host 192.168.XXX.XXX',  output=command_runner(cmd))

# NIDS_Mock2
@app.route('/api/v1/resources/attacks/NIDS_Mock2/<host>')
def api_nids2_attack(host):
    # return 'User %s' % escape(username)
    cmd = ["python3","main.py", "-p", "NIDS_Mock2", "--host", host]
    print(cmd)
    return jsonify(command="NIDS_Mock2", consoleCommand='python3 main.py -p NIDS_Mock2 --host 192.168.XXX.XXX',  output=command_runner(cmd))

# NIDS_Mock3
@app.route('/api/v1/resources/attacks/NIDS_Mock3/<host>')
def api_nids3_attack(host):
    # return 'User %s' % escape(username)
    cmd = ["python3","main.py", "-p", "NIDS_Mock3", "--host", host]
    print(cmd)
    return jsonify(command="NIDS_Mock1", consoleCommand='python3 main.py -p NIDS_Mock3 --host 192.168.XXX.XXX',  output=command_runner(cmd))


# HIDS
# HIDS_Mock1
@app.route('/api/v1/resources/attacks/HIDS_Mock1/<host>')
def api_hids1_attack(host):
    # return 'User %s' % escape(username)
    cmd = ["python3","main.py", "-p", "HIDS_Mock1", "--host", host]
    print(cmd)
    return jsonify(command="HIDS_Mock1", consoleCommand='python3 main.py -p HIDS_Mock1 --host 192.168.XXX.XXX',  output=command_runner(cmd))

# HIDS_Mock2
@app.route('/api/v1/resources/attacks/HIDS_Mock2/<host>')
def api_hids2_attack(host):
    # return 'User %s' % escape(username)
    cmd = ["python3","main.py", "-p", "HIDS_Mock2", "--host", host]
    print(cmd)
    return jsonify(command="HIDS_Mock2", consoleCommand='python3 main.py -p HIDS_Mock2 --host 192.168.XXX.XXX',  output=command_runner(cmd))

# HIDS_Mock3
@app.route('/api/v1/resources/attacks/HIDS_Mock3/<host>')
def api_hids3_attack(host):
    # return 'User %s' % escape(username)
    cmd = ["python3","main.py", "-p", "HIDS_Mock3", "--host", host]
    print(cmd)
    return jsonify(command="HIDS_Mock3", consoleCommand='python3 main.py -p HIDS_Mock3 --host 192.168.XXX.XXX',  output=command_runner(cmd))

#Error 
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not found 404'}), 404

app.run(host='0.0.0.0')
