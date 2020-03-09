import unittest

from models.py import Post


class PostTestCase(TestCase):
    # def setUp(self):
    #     Post.objects.create(title="Post", content="My Post")

    def test_post(self):
        post = Post(name="post", content="my post")
        self.assertEqual(post.content, "my post")


# Create your tests here.

if __name__ == '__main__':
    unittest.main()
