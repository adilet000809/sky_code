from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    email = models.EmailField()
    experience = models.IntegerField()
    image = models.ImageField(upload_to='teacher/')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Partner(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='partner/')

    def __str__(self):
        return self.name



