# Webhook Saver

This repository contains a simple Flask application that serves as an API for saving JSON data to a MongoDB database. The API receives JSON payloads via HTTP POST requests and stores them in a specified MongoDB collection.

## Usage

Follow the steps below to run Webhook Saver:

1. Clone the repository:

```bash
git clone https://github.com/moreloja/webhook-saver.git
cd webhook-saver
```

2. Build the Docker image:

```bash
docker compose build
```

3. Run the Docker container:

```bash
docker compose up -d
```

## Configuration

The API can be configured using environment variables:

- `MONGO_HOST`: The hostname or IP address of the MongoDB server. Default: `'mongodb'`
- `MONGO_PORT`: The port number of the MongoDB server. Default: `27017`
- `MONGO_DB_NAME`: The name of the MongoDB database to use. Default: `'moreloja'`
- `MONGO_COLLECTION_NAME`: The name of the MongoDB collection to store data in. Default: `'jellyfin-music'`

## API Endpoints

### Save JSON Data

- **Endpoint:** `/save_json`
- **Method:** `POST`
- **Payload:** JSON data to be saved in the specified MongoDB collection.
- **Response:** Returns a JSON response indicating success or error.

Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://localhost:4433/save_json
```
