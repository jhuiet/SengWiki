

#from tempfile import mkdtemp
from wiki.web.user import UserManager
from wiki.web.user import User

import os
from . import WikiBaseTestCase



TEST_FILE_PATH = 'C:\\Users\\jhuie\\PycharmProjects\\SEWIKI\\tests\\'
USER_FILE_PATH = 'C:\\Users\\jhuie\\PycharmProjects\\SEWIKI\\user\\'


USER_CONTENT = {u'name': {u'active': True, u'authentication_method': u'cleartext', u'password': u'1234', u'authenticated': True, u'roles': []}, u'sam': {u'active': True, u'authentication_method': u'cleartext', u'password': u'1234', u'authenticated': True, u'roles': []}, u'cho': {u'active': True, u'authentication_method': u'cleartext', u'password': u'12345678', u'authenticated': True, u'roles': []}}




class TestUserManager(WikiBaseTestCase):

##test if file content from read matches what it should be
##test if json file exists
##
    def setUp(self):
        super(TestUserManager, self).setUp()
        self.file = os.path.join(TEST_FILE_PATH, 'users.json')


    def test_invalid_authentication_method(self):
        m = UserManager(TEST_FILE_PATH)
        self.assertRaises(NotImplementedError, m.add_user, m, 'bobby', 12345, authentication_method='this will cause an error')

    def test_read(self):
        #assert self.file == UserManager.read(UserManager(TEST_FILE_PATH))
        self.assertEquals(USER_CONTENT,UserManager.read(UserManager(TEST_FILE_PATH)))
        #self.assertNotEqual(USER_CONTENT, UserManager.read(UserManager(USER_FILE_PATH))
    #def test_write(self):



    # def test_add_user(self):
    #     UserManager.add_user(UserManager(TEST_FILE_PATH), 'bobby', 12345,active=True, roles=[], authentication_method=None)
    #     self.assertEquals(USER_CONTENT, UserManager.read(UserManager(TEST_FILE_PATH)))
    #    # return User(self, name, userdata)


    def test_get_user(self):
        Manager = UserManager(TEST_FILE_PATH)


        self.assertEqual(Manager.get_user(self, 'cho'), User(Manager, 'cho', ''))
        #self.fail()

    def test_delete_user(self):
        self.fail()

    def test_update(self):
        self.fail()
