# Generated by Django 3.1.7 on 2021-03-04 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_auto_20210304_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heartdisease',
            old_name='threstbps',
            new_name='trestbps',
        ),
    ]
