# Generated by Django 4.2.8 on 2024-02-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qgisfeed', '0013_alter_qgisfeedentry_publish_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyqgisuservisit',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
