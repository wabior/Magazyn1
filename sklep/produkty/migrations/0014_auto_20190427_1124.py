# Generated by Django 2.2 on 2019-04-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0013_auto_20190427_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkty',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
