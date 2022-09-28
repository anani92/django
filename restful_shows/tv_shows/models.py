from django.db import models
from datetime import datetime
today = datetime.today()
print(today)


class ShowsManager(models.Manager):
    def show_validator(self, request_data):
        errors = {}
        if len(request_data['show_title']) < 5:
            errors['title'] = 'Please enter a valid title'
        if len(request_data['net_work']) < 5:
            errors['network'] = 'Please enter a valid network'
        if len(request_data['desc']) < 75:
            errors['desc'] = 'description should be at least 70 charachters'
        if request_data['release_date'] > str(today):
            errors['release_date'] = 'please enter a valid date'
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(null=True)
    objects = ShowsManager()
