# Generated by Django 5.0.1 on 2024-01-11 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageUrl',
            field=models.CharField(default='', max_length=255),
        ),
    ]
