import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from database.models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(jwt):
        actors = Actor.query.all()
        formatted_actors = [actor.format() for actor in actors]
        return jsonify({
            'success': True,
            'actors': formatted_actors
        })

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(jwt):
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies]
        return jsonify({
            'success': True,
            'movies': formatted_movies
        })

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(jwt, actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)
        try:
            data = request.get_json('actor')
            actor.name = data['name']
            actor.age = data['age']
            actor.gender = data['gender']
            actor.update()
        except Exception:
            abort(400)

        return jsonify({
            'success': True,
            'actors': [actor.format()]
        })

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(jwt, movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)
        try:
            data = request.get_json('movie')
            movie.title = data['title']
            movie.release_date = data['release_date']
            movie.update()
        except Exception:
            abort(400)
        return jsonify({
            'success': True,
            'movies': [movie.format()]
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwt, actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)
        try:
            actor.delete()
        except Exception:
            abort(422)

        return jsonify({
            'success': True,
            'deleted': actor_id
        })

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(jwt, movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)
        try:
            movie.delete()
        except Exception:
            abort(422)

        return jsonify({
            'success': True,
            'deleted': movie_id
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def new_actor(jwt):
        try:
            data = request.get_json('actor')
            actor = Actor(name=data['name'],
                          age=data['age'], gender=data['gender'])
            actor.insert()
        except Exception:
            abort(400)
        return jsonify({
            'success': True,
            'actors': [actor.format()]
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def new_movie(jwt):
        try:
            data = request.get_json('movie')
            movie = Movie(title=data['title'],
                          release_date=data['release_date'])
            movie.insert()
        except Exception:
            abort(400)
        return jsonify({
            'success': True,
            'movies': [movie.format()]
        })

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
