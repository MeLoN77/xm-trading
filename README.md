# trading-platform-xm
Automation testing using Python 3

    trading-platform-xm/
    │
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    ├── trade_xm_app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── database.py
    │   ├── models.py
    │   ├── routers/
    │   │   ├── __init__.py
    │   │   ├── orders.py
    │   ├── websocket.py
    ├── tests/
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── constants_for_test.py
    │   ├── test_rest_api.py
    │   ├── test_websocket.py
    │   ├── test_performance.py




## Trading Platform API

### Overview

This project simulates a trading platform API with WebSocket support. The API is built using FastAPI and Dockerized for easy deployment.

### Requirements

- Docker
- Docker Compose (optional)
- Install python 3.10 and create new .venv folder:
  - ```
    # python3 -m venv .venv
    # source .venv/bin/activate
    ```
- Install python requirements by running command:
  - ```pip install -r test-requirements.txt```
- Install Docker Desktop & Run it

### Running the Application

1. **Build the Docker image:**

    ```` 
    docker build -t trading-platform-xm-api .
    ````
   
2. **When you want to run standalone the Trading API Docker container:**

    ````
    docker run -d -p 8000:8000 trading-platform-xm
    ````

3. **Build the Test Docker image:**

    ```` 
    docker build -t trading-platform-xm-tests .
    ````
   
4. **Run the Docker Compose**

    ````
    docker-compose up --build
    ````

    - Copy report file:
      ```commandline
      docker cp trading-platform-xm-tests:/trade_xm_app/reports/report.html ./reports/report.html
    ```


5. **Shut Down the Docker Compose and Clean Up images**
    ````
    docker-compose down && docker rmi $(docker images -q)
    ````

6. **Access the API documentation:**
Open your browser and navigate to http://localhost:8000/docs to view the automatically generated API documentation provided by Swagger.

    
    Endpoints
    POST /orders: Create a new order.
    GET /orders/{order_id}: Get order details by order_id.
    PUT /orders/{order_id}/status: Update order status by order_id.
    DELETE /orders/{order_id}: Delete an order by order_id.
    ws://localhost:8000/ws: WebSocket endpoint for real-time updates.

7. **Making API Requests**
Use tools like curl, Postman, or directly through the Swagger UI.

Example curl Commands

- Create an Order:  
    ````
    curl -X POST "http://localhost:8000/orders" -H "Content-Type: application/json" -d '{"details": "Order details"}'
    ````

- Get an Order:  
    ````
    curl -X GET "http://localhost:8000/orders/{order_id}"
    ````
  
- Get an all Orders:  
    ````
    curl -X GET "http://localhost:8000/orders"
    ````

- Update Order Status:  
    ````
    curl -X PUT "http://localhost:8000/orders/{order_id}/status" -H "Content-Type: application/json" -d '{"details": "Order updated details"}'
    ````
  

- Delete an Order:  
    ````
    curl -X DELETE "http://localhost:8000/orders/{order_id}"
    ````

### Running the Tests

1. **Run the API tests**:
   ```
   pytest tests/test_rest_api.py --html=reports/report_rest_api.html
   ```

2. **Run the WebSocket tests**:
    ```
    pytest tests/test_websocket.py --html=reports/report_websocket.html
   ```

3. **Run the performance tests**:
    ```
    pytest tests/test_performance.py --html=reports/report_performance.html
   ```
