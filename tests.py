import unittest

import CSC307_LyncUp

from CSC307_LyncUp import wsgi

from LyncUp.models import Post



from django.db import models


class MyTestCase(unittest.TestCase):
    def test_post1(self):
        post = Post(title="post", content="my post", date_posted="Mon, 23 May 2016 08:30:15 GMT")
        self.assertEqual(post.title, "post")

    def test_post2(self):
        post = Post(title="post", content="my post")
        self.assertEqual(post.content, "my post")

    def test_post3(self):
        post = Post(title="post", content="my post")
        self.assertNotEqual(post.date_posted, "today")


if __name__ == '__main__':
    unittest.main()
