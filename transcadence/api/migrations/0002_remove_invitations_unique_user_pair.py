# Generated by Django 4.2.16 on 2024-11-24 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='invitations',
            name='unique_user_pair',
        ),
    ]
