import unittest
from database import *

class TestDataBase(unittest.TestCase):

    # Gabriel
    def test_database_fetch_users(self):
        # tests to see if expected users are in database
        db_connection = connect_db("/Users/gabriel/Desktop/LyncUpDB")
        user_in_db = [('gabrielbarney', 'test', None, None)]
        confirm_logins_in_db = fetch_users(db_connection)
        self.assertEqual(confirm_logins_in_db, user_in_db)

    # Riley
    def test_database_connects(self):
        # test to see if database connection is made
        db_connection = connect_db("/Users/gabriel/Desktop/LyncUpDB")
        self.assertNotEqual(db_connection, False)

    # Matt
    def test_string_to_array(self):
        # test for method that converts string to array
        # for streamlining finicky database output
        database_array_conversion = ['gabrielbarney', 'test', 'None', 'None']
        # output type checked using isinstance()
        finicky_database_output = "[('gabrielbarney', 'test', None, None)]"
        conversion_string_to_array = string_to_array(finicky_database_output)
        self.assertListEqual(database_array_conversion, conversion_string_to_array)