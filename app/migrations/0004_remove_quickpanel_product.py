# Generated by Django 3.2.6 on 2021-09-14 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_quickpanel_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quickpanel',
            name='product',
        ),
    ]
