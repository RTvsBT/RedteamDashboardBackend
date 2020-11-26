import flask, subprocess
from flask import request, jsonify
 
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Home
# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Cyber Attacks</h1>
# <p>A prototype API for cyber attackzz.</p>'''


@app.route('/', methods=['GET'])
def home():
    cmd = ["python3","main.py", "-l"]
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


@app.route('/api/v1/resources/attacks/all', methods=['GET'])
def api_all():
    cmd = ["python3","main.py", "-l"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    out = out.decode()
    return jsonify(command="list", consoleCommand='python3 main.py -l', output=out)

app.run()
