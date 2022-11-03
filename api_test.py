from bottle import route, response, abort, request
from utils import *
 
 
@route('/api/item', method=['GET', 'POST'])
def handle_item():
    try:
        response.headers['Content-Type'] = 'application/json'
        if request.method == 'GET':
            return get_items()
        else:
            return create_item(key=request.query.key, payload=request.body)
    except:
        # internal server error
        abort(500)
 
 
@route('/api/item/<item_id>', method=['PUT', 'DELETE'])
def modify_item(item_id):
    try:
        response.headers['Content-Type'] = 'application/json'
        if request.method == 'PUT':
            return create_item(item_id, request.body, False)
        else:
            # not implemented
            abort(501)
    except:
        abort(500)