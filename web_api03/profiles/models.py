from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=40)
    address = models.ForeignKey('Address', related_name='address', on_delete=models.CASCADE)


class Comment(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=40)
    body = models.TextField()
    postId = models.ForeignKey('Post', on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    userId = models.ForeignKey('Profile', on_delete=models.CASCADE)


class Address(models.Model):
    street = models.CharField(max_length=30)
    suite = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=15)


    def __str__(self):
        return self.street +" / " + self.suite +" / " +self.city +" / " + self.zipcode
