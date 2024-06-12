# Generated by Django 4.2.13 on 2024-06-12 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default='1990-12-28'),
            preserve_default=False,
        ),
    ]
