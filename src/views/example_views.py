
from flask import request, Blueprint, jsonify

example_api = Blueprint('example_api', __name__)

# register your endpoints here

@example_api.route('/', methods=['GET', 'POST'])
def endpoint():
    '''
    an example endpoint
    this blueprint is imported
    and registered in src/app_factory
    '''
    req_data = request.get_json()

    if request.method == 'GET':
        return jsonify({
            'status': 'success'
        }), 200

    if request.method == 'POST':
        return req_data, 200

