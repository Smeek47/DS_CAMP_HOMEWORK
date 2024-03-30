# Simple REST API with FastAPI

This is a simple REST API server implemented using FastAPI, capable of handling three types of requests: GET, POST, and DELETE.

## Entry Points

1. **POST /api/add_record/{record}**
   - Adds the specified record to the server and returns a response indicating the addition.
   
2. **GET /api/last_10_records**
   - Retrieves the last 10 added records in JSON format.

3. **DELETE /api/delete_record/{record}**
   - Deletes the specified record from the server and returns a response indicating the deletion.

## Usage

1. Clone this repository to your local machine
2. Locate in command line to directory: 
```CMD
cd your_repository_dir
```
1. Build docker image using:
```CMD
docker build -t myapi .
```
1. Run container by:
```CMD
docker run -d --name myapi-container -p 8000:8000 myapi
```
1. Now you can go to http://127.0.0.1:8000/docs and check workability
