# Generated by Django 4.0.2 on 2022-02-10 12:28

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=20, verbose_name='first name')),
                ('last_name', models.CharField(default='', max_length=20, verbose_name='last name')),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^01[0-2][0-9]{8}$', 'Egyptian phone number is required')], verbose_name='phone')),
                ('avatar', models.ImageField(default='profile_images/default-pic.jpeg', upload_to='profile_images', verbose_name='profile picture')),
                ('country', models.CharField(blank=True, default='', max_length=20, verbose_name='country')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='birthdate')),
                ('fb_account', models.URLField(blank=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
