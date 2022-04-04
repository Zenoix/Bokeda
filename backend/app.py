from flask import Flask, request
from flask_restful import Resource, Api

import data_handling

app = Flask(__name__)
api = Api(app)

file_paths = "hello"


class DataCollection(Resource):
    def get(self):
        return file_paths

    def put(self):
        file_paths = request.json
        return file_paths


api.add_resource(DataCollection, '/data')


if __name__ == '__main__':
    app.run(debug=True)
