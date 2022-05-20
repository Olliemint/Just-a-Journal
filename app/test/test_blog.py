import unittest

from app.models import Blog,User

class TestBlog(unittest.TestCase):
    """
    This is the class which we will use to do tests for the Blog
    """

    def setUp(self):
        """
        This will create an instance of the Blog before each test case
        """
        self.user_Ollie = User(username = "Ollie", email ="oliverkoechrj@gmail.com", password = '1234')
        self.new_blog = Blog(title = "blog1",content ="my new blog")

    def tearDown(self):
        """
        Will delete all the info from the db
        """
        Blog.query.delete()
        User.query.delete()
    

    def test_instance(self):
        """
        Will test whether the new_blog is an instance of Blog
        """
        self.assertEquals(self.new_blog.title,'blog1')
        self.assertEquals(self.new_blog.content,'my new blog')

  

    def test_save_blog(self):
        """
        Will test whether the user is saved into the database
        """
        self.new_blog.save_blog()
        blogs = Blog.query.all()
        self.assertTrue(len(blogs) > 0)

    def test_relationship_user(self):
        """
        Will test whether the blog is correctly related to the user who posted it
        """
        user = self.new_blog.username
        self.assertTrue(user == "Ollie")
        
    def test_get_blog_by_id(self):
    
        self.new_blog.save_blog()
        got_blog = Blog.get_blogs(12)
        self.assertTrue(len(got_blog) == 1)  
        
        
        
        
        
        