import os
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Get MongoDB connection details from environment variables
mongo_host = os.environ.get('MONGO_HOST', 'mongodb')
mongo_port = int(os.environ.get('MONGO_PORT', 27017))
mongo_db_name = os.environ.get('MONGO_DB_NAME', 'moreloja')
mongo_collection_name = os.environ.get('MONGO_COLLECTION_NAME', 'jellyfin-music')

client = MongoClient(host=mongo_host, port=mongo_port)
db = client[mongo_db_name]
collection = db[mongo_collection_name]

@app.route('/save_json', methods=['POST'])
def save_json_to_mongodb():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        collection.insert_one(data)
        return jsonify({"message": "Data saved successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
