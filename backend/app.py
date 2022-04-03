from flask import Flask, request
from flask_restful import Resource, Api

import data_handling

app = Flask(__name__)
api = Api(app)


class DataCollection(Resource):
    def put(self):
        file_paths = request.json
        return file_paths


api.add_resource(DataCollection, '/data')


if __name__ == '__main__':
    app.run(debug=True)
