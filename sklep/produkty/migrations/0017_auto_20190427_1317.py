# Generated by Django 2.2 on 2019-04-27 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0016_auto_20190427_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produkty',
            old_name='image',
            new_name='obraz',
        ),
    ]