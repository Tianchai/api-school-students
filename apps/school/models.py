import uuid
from django.db import models


def id_generator():
    return uuid.uuid4().hex[0:20]


class School(models.Model):
    id = models.CharField(
        primary_key=True,
        editable=False,
        max_length=20,
        default=id_generator,
    )
    name = models.CharField(max_length=20)
    max_students = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    id = models.CharField(
        primary_key=True,
        editable=False,
        max_length=20,
        default=id_generator,
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
