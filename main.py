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

db = client["tes"]
clients = db["clients"]


# =========================
# Client Resource
# =========================

class Client(Resource):

    def get(self):
        data = []

        for client in clients.find():
            data.append({
                "id": str(client["_id"]),
                "name": client.get("name"),
                "email": client.get("email")
            })

        return data, 200

api.add_resource(Client, "/clients")

if __name__ == "__main__":
    app.run(debug=True)