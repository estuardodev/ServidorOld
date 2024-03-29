# Generated by Django 4.1.7 on 2023-02-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0005_country_data_of_ipuser_for_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_of_ipuser_for_country',
            name='fk_countries',
        ),
        migrations.RemoveField(
            model_name='data_of_ipuser_for_country',
            name='fk_ipusers',
        ),
        migrations.AddField(
            model_name='ipusers',
            name='city',
            field=models.CharField(db_column='City', max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='ipusers',
            name='code_zip',
            field=models.CharField(db_column='CodePostal', max_length=60, null=True, verbose_name='Code Postal'),
        ),
        migrations.AddField(
            model_name='ipusers',
            name='isp',
            field=models.CharField(db_column='ISP', max_length=255, null=True, verbose_name='ISP'),
        ),
        migrations.AddField(
            model_name='ipusers',
            name='lat',
            field=models.CharField(db_column='latitude', max_length=255, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='ipusers',
            name='lon',
            field=models.CharField(db_column='langitude', max_length=255, null=True, verbose_name='Longitude'),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Data_of_IPUser_for_Country',
        ),
    ]
