# Generated by Django 4.0.6 on 2022-12-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_in_work',
            field=models.BooleanField(default=False),
        ),
    ]
