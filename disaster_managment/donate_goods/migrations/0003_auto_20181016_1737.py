# Generated by Django 2.1.2 on 2018-10-16 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate_goods', '0002_auto_20181016_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donate_goods',
            old_name='Vehicles',
            new_name='Vehicles_Numbers',
        ),
    ]
