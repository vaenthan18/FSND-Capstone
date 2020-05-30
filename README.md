# FSND Capstone Project: Casting Agency API

## Introduction to Project
---
This application developed for the Udacity Full Stack Nanodegree Program aims to make logging Actors and Movies along with their respective details easier for a casting agency, with a remote server and database that can be accessed with the appropriate credentials to give the individuals of the casting agency the appropriate access. This runs off of a flask server hostend on heroku following the pep8 style guidelines with an optional ionic frontend that can be run locally.


## Application URL's: 

- **Live Production Server:**

```txt
https://vaenthan-casting-agency.herokuapp.com/
```

- **Local Development Server:**

```shell
http://localhost:5000
```


- **Local Frontend Application:**

```shell
http://localhost:8100
```


## Getting Started

---

### Backend
---
### Installing Dependencies:
**Python 3.7**

Follow instructions to install the version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

**Virtual Environment**

It is recommended to utilize a virtual environment to run this project locally. This will allow us to ensure that your project can wrap it's particular set of dependencies to the project scope, and ensures you're not polluting the global python installation on your local machine. Complete instructions for setting up a proper virtual environment can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

**Install Dependencies**

```shell
pip install -r requirements.txt
```

- This will install all of the required python packages which are located in the `requirements.txt` file



#### Setup Local Postgres Database

```shell
createdb capstone
```

- Setup environment variable for local database path:

```shell
export DATABASE_URL=<URI_TO_DATABASE> 
```


**Running The Server Locally**
>From the project root directory, run
>```shell
>source ./setup.sh
>export DATABASE_URL=<URI_TO_DATABASE> 
>```
>
> **NOTE:**  <u>Production database paths are already configured via Heroku</u>
>
> 
>
> Set entry-point and run the application:
>
> ```shell
> export FLASK_APP=app.py
> flask run --reload
> ```



