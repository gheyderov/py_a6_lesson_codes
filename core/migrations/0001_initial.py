# Generated by Django 4.2.7 on 2023-12-01 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=40, verbose_name='email')),
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('message', models.TextField(max_length=255, verbose_name='message')),
            ],
        ),
    ]