from flask import Flask, render_template, request, jsonify
import atexit
import os
import json
from algorithm import fun_watson as algo

app = Flask(__name__, static_url_path='')

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/api', methods=['GET'])
def get_visitor():
    if client:
        return jsonify(list(map(lambda doc: doc['name'], db)))
    else:
        print('No database')
        return jsonify([])


@app.route('/api', methods=['POST'])
def run_algo():
    N = request.json['N_value']
    p = request.json['p_value']
    q = request.json['q_value']

    return jsonify(algo(int(float(N)),int(float(p)),int(float(q))))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
