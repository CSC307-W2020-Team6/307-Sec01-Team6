from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.utils import timezone
import pytz

from .models import Post


class TestCases(TestCase):
    def test_fields(self):
        user1 = User(username="gabriel",
                     password="test1",
                     email="test@test.com")
        user1.save()
        post = Post(title="title!", content="content!",
                     date_posted=timezone.now(),
                     author=User.objects.first())
        post.save()
        tester = Post.objects.first()
        self.assertEqual(tester, post)
