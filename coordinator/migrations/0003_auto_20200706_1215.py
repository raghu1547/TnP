# Generated by Django 3.0.8 on 2020-07-06 12:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coordinator', '0002_announcement_companies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='datePublished',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
