# Generated by Django 4.1.3 on 2022-11-13 10:17

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_users_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='no_of_properties_bought',
        ),
        migrations.RemoveField(
            model_name='users',
            name='no_of_properties_sold',
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.ForeignKey(default=(), null=True, on_delete=users.models.gender_default, to='users.gender_of_user'),
        ),
    ]
