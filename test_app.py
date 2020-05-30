import unittest
import os
import json
from flask_sqlalchemy import SQLAlchemy
from jose import jwt

from app import create_app
from database.models import Actor, Movie, setup_db


class CastingTestCase(unittest.TestCase):
    """This class represents the casting test case"""

    def setUp(self):
        """Define test variables and initialize the app"""
        self.app = create_app()
        self.client = self.app.test_client
        self.executive_producer_jwt = os.environ.get('EXECUTIVE_PRODUCER')
        self.casting_manager_jwt = os.environ.get('CASTING_MANAGER')
        self.casting_assistant_jwt = os.environ.get('CASTING_ASSISTANT')
        self.executive_producer = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)
        }
        self.casting_manager = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.casting_manager_jwt)
        }
        self.casting_assistant = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.casting_assistant_jwt)
        }

        self.new_actor = Actor(name="Test_Actor", age=45, gender='Male')
        self.new_movie = Movie(title='Test_Movie', release_date='2016-12-06')

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_post_actors(self):
        res = self.client().post('/actors', json=self.new_actor.format(),
                                 headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])

    def test_delete_actors(self):
        actor = self.new_actor
        actor.insert()
        res = self.client().delete('/actors/{}'.format(actor.id),
                                   headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['deleted'])

    def test_patch_actors(self):
        actor = self.new_actor
        actor.insert()
        patched_actor = self.new_actor
        patched_actor.age = 34
        res = self.client().patch('/actors/{}'.format(actor.id),
                                  json=patched_actor.format(),
                                  headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'])

    def test_post_movies(self):
        res = self.client().post('/movies', json=self.new_movie.format(),
                                 headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'])

    def test_delete_movies(self):
        movie = self.new_movie
        movie.insert()
        res = self.client().delete('/movies/{}'.format(movie.id),
                                   headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['deleted'])

    def test_patch_movies(self):
        movie = self.new_movie
        movie.insert()
        patched_movie = movie
        patched_movie.title = 'New Title'
        res = self.client().patch('/movies/{}'.format(movie.id),
                                  json=patched_movie.format(),
                                  headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'])

    # Errors
    def test_401_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_401_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_400_post_actors(self):
        res = self.client().post('/actors', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 400)

    def test_404_delete_actors(self):
        res = self.client().delete('/actors/234255',
                                   headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)

    def test_404_patch_actors(self):
        res = self.client().patch('/actors/5365436',
                                  headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)

    def test_400_post_movies(self):
        res = self.client().post('/movies', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 400)

    def test_404_delete_movies(self):
        res = self.client().delete('/movies/234255',
                                   headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)

    def test_404_patch_movies(self):
        res = self.client().patch('/movies/5365436',
                                  headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)

    # Role Based Authentication
    def test_get_actors_casting_assistant(self):
        res = self.client().get('/actors', headers=self.casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_post_actors_casting_assistant(self):
        res = self.client().post('/actors', json=self.new_actor.format(),
                                 headers=self.casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_post_actors_casting_manager(self):
        res = self.client().post('/actors', json=self.new_actor.format(),
                                 headers=self.casting_manager)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])

    def test_401_delete_movies_casting_manager(self):
        movie = self.new_movie
        movie.insert()
        res = self.client().delete('/movies/{}'.format(movie.id),
                                   headers=self.casting_manager)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
