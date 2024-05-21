# Energy Services Simulation API

Welcome to the Energy Services Simulation API! This documentation lists a set of RESTful APIs to manage and simulate energy production where the backend is designed to interface with NREL's python based SDK, PySAM, for the System Advisory Module (SAM) Photovoltaic module with the intent to compare against Aurora Solar.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Batch Runs](#batch-runs)
- [API Endpoints](#api-endpoints)

## Overview

The Energy Services Simulation API allows users to input PV system's design id and check the energy production values, design component specs, and losses incurred. The goal is to provide a flexible and scalable solution for energy simulation needs.

## Features

- **Simulation Management**: Generate and monitor results for simulation jobs.
- **Detailed Logging and Error Handling**: Comprehensive logging for monitoring and debugging, with robust error handling mechanisms.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://yourusername@bitbucket.org/gelibitbucket/energy-services-simulation.git
    cd energy-services-simulation
    ```

2. **Installation Instructions:**

   ### Installation Instructions (tested on Windows)

   The `backend` module is managed by the `poetry` dependency management and packaging tool.
   
   On a `Windows` machine, `poetry` is best installed within a virtual environment.
   
   With Python 3, a virtual environment can be created as:
   
    ```bash
    C:\> python -m venv <path>\<env-name>
    ```

    The virtual environment can be activated as follows:
    
    ```bash
    C:\> <path>\<env-name>\Scripts\activate
    ```

    To deactivate simply execute
    
    ```bash
    (env) C:\> deactivate
    ```

    Once in an active virtual environment, install `poetry` as follows:
    
    ```bash
    (env) C:\> <path>\<env-name>\Scripts\pip install -U pip setuptools # update pip and setuptools
    (env) C:\> <path>\<env-name>\Scripts\pip install poetry
    ```

    To install the `backend API dependencies` :
    
    ```bash
    (env) C:\> cd backend
    (env) C:\backend> poetry install
    (env) C:\backend> python3 -m pip install requirements.txt
    ```

    The `backend` and the 'API' comes shipped with unit-tests and integration-tests which can be run by invoking:
    
    ```bash
    (env) C:\backend> poetry run pytest
    ```

3. **Run the application:**

    ```cmd
    (env) C:\backend> poetry run geli/views/simulation_api.py
    ```

## Usage

Once the application is running, you can interact with the API using tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/).

### Example Request

To start a new simulation:

 ```cmd
curl -X POST "http://localhost:8000/simulation/resi/v1/simulationjob" -H "Content-Type: application/json" -d "{
    \"input_params\": {
        \"param1\": \"value1\",
        \"param2\": \"value2\",
        ...
        \"param7\": \"value7\"
    }
 }"
 ```

## Batch Runs

- **Run batch script with hosting API on localhost:**

    To run a batch script that hosts the API on localhost, use the following command:
    
    ```cmd
    (env) C:\> cd backend
    (env) C:\backend> python geli/views/client_sim.py "invoking API"
    ```

- **Run batch script without hosting API on localhost:**

    To run a batch script without hosting the API on localhost, use the following command:
    
    ```cmd
    (env) C:\> cd backend
    (env) C:\backend> python geli/views/client_sim.py "without invoking API"
    ```

## API Endpoints

(https://nbmbz5znsb.execute-api.us-west-2.amazonaws.com/dev/simulation/resi/v1/simulationjob)
