from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class DataCollection(Resource):
    def put(self):
        file_paths = request.json
        print(f"Python received: {file_paths}")
        return file_paths


api.add_resource(DataCollection, '/data')


if __name__ == '__main__':
    print("test")
    app.run(debug=True)
