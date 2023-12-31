# Generated by Django 4.2.4 on 2023-08-20 09:35

from django.db import migrations


def set_date(apps, schema_editor):
    Book = apps.get_model('reviews', 'Book')
    for book in Book.objects.all():
        book.release_date = "2022-07-01"
        book.save()

class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20230820_0926'),
    ]

    operations = [
        migrations.RunPython(set_date)
    ]
