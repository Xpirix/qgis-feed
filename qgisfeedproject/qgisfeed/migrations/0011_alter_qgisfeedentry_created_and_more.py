# Generated by Django 4.2.7 on 2023-11-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qgisfeed', '0010_alter_qgisfeedentry_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qgisfeedentry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='qgisfeedentry',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modification date'),
        ),
    ]