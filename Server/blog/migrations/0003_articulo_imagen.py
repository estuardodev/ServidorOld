# Generated by Django 4.1.2 on 2022-12-16 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_articulo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog/articulos/images/'),
        ),
    ]