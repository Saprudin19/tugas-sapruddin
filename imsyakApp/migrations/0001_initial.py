# Generated by Django 4.2 on 2023-05-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jadwalModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tanggal', models.CharField(max_length=70)),
                ('Imsyak', models.TimeField()),
                ('Subuh', models.TimeField()),
                ('Terbit', models.TimeField()),
                ('Duha', models.TimeField()),
                ('Asar', models.TimeField()),
                ('Magrib', models.TimeField()),
                ('Isya', models.TimeField()),
            ],
        ),
    ]