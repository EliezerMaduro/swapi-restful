# Technical Challenge NTD

## Overview

This project is a solution to the technical challenge provided by NTD. 

## Features

This project is divided in 3 modules to allow responsability segregation, It have an ingestion app that ingest all the data deltas from https://swapi-graphql.netlify.app/graphql GraphQL API every 5 minutes, this is achieved thanks to a celery worker scheduler, once it gets the data from the API it update or create a new record on the database.

In the other side, we have the rest_api app that creates the RESTful API to consume the data from the database, it is a CRUD API. These are the additional feature included in this API, it have **CORS validation** to be able to be consumed from a frontend, it is **API Key based authentication** which the current API Key value for test purposes is: **aAKGsQ7nenYEA5SoiKhhj7HMzYC83rpyf8qEq0Bs**, it have a **pagination** to not overload API responses, and it have a **Swagger** in the path **/api/docs/** where you can test out the API adding the API Key mentioned.

Then, we have Core app where is all the cross-app models, in order to make easier the import of the models.

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/technical_challenge_ntd.git
    ```
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the application:**
    ```bash
    python manage.py runserver
    ```

4. **Required Enviromental Variables**
    ```bash
    POSTGRES_DB
    POSTGRES_USER
    POSTGRES_PASSWORD
    POSTGRES_HOST
    POSTGRES_PORT
    POSTGRES_SSLMODE

    REDIS_URL
    ``` 

## Test API

- **API KEY**: **aAKGsQ7nenYEA5SoiKhhj7HMzYC83rpyf8qEq0Bs**