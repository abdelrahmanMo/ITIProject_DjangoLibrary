from django.db import models
from django.contrib.auth.models import User

from Authors.models import Authors
# Create your models here.

class status(models.Model):
    statName = models.CharField(max_length=50)

    def __str__(self):
        return self.statName

class Books(models.Model):
    User = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    statusName = models.ForeignKey(status,null=True,on_delete=models.SET_NULL)
    author = models.ForeignKey(Authors,on_delete=models.CASCADE,related_name="listbook")
    Name = models.CharField(max_length=50)
    description = models.TextField(default=' ')
    bookImg = models.ImageField(upload_to='book_img',default='book_img/default.png')

    def __str__(self):
        return self.Name