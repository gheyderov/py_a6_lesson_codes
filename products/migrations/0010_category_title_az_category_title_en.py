# Generated by Django 4.2.7 on 2024-01-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_blockedips'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_az',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
    ]