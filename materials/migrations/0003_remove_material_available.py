# Generated by Django 4.2.1 on 2023-09-01 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_material_available_material_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='available',
        ),
    ]
