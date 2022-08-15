from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    genre = models.CharField(max_length=255)
    featured = models.BooleanField()

class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

class Tracker(models.Model):
    WANT_TO_READ = 'WTR'
    READING = 'R'
    FINISHED = 'F'
    TRACKING_LIST = [
        (WANT_TO_READ, "Want to Read"),
        (READING, "Reading"),
        (FINISHED, "Finished"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    status = models.CharField(max_length=3, choices=TRACKING_LIST, default=WANT_TO_READ)