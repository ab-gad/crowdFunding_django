# Generated by Django 4.0.2 on 2022-02-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test_simulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_simulation', models.CharField(max_length=50)),
                ('tags_simulation', models.CharField(max_length=20)),
                ('rate_simulation', models.IntegerField()),
            ],
        ),
    ]