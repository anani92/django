# Generated by Django 2.2.4 on 2022-09-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('release_date', models.DateField(auto_now=True)),
                ('description', models.TextField(default='null')),
            ],
        ),
    ]
