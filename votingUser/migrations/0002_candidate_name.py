# Generated by Django 4.2.8 on 2024-03-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='name',
            field=models.CharField(default='Ganesh', max_length=255),
        ),
    ]
