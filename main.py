from flask import Flask
from flask_restful import Api, Resource
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

app = Flask(__name__)
api = Api(app)


# =========================
# MongoDB
# =========================

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(
    mongo_uri,
    server_api=ServerApi("1")
)

db = client["sample_mflix"]
tes1_collection = db["movies"]


# =========================
# Client Resource
# =========================

class Tes1(Resource):

    def get(self):
        data = []

        for document in tes1_collection.find():
            data.append({
                "id": str(document["_id"]),
                "name": document.get("title")
            })

        return data, 200


api.add_resource(Tes1, "/tes1")


if __name__ == "__main__":
    app.run(debug=True)