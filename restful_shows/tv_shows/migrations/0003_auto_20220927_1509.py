# Generated by Django 2.2.4 on 2022-09-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0002_shows_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='description',
            field=models.TextField(null=True),
        ),
    ]