# Generated by Django 3.1.4 on 2020-12-15 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_buypass_buyticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buypass',
            old_name='duration',
            new_name='durationtype',
        ),
        migrations.RenameField(
            model_name='buypass',
            old_name='gender',
            new_name='gender2',
        ),
        migrations.RenameField(
            model_name='buyticket',
            old_name='gender',
            new_name='gender1',
        ),
        migrations.RenameField(
            model_name='buyticket',
            old_name='stop1',
            new_name='stop01',
        ),
        migrations.RenameField(
            model_name='buyticket',
            old_name='stop2',
            new_name='stop02',
        ),
    ]
