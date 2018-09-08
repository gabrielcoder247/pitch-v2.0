import unittest
from app.models import User



class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password = 'moringa')
        