from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=75)
    release_date = models.DateField(auto_now=True)
    description = models.TextField(default="null")
