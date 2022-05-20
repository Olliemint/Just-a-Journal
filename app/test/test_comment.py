import unittest
from app.models import User,Blog,Comment

class TestComment(unittest.TestCase):
    """
    This is where we will run all the tests for the Comment model
    """

    def setUp(self):    
        """
        This will create a new instance of User, Blog and Comment before each test
        """
        self.user_user= User(username = "Ollie", email ="oliverkoechrj@gmail.com", password = '1234')

        self.new_blog = Blog(title = "blog1",content ="my new blog")

        self.new_comment = Comment(comment = "ux", author = self.new_user, blog = self.new_blog)

    def tearDown(self):
        """
        Will clear the db after each test
        """
        
        
        Comment.query.delete()

    def test_instance(self):
        """
        Will test whether the new comment is an instance of the Comment model
        """
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_init(self):
        """
        Will test whether the comment is instantiated correctly
        """
        self.assertEquals(self.new_comment.comment, "its true")

    def test_relationship_picth(self):
        """
        Will test whether the comment is correctly related to its blog
        """

        blog_title = self.new_comment.blog.title
        self.assertTrue(blog_title == "hello")

    def test_relationship_user(self):
        """
        Will test whether the comment is correctly related to the user who posted it
        """

        username = self.new_comment.user.username
        self.assertTrue(username == "Ollie")