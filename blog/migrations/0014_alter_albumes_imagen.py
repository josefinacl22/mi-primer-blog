# Generated by Django 3.2.25 on 2025-06-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_albumes_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumes',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