**Running Tests**
>To test the python unit tests, from the project root directory, run
>```shell
>source ./setup.sh
>python3 test_app.py 
>```
>
>Endpoints can also be tested with [Postman](https://getpostman.com)
>- Import the postman collection `./vaenthan-fsnd-capstone.postman_collection.json`
>- Run the collection to manually test each endpoint.
>- If a 404 error is raised, reset the database and run again
>- The local database must be running

**JWT's and other Environment Variables can be found in `setup.sh`**

### Frontend (Optional)
---

**Installing Node and NPM**

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

**Installing Ionic Cli**

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI  is in the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

**Installing project dependencies**

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal, cd into the `frontend` directory and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

## Running Your Frontend in Dev Mode

Ionic ships with a useful development server which detects changes and transpiles as you work. The application is then accessible through the browser on a localhost port. To run the development server, cd into the `frontend` directory and run:

```bash
ionic serve
```

>_Node_: By default the frontend connects to the remote server, however this can be modified in the apiServerUrl field in `./frontend/src/environments/environment.ts`

## API Reference

---

| API Base URL:                              | Environment:               |
| ------------------------------------------ | -------------------------- |
| https://vaenthan-casting-agency.herokuapp.com/ | Production API Base URL    |
| http://localhost:5000/                  | Local Development Base URL |



### All Available Endpoints:

| Endpoint:               | Available Methods:     | Details:                                                     |
| ----------------------- | ---------------------- | ------------------------------------------------------------ |
| `/`                     | `GET`                  | returns the application index route                          |
| `/actors`            | [`GET, POST`]          | used to `GET` a `list` of all `actors` and `POST` new `actors` |
| `/movies`            | [`GET, POST`]          | used to `GET` a `list` of all `movies` and `POST` new `movies` |
| `/actors/<actor_id>` | [`PATCH, DELETE`] | used to `PATCH` or `DELETE` a single `actor` by `actor_id` |
| `/movies/<movie_id>` | [`PATCH, DELETE`] | used to `PATCH` or `DELETE` a single `movie` by `movie_id` |



### Permissions By Role:

| Permissions     | Roles                                                       | Details                                                      |
| --------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| `get:actors`    | [`executive_producer, casting_director, casting_assistant`] | get a list of all actors|
| `get:movies`    | [`executive_producer, casting_director, casting_assistant`] | get a list of all movies|
| `post:actors`   | [`executive_producer, casting_director`]                    | post a new actor, using the `POST` method   |
| `post:movies`   | [`executive_producer`]                                      | post a new movie, using the `POST` method   |
| `patch:actors`  | [`executive_producer, casting_director`]                    | update an existing actor, using the `PATCH` method  |
| `patch:movies`  | [`executive_producer, casting_director`]                    | update an existing movie, using the `PATCH` method  |
| `delete:actors` | [`executive_producer, casting_director`]                    | delete an existing actor, using the `DELETE` method |
| `delete:movies` | [`executive_producer`]                                      | delete an existing movie, using the `DELETE` method  |



## Endpoint Usage

**`GET /actors`**

> - Fetch a list of `actors`
> - Args: `none`
> - Returns: `JSON` containing formatted actor data
>
> **EXAMPLE RESPONSE:**
>
> ```json
> {
>   "actors": [
>     {
>       "id": 1,
>       "name": "Scarlett Johansson",
>       "age": 35,
>       "gender": "Female"
>     },
>     {
>       "id": 2,
>       "name": "Tom Holland",
>       "age": 22,
>       "gender": "Male"
>     },
>     {
>       "id": 3,
>       "name": "Leonardo Dicaprio",
>       "age": 38,
>       "gender": "Male"
>     }
>   ],
>   "success": true
> }
> ```



**`GET /movies`**

> - Fetch a list of `movies`
> - Args: `none`
> - Returns: `JSON` containing formatted movie data
>
> **EXAMPLE RESPONSE:**
>
> ```json
> {
>   "movies": [
>     {
>       "id": 1,
>       "title": "Avengers",
>       "release_date": "2010-04-20"
>     },
>     {
>       "id": 2,
>       "title": "Lion King",
>       "release_date": "2018-06-17"
>     },
>     {
>       "id": 3,
>       "title": "Die Hard",
>       "release_date": "1998-01-26"
>     }
>   ],
>   "success": true
> }
> ```





**`POST /actors`**

> - Insert new actor record into database
> - Args: `name, age, gender`
> - Returns: `JSON` reponse containing request status, and the new actor in a list
>
> **EXAMPLE RESPONSE**
>
> ```json
> {
>   "actor"s: [
>     {
>       "age": 24,
>       "gender": "Male",
>       "id": 4,
>       "name": "Tim Adams"
>     }
>   ],
>   "success": true
> }
> ```





**`POST /movies`**

> - Insert new movie record into database
> - Args: `title, year`
> - Returns: `JSON` response containing request status and new movie details
>
> **EXAMPLE RESPONSE**
>
> ```json
> {
>   "movies": [
>     {
>       "id": 4,
>       "title": "The Movie 4",
>       "release_date": "2004-01-26"
>     }
>   ],
>   "success": true
> }
> ```



**`PATCH /actors/<int:actor_id>`**

> - Fetch a single `actor` by `actor_id`
> - Args: `actor_id`
> - Returns: `JSON` repsonse containing request status and updated actor in a list
>
> **EXAMPLE RESPONSE:**
>
> ```json
> {
>   "actors": [
>     {
>       "age": 34,
>       "gender": "Male",
>       "id": 2,
>       "name": "Leroy Jenkins"
>     }
>   ],
>   "success": true
> }
> ```
>
> 



**`PATCH /movies/<int:movie_id>`**

> - Fetch a single `movie` by `movie_id`
> - Args: `movie_id`
> - Returns: `JSON` repsonse containing request status and updated movie in a list
>
> **EXAMPLE RESPONSE:**
>
> ```json
> {
>   "movies": [
>     {
>       "id": 2,
>       "title": "Endgame",
>       "release_date": "2019-04-26"
>     }
>   ],
>   "success": true
> }
> ```



**`DELETE /actors/<int:actor_id>`**

> - Delete a single `actor` by `actor_id`
> - Args: `actor_id`
> - Returns: `JSON` repsonse containing request status and deleted `actor_id`
>
> **EXAMPLE RESPONSE:**
>
> ```json
> {
>   "deleted": 3,
>   "success": true
> }
> ```



**`DELETE /movies/<int:movie_id>`**

> - Delete a single `movie` by `movie_id`
> - Args: `movie_id`
> - Returns: `JSON` repsonse containing request status, and deleted `movie_id`
>
> **EXAMPLE RESPONSE:**
>
> ```json
> {
>   "deleted": 3,
>   "success": true
> }
> ```

