from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Books
class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields=['Name','statusName','author','description','bookImg']
