# Flask web application 
This app provides a RESTful API for managing a collection of items. The application supports basic CRUD operations (Create, Read, Update, Delete) and uses SQLite as the database.

## Features
* Add new items to the database.
* Retrieve a list of all items.
* Simple JSON-based API.

## Technologies Used
* Flask: A lightweight WSGI web application framework.
* SQLite: A lightweight database for storing items.
* Werkzeug: A comprehensive WSGI web application library.

# Getting Started
## Prerequisites
* Docker installed on your machine.
* Basic knowledge of how to use curl or a tool like Postman for making HTTP requests.

## Building and Running the Application
1. Build the Docker image:
`docker build -t my-flask-app .`
2. `docker run -p 5000:5000 my-flask-app`
3. Access the API: Open your browser or use a tool like Postman to interact with the API.

## Accessing the application:
* http://ip-address:5000/items    (or)
* http://localhost:5000/items


## To POST:
* Use a tool like Postman or curl to send a POST request to `http://localhost:5000/items`
* `curl -X POST -H "Content-Type: application/json" -d '{"name": "Item 1"}' http://localhost:5000/items`

## CURL Commands:
* `curl -X GET http://localhost:5000/items`
* `curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Item"}' http://localhost:5000/items/1`
* `curl -X DELETE http://localhost:5000/items/1`
* `curl -X POST -H "Content-Type: application/json" -d '{"name": "Item 2", "description": "This is item 2."}' http://localhost:5000/items`


## API Endpoints
1. Get All Items
* Endpoint: GET /items
* Description: Retrieve a list of all items in the database.
* Response:
  * Status Code: 200 OK
  * Body: JSON array of items.

### Example response:
```
[
    [1, "Item 1"],
    [2, "Item 2"]
]
```

2. Add a New Item
* Endpoint: POST /items
* Description: Add a new item to the database.
* Request Body:
  * JSON object with the following structure:
```
  {
    "name": "Item Name"
  }
```

* Response:
* Status Code: 201 Created
* Body: JSON message confirming the addition.
Example response:
```
{
    "message": "Item added"
}
```

## Notes:
The application uses SQLite for storage, which means data will persist in the data.db file within the container.
