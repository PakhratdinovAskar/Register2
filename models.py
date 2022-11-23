from django.db import models

# Create your models here.
class Person(models.Model):
    lastName = models.TextField()
    firstName = models.TextField()


class NumberPhone(models.Model):
    number = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)