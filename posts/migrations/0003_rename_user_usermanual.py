# Generated by Django 3.2.6 on 2021-08-15 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserManual',
        ),
    ]