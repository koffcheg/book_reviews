# Generated by Django 4.2.4 on 2023-08-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20230820_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
