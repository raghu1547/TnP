# Generated by Django 2.1.1 on 2018-09-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science & Engineering'), ('ECE', 'Electronics & Communication Engineering'), ('ECE', 'Electrical & Electronics Engineering'), ('ME', 'Mechanical Engineering'), ('CHE', 'Chemical Engineering'), ('CE', 'Civil Engineering'), ('MME', 'Metallurgical & Materials Engineering'), ('BIO', 'Biotechnology')], default='CSE', max_length=3)),
            ],
        ),
    ]
