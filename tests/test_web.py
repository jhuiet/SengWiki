import os

from . import WikiBaseTestCase

TEST_FILE_PATH = 'C:\\Users\\jhuie\\PycharmProjects\\SEWIKI\\user\\testingg'

USER_CONTENT =u"""\
{
  "name": {
    "active": true, 
    "authentication_method": "cleartext", 
    "password": "1234", 
    "authenticated": true, 
    "roles": []
  }, 
  "sam": {
    "active": true, 
    "authentication_method": "cleartext", 
    "password": "1234", 
    "authenticated": true, 
    "roles": []
  }
}
"""

class WebContentTestCase(WikiBaseTestCase):
    """
        Various test cases around web content.
    """

    # def setUp(self):
    #     super(WikiBaseTestCase, self).setup()


    def test_index_missing(self):
        """
            Assert the wiki will correctly play the content missing
            index page, if no index page exists.
        """
        rsp = self.app.get('/')
        assert b"You did not create any content yet." in rsp.data
        assert rsp.status_code == 200
#may be able to test if a file is created or not, but that doesn't really test the method that well
    #def test_create_file(self):
        #assert self.create_file('bob',mkdtemp(dir=TEST_FILE_PATH))
               #== 'C:\\Users\\jhuie\\PycharmProjects\\SEWIKI\\user\\testingg\\bob'
        #def create_file(self, name, content=u'', folder=None):


#
#
# class TestUser(WebContentTestCase):
#
#     #def setUp(self):
#
#     def test_get(self):
#         self.fail()
#
#     def test_set(self):
#         self.fail()
#
#     def test_save(self):
#         self.fail()
#
#     def test_is_authenticated(self):
#         self.fail()
#
#     def test_is_active(self):
#         self.fail()
#
#     def test_is_anonymous(self):
#         self.fail()
#
#     def test_get_id(self):
#         self.fail()
#
#     def test_check_password(self):
#         self.fail()
#
#         #self.assertRaises(self, NotImplementedError, u, self, '#$HR#@')
#
#
#
#
# class TestUserManager(WebContentTestCase):
#
#     user_content = USER_CONTENT
#
#     def setUp(self):
#
#         super(TestUserManager, self).setUp()
#         #self.file = os.path.join(USER_MANAGER_FILE_PATH, 'users.json')
#
#     def test_read(self):
#         ''' simple test to see the data retrieved from json file is not null'''
#         self.assertEqual(self.test_read(), self.user_content)
#
#     def test_write(self):
#         self.fail()
#
#     def test_add_user(self):
#         assert User.adUser(self, name, userdata)
#
#     def test_get_user(self):
#         self.fail()
#
#     def test_delete_user(self):
#         self.fail()
#
#     def test_update(self):
#         self.fail()
