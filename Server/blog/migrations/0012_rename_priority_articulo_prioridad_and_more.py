# Generated by Django 4.1.2 on 2022-12-16 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_articulo_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='priority',
            new_name='Prioridad',
        ),
        migrations.RenameField(
            model_name='articulo',
            old_name='alt_image',
            new_name='alt_imagen',
        ),
        migrations.RenameField(
            model_name='articulo',
            old_name='created',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='articulo',
            old_name='created_at',
            new_name='creado_el',
        ),
    ]
