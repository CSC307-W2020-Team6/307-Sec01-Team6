from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Group(models.Model):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(User)
    image = models.ImageField(default='default_group.jpg', upload_to='group_pics')
    group_owner = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, related_name='group_owner')

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


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


