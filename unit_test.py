import unittest
from model import Users, session
from controller import ModelProcessor



class TestModelProcessor(unittest.TestCase):

    def setUp(self):
        self.mp = ModelProcessor()

    def tearDown(self):
        pass
        
    def test_user_exist(self):
        self.mp.add_user(888)
        self.exsist = self.mp.user_exists(888)
        self.assertEqual(self.exsist, True)
        

if __name__ == '__main__':
    unittest.main()
