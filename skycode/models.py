from django.db import models


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


class CourseManager(models.Manager):
    def all(self):
        return super(CourseManager, self).get_queryset().filter(available=True)


class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    start = models.DateField()
    time = models.TimeField()
    duration = models.CharField(max_length=50)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='course/')
    description = models.TextField(max_length=200, null=True, blank=True)
    objects = CourseManager()

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    question = models.TextField(max_length=200)
    answered = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.name


class Request(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.phone






