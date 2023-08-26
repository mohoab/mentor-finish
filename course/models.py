from django.db import models
from django.contrib.auth.models import User
import datetime

class skills(models.Model):
    name= models.TextField()
    def __str__(self) :
        return self.name
#########################################################################
class category(models.Model):
    title= models.CharField(max_length=50)


    def __str__(self) :
        return self.title
#########################################################################
class trainer (models.Model):
    info = models.ForeignKey(User , on_delete=models.CASCADE)
    skills = models.ManyToManyField(skills)
    descriptions = models.CharField(max_length=200)
    twitter = models.TextField(null=True)
    facebook = models.TextField(null=True)
    linkdien = models.TextField(null=True)
    instagram = models.TextField(null=True)
    image = models.ImageField(upload_to='trainers' , default= 'trainers/default.jpg')
    status = models.BooleanField(default=True)
    def __str__(self) :
        return self.info.username
#########################################################################
class course (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='course')
    counted_views = models.IntegerField(default=0)
    counted_likes = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    trainer = models.ForeignKey(trainer , on_delete= models.CASCADE)
    category = models.ManyToManyField(category)
    schedule = models.DateTimeField(default=datetime.datetime.now())
    available_seats = models.IntegerField(default=0)
    class Meta:
        ordering = ('-created_date',)

    def __str__(self) :
        return self.title
        