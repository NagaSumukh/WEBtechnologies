# Generated by Django 2.2.6 on 2019-11-01 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0007_playersa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('phno', models.IntegerField()),
                ('feedback', models.CharField(max_length=10000)),
            ],
        ),
    ]