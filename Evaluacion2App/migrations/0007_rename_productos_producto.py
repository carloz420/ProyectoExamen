# Generated by Django 4.0.5 on 2022-07-06 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluacion2App', '0006_rename_producto_productos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='productos',
            new_name='producto',
        ),
    ]