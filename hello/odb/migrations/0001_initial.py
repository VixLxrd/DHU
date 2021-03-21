# Generated by Django 3.1.7 on 2021-03-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.PositiveIntegerField()),
                ('date', models.PositiveIntegerField()),
                ('aqua_hot', models.PositiveIntegerField()),
                ('aqua_cold', models.PositiveIntegerField()),
                ('el', models.PositiveIntegerField()),
                ('temp', models.PositiveIntegerField()),
            ],
        ),
    ]
