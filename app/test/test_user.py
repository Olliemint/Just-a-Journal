import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Ollie = User(username = "Ollie", email ="oliverkoechrj@gmail.com", password = '1234')
        

        

    def tearDown(self):
        User.query.delete()
 
    def test_password(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    

    def test_save_user(self):
        self.new_user.save_user()
        self.assertTrue(len(User.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_user.username, 'Ollie')
        self.assertEquals(self.new_user.email, 'oliverkoechrj@gmail.com')
        self.assertTrue(self.new_user.password,'1234')


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password 