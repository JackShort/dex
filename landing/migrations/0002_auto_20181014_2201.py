# Generated by Django 2.1.1 on 2018-10-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
