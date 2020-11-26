import flask, subprocess
from flask import request, jsonify
 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    cmd = ["python3","main.py", "-d"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    out = out.decode()
    print(out) 
    return jsonify(command="list", output=out)

#Error 
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not found 404'}), 404


# Return the possible atacks 
@app.route('/api/v1/resources/attacks/all', methods=['GET'])
def api_all():
    cmd = ["python3","main.py", "-l"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    out = out.decode()
    return jsonify(command="list", consoleCommand='python3 main.py -l', output=out)

# Runs GetHostname attack
@app.route('/api/v1/resources/attacks/gethostname', methods=['GET'])
def api_gethostname():
    cmd = ["python3","main.py", "-p", "GetHostname"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    out = out.decode()
    return jsonify(command="gethostname", consoleCommand='python3 main.py -p GetHostname', output=out)

    
app.run()
