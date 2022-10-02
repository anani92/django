from django.db import models
from requests import request

# Create your models here.


class UserManger(models.Manager):
    def validate_user(self, request_data):
        errors = {}
        if len(request_data.POST['first_name']) < 5:
            errors['first_name'] = 'first name should be at least 5 letters'
        if len(request_data.POST['last_name']) < 5:
            errors['last_name'] = 'last name should be at least 5 letters'
        if len(request_data.POST['email']) < 15:
            errors['email'] = 'email should be at least 15 letters'
        if request_data.POST['password'] != request_data.POST['confirm_password']:
            errors['password'] = 'password does not match'

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=95)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManger()
