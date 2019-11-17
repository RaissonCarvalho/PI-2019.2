from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profile" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.OneToOneField('Address', related_name='address', on_delete=models.CASCADE)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    postId = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    userId = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    @property
    def ammount(self):
        return self.comments.all()


class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    def __str__(self):
        return self.street +" / " + self.suite +" / " +self.city +" / " + self.zipcode