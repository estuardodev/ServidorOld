# Generated by Django 4.1.7 on 2023-06-13 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_rename_alt_imagen_articulo_alt_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]