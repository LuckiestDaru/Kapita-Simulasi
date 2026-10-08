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

db = client["kapita"]
tes1 = db["tes1"]


# =========================
# Client Resource
# =========================

class tes1(Resource):

    def get(self):
        data = []

        for client in tes1.find():
            data.append({
                "id": str(client["_id"]),
                "name": client.get("name"),
                "email": client.get("email")
            })

        return data, 200

api.add_resource(tes1, "/")

if __name__ == "__main__":
    app.run(debug=True)