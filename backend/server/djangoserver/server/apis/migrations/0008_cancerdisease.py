# Generated by Django 3.1.7 on 2021-03-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_auto_20210304_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancerDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius_mean', models.FloatField()),
                ('perimeter_mean', models.FloatField()),
                ('area_mean', models.FloatField()),
                ('concavity_mean', models.FloatField()),
                ('concave_points_mean', models.FloatField()),
                ('radius_se', models.FloatField()),
                ('area_se', models.FloatField()),
                ('radius_worst', models.FloatField()),
                ('texture_worst', models.FloatField()),
                ('perimeter_worst', models.FloatField()),
                ('area_worst', models.FloatField()),
                ('compactness_worst', models.FloatField()),
                ('concavity_worst', models.FloatField()),
                ('concave_points_worst', models.FloatField()),
            ],
        ),
    ]