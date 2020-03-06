from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Group(models.Model):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(User)
    image = models.ImageField(default='default.jpg', upload_to='group_pics')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
