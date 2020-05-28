import unittest
import os
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import Actor, Movie, setup_db


class CastingTestCase(unittest.TestCase):
    """This class represents the casting test case"""

    def setUp(self):
        """Define test variables and initialize the app"""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

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
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])

    def test_post_actors(self):
        res = self.client().post('/actors', json=self.new_actor.format())
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])

    def test_delete_actors(self):
        actor = self.new_actor
        actor.insert()
        res = self.client().delete('/actors/{}'.format(actor.id))
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['deleted'])

    def test_patch_actors(self):
        actor = self.new_actor
        actor.insert()
        patched_actor = self.new_actor
        patched_actor.age = 34
        res = self.client().patch('/actors/{}'.format(actor.id), json=patched_actor.format())
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['actors'], patched_actor.format())


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
