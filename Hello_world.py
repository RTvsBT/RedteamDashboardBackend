import flask, subprocess
from flask import request, jsonify
 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
attacks = [
    {'id': 0,
     'title': 'NMAP Scan',
     'response': 'Veel outpout'},
    {'id': 1,
     'title': 'Buffer overflow',
     'response': 'You got root access '},
    {'id': 2,
     'response': '1337 hack'}
]

#Home
# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Cyber Attacks</h1>
# <p>A prototype API for cyber attackzz.</p>'''


@app.route('/', methods=['GET'])
def home():
    cmd = ["python","main.py", "-d"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    print (out)
    return out


#Error 
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not found 404'}), 404


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/attacks/all', methods=['GET'])
def api_all():
    return jsonify(attacks)

@app.route('/api/v1/resources/attacks', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for attack in attacks:
        if attack['id'] == id:
            results.append(attack)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
