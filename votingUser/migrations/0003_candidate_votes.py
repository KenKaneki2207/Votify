# Generated by Django 4.2.8 on 2024-03-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingUser', '0002_candidate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
