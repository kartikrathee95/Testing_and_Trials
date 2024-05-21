# Energy Services Simulation API

Welcome to the Energy Services Simulation API! This project provides a set of RESTful APIs to manage and simulate energy production and storage scenarios.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Energy Services Simulation API allows users to submit simulation jobs and check the status and results of these simulations. The goal is to provide a flexible and scalable solution for energy simulation needs.

## Features

- **Simulation Management**: Submit, monitor, and retrieve results for simulation jobs.
- **Asynchronous Processing**: Efficient handling of simulation tasks using asynchronous programming.
- **Detailed Logging and Error Handling**: Comprehensive logging for monitoring and debugging, with robust error handling mechanisms.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/energy-services-simulation.git
    cd energy-services-simulation
    ```

2. **Install dependencies:**

    We use [Poetry](https://python-poetry.org/) for dependency management. If you don't have Poetry installed, you can install it by following the [official guide](https://python-poetry.org/docs/#installation).

    ```bash
    poetry install
    ```

3. **Run the application:**

    ```bash
    poetry run uvicorn app.main:app --reload
    ```

## Usage

Once the application is running, you can interact with the API using tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/).

### Example Request

To start a new simulation:

```bash
curl -X POST "http://127.0.0.1:8000/simulation/start" -H "Content-Type: application/json" -d '{
    "input_Params": {
        "param1": "value1",
        "param2": "value2",
        ...
    }
}'
