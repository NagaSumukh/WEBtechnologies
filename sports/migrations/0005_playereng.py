# Generated by Django 2.2.6 on 2019-10-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_auto_20191026_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerEng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('battingstyle', models.CharField(max_length=150)),
                ('bowlingstyle', models.CharField(max_length=150)),
                ('iccrank', models.IntegerField()),
                ('matches', models.IntegerField()),
                ('runs', models.IntegerField()),
                ('wickets', models.IntegerField()),
            ],
        ),
    ]
