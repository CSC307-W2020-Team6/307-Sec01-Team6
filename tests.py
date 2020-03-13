
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# 
# 
# class AccountTestCase(LiveServerTestCase):
# 
#     def setUp(self):
#         self.selenium = webdriver.Safari()
#         super(AccountTestCase, self).setUp()
# 
#     def tearDown(self):
#         self.selenium.quit()
#         super(AccountTestCase, self).tearDown()
# 
#     def test_register(self):
#         selenium = self.selenium
#         # Opening the link we want to test
#         selenium.get('http://127.0.0.1:8000/register/')
#         # find the form element
#         username = selenium.find_element_by_id('id_username')
#         email = selenium.find_element_by_id('email')
#         password1 = selenium.find_element_by_id('password1')
#         password2 = selenium.find_element_by_id('password2')
#         submit = selenium.find_element_by_name('register')
# 
#         username.send_keys('rmete')
#         email.send_keys('riley@mete.com')
#         password1.send_keys('password321')
#         password2.send_keys('password321')
# 
#         submit.send_keys(Keys.RETURN)
# 
#         assert 'Check your email' in selenium.page_source

import unittest
import CSC307_LyncUp
from CSC307_LyncUp import wsgi
from LyncUp.models import Post, Group
from users.models import Profile
from timetable.models import Event
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class MyTestCase(unittest.TestCase):

    # The following test cases are designed to test our Post class
    def test_post1(self):
        post = Post(title="post", content="my post", date_posted="Mon, 23 May 2016 08:30:15 GMT")
        self.assertEqual(post.title, "post")

    def test_post2(self):
        post = Post(title="post", content="my post")
        self.assertEqual(post.content, "my post")

    def test_post3(self):
        post = Post(title="post", content="my post")
        self.assertNotEqual(post.date_posted, "today")

    # The following test cases are designed to test our Group class

    def test_group1(self):
        matt = User(username="MattyJ", password="word", email="matt@icloud.com",
                    first_name="Matt", last_name="Jaojoco", id=0)
        riley = User(username="RiRi", password="word", email="riley@icloud.com",
                     first_name="Riley", last_name="Mete", id=1)
        gabe = User(username="Gabester", password="word", email="gabe@icloud.com",
                    first_name="Gabe", last_name="Barney", group=3, id=2)
        group = Group(name="The Boys", id=3, image='default_group.jpg', group_owner=matt)

        self.assertEqual("The Boys", group.name)


    def test_group3(self):
        matt = User(username="MattyJ", password="word", email="matt@icloud.com",
                    first_name="Matt", last_name="Jaojoco", id=0)
        riley = User(username="RiRi", password="word", email="riley@icloud.com",
                     first_name="Riley", last_name="Mete", id=1)
        gabe = User(username="Gabester", password="word", email="gabe@icloud.com",
                    first_name="Gabe", last_name="Barney", group=3, id=2)
        group = Group(name="The Boys", id=3, image='default_group.jpg', group_owner=matt)

        self.assertEqual(group.image, 'default_group.jpg')

    def test_group4(self):
        matt = User(username="MattyJ", password="word", email="matt@icloud.com",
                    first_name="Matt", last_name="Jaojoco", id=0)
        riley = User(username="RiRi", password="word", email="riley@icloud.com",
                     first_name="Riley", last_name="Mete", id=1)
        gabe = User(username="Gabester", password="word", email="gabe@icloud.com",
                    first_name="Gabe", last_name="Barney", group=3, id=2)
        group = Group(name="The Boys", id=3, image='default_group.jpg', group_owner=matt)

        self.assertEqual(group.group_owner, matt)

# The following test cases are designed to test our Profile class

    def test_profile1(self):
        gabe = User(username="Gabester", password="word", email="gabe@icloud.com",
                    first_name="Gabe", last_name="Barney", group=3, id=2)
        profile = Profile(user=gabe, image="default.jpg")
        self.assertEqual(profile.user, gabe)

    def test_profile2(self):
        riley = User(username="RiRi", password="word", email="riley@icloud.com",
                     first_name="Riley", last_name="Mete", id=1)
        profile = Profile(user=riley, image="default.jpg")
        self.assertEqual(profile.image, "default.jpg")

# The following test cases are designed to test our Event class
    def test_event1(self):
        matt = User(username="MattyJ", password="word", email="matt@icloud.com",
                    first_name="Matt", last_name="Jaojoco", id=0)
        event = Event(owner=matt, event_name="Software Engineering", date=timezone.now,
                      start_time=timezone.now, end_time=timezone.now)
        self.assertEqual(event.owner, matt)

    def test_event2(self):
        gabe = User(username="Gabester", password="word", email="gabe@icloud.com",
                    first_name="Gabe", last_name="Barney", group=3, id=2)
        event = Event(owner=gabe, event_name="Programming", date=timezone.now,
                      start_time=timezone.now, end_time=timezone.now)
        self.assertEqual(event.event_name, "Programming")

    def test_event3(self):
        riley = User(username="RiRi", password="word", email="riley@icloud.com",
                     first_name="Riley", last_name="Mete", id=1)
        event = Event(owner=riley, event_name="Coding", date=timezone.now,
                      start_time=timezone.now, end_time="08:10:00")
        self.assertEqual(event.end_time, "08:10:00")



if __name__ == '__main__':
    unittest.main()

