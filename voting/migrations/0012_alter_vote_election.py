# Generated by Django 4.2.8 on 2024-04-05 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0011_election_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.election'),
        ),
    ]