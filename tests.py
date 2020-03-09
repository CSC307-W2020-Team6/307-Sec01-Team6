import unittest
import CSC307_LyncUp
from CSC307_LyncUp import wsgi
from LyncUp.models import Post, Group
from django.contrib.auth.models import User
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

    # def test_group2(self):
    #     matt = User(username="MattyJ", password="word", email="matt@icloud.com",
    #                 first_name="Matt", last_name="Jaojoco", id=0)
    #     riley = User(username="RiRi", password="word", email="riley@icloud.com",
    #                  first_name="Riley", last_name="Mete", id=1)
    #     gabe = User(username="Gabester", password="word", email="gabe@icloud.com",
    #                 first_name="Gabe", last_name="Barney", group=3, id=2)
    #     group = Group(name="The Boys", id=3, image='default_group.jpg', group_owner=matt)
    #     group.members = models.ManyToManyField(riley)
    #     self.assertEqual(group.members[0], riley)

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


if __name__ == '__main__':
    unittest.main()
