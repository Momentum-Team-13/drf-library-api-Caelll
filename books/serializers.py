from rest_framework import serializers
from .models import Book, User, Tracker

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['title', 'author', 'publication_date', 'genre', 'featured']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email']

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['WANT_TO_READ', 'READING', 'FINISHED']