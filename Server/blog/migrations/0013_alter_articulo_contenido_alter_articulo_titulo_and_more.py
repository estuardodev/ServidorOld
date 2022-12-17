# Generated by Django 4.1.2 on 2022-12-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_priority_articulo_prioridad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='contenido',
            field=models.TextField(max_length=5000, verbose_name='Escríbe tu contenido no mayor a 5000 caracteres'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(max_length=150, verbose_name='Escríbe tu título no mayor a 150 caracteres'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='url',
            field=models.CharField(max_length=500, verbose_name='/articulo/page-1'),
        ),
    ]