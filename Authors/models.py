from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Authors(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    authorName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=50)
    img = models.ImageField(upload_to='authors_img/',default='author_img/default.png')

    def __str__(self):
        return self.authorName

