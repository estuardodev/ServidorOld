# Generated by Django 4.1.2 on 2022-12-16 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_articulo_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='created',
            new_name='date',
        ),
    ]
