# Generated by Django 4.0.5 on 2022-06-15 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hermanos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hermanos', models.CharField(max_length=42)),
                ('Edad', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='Madre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mama', models.CharField(max_length=42)),
                ('Edad', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Papa', models.CharField(max_length=42)),
                ('Edad', models.IntegerField(verbose_name=2)),
            ],
        ),
    ]
