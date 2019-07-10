import markdown
import shelve
import os

from flask import Flask, g, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    with open (os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read();
    return markdown.markdown(content)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

class DeviceList(Resource):

    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])

        return{'message': 'Success', 'data': devices}, 200

    def post(self):
        json_data = request.get_json(force=True)

        shelf = get_db()
        shelf[json_data['identifier']] = json_data

        return {'message': 'Device registered', 'data': json_data}, 201

class Device(Resource):
    def get(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message': 'Device not found', 'data': {}}, 404

        return {'message': 'Devices found', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in shelf):
            return {'message': 'Device not found', 'data': {}}, 404

        del shelf[identifier]
        return '', 204

api.add_resource(DeviceList, '/devices')
api.add_resource(Device, '/device/<string:identifier>')
