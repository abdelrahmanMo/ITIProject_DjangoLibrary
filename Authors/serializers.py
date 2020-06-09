from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Authors
class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ["authorName","phoneNumber","img"]
