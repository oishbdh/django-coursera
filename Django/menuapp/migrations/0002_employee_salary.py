# Generated by Django 4.1.7 on 2023-04-01 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
