# Generated by Django 2.2.6 on 2019-10-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_schedule_teamrankingodi'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.URLField(max_length=1000)),
                ('info', models.CharField(max_length=500)),
            ],
        ),
    ]
