# Generated by Django 3.2.9 on 2021-11-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meeteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
