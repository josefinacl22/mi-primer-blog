# Generated by Django 3.2.25 on 2025-06-20 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_albumes_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumes',
            name='imagen',
        ),
    ]
