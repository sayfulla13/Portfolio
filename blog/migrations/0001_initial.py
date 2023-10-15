# Generated by Django 4.2.6 on 2023-10-13 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('urls', models.URLField(blank=True)),
            ],
        ),
    ]