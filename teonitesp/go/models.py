from django.db import models
from django.db import connection
# Create your models here.



class Authors(models.Model):
    id_author = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50,unique=True)



class Posts(models.Model):
    id_post = models.AutoField(primary_key=True)
    post = models.TextField()
    link = models.CharField(max_length=200,unique=True)
    crc = models.CharField(max_length=10)
    id_author = models.ForeignKey('Authors', on_delete=models.CASCADE )
