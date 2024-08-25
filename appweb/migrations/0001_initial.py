# Generated by Django 5.1 on 2024-08-17 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('theme', models.CharField(max_length=250)),
                ('synopsis', models.CharField(max_length=500)),
            ],
        ),
    ]
