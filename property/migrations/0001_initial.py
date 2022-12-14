# Generated by Django 4.1.3 on 2022-11-11 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import property.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Varanasi', max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='facing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facing', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name_plural': 'facing',
            },
        ),
        migrations.CreateModel(
            name='overlooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overlooking', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'overlooking',
            },
        ),
        migrations.CreateModel(
            name='pincode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=6)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.city')),
            ],
        ),
        migrations.CreateModel(
            name='possession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possession', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'possession',
            },
        ),
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('street_address', models.CharField(default='', max_length=250)),
                ('landmark', models.CharField(blank=True, max_length=150)),
                ('area', models.PositiveIntegerField()),
                ('price', models.PositiveBigIntegerField()),
                ('main_picture', models.ImageField(upload_to=property.models.get_file_path)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.city')),
                ('pincode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.pincode')),
            ],
            options={
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
            name='property_ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_ownership', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'property_ownership',
            },
        ),
        migrations.CreateModel(
            name='transaction_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'transaction_types',
            },
        ),
        migrations.CreateModel(
            name='property_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=property.models.get_file_path)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
            options={
                'verbose_name_plural': 'property_images',
            },
        ),
        migrations.CreateModel(
            name='property_features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=250)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
            options={
                'verbose_name_plural': 'property_features',
            },
        ),
        migrations.CreateModel(
            name='property_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.PositiveIntegerField()),
                ('breadth', models.PositiveIntegerField()),
                ('floors_allowed', models.PositiveIntegerField()),
                ('boundary_wall', models.BooleanField(default=False)),
                ('width_of_facing_road', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('facing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.facing')),
                ('overlooking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.overlooking')),
                ('possession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.possession')),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='property.property')),
                ('property_ownership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property_ownership')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.transaction_type')),
            ],
            options={
                'verbose_name_plural': 'property_details',
            },
        ),
    ]
