# Generated by Django 4.1.4 on 2023-02-06 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finetunedmodels',
            old_name='user_id',
            new_name='user_email',
        ),
    ]