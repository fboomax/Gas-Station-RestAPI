# <font >Gas Station Django Project with REST API</font>

This repository contains a Python project built with Django that simulates a gas station management system. 
The project includes a REST API to facilitate the interaction with the gas station's data.

## Features

* User authentication: Users can create accounts, log in, and perform actions based on their roles.
* Gas station management: Users can manage various aspects of the gas station, such as fuel prices, inventory, and sales.
* REST API: Provides endpoints to interact with the gas station's data, allowing external applications to integrate with the system.

## Installation & Run app

1. Create [Python 3.8 virtualenv and activate it](https://docs.python.org/3/library/venv.html)
3. Install [Docker Engine](https://docs.docker.com/engine/install/)
4. Clone the repository
5. Build docker containers 
```docker-compose build```
7. Run docker containers
```docker-compose up```
9. Using the app 
  Visit http://127.0.0.1:8000

## API Endpoints
- 'GET /api/v1/gas-stations': Retrieve a list of gas stations (json).
- 'GET /api/v1/gas-stations-xml': Retrive a list of gas station (XML).
- 'GET /api/v1/gas-stations/{station_id}': Retrieve details of a specific gas station.
- 'GET /api/v1/gas-stations/{station_id}/prices-data': Retrieve the fuel prices for a specif gas station.
- 'GET /api/v1/gas-stations/all': Retrieve the quantity of the gas stations.
- 'GET /api/v1/prices-data': Retrive the prices data of the gas stations.
- 'GET /api/v1/prices-data/aggregate': Retrieve min, average and max, price per lt

## Acknowledgements
- **Django**: The web framework used in this project.
- **Django REST Framework**: The toolkit used to build the REST API.
- **Python**: The programming language used for development.

