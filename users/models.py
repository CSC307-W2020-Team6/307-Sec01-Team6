from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    ##
    friends = models.ManyToManyField('self', through='Relationship',
                                     symmetrical=False,
                                     related_name='related_to')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

## From here
class Relationship(models.Model):
    from_person = models.ForeignKey(Profile, related_name="from_people",
                                    on_delete=models.CASCADE)
    to_person = models.ForeignKey(Profile, related_name = 'to_people',
                                  on_delete=models.CASCADE)

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_users = models.ForeignKey(User, related_name="owner", null = True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

    def save(self):
        super().save()

    def __str__(self):
        return str(self.current_user)
