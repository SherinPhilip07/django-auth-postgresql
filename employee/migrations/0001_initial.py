# Generated by Django 3.2.5 on 2021-07-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
    ]