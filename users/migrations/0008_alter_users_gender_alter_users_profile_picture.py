# Generated by Django 4.1.3 on 2022-11-11 20:14

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_users_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.ForeignKey(default=(), null=True, on_delete=users.models.gender_default, to='users.gender_of_user'),
        ),
        migrations.AlterField(
            model_name='users',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.get_file_path),
        ),
    ]
