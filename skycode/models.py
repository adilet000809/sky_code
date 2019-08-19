from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


class Teacher(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    email = models.EmailField()
    experience = models.IntegerField()
    image = models.ImageField(upload_to='teacher/')

    def __str__(self):
        return self.firstName + ' ' + self.lastName


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
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Request(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comments = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.phone


class News(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Teacher)
def teacher_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(post_delete, sender=Partner)
def partner_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(post_delete, sender=Course)
def course_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(post_delete, sender=News)
def news_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(post_save, sender=Question)
def question_delete(sender, instance, **kwargs):
    if instance.answered:
        instance.delete()


@receiver(post_save, sender=Request)
def request_delete(sender, instance, **kwargs):
    if instance.accepted:
        instance.delete()


