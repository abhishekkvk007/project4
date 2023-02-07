# Generated by Django 4.1.5 on 2023-01-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
