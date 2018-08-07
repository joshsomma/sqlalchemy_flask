import unittest

from main import Session
from movie import Movie
from actors import Actor

session = Session()

class SQLAlchemy_tests(unittest.TestCase):
    
    def test_connect(self):
        print(session.query(Movie).exists())
        

    

