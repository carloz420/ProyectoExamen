# Generated by Django 4.0.5 on 2022-07-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluacion2App', '0004_producto_delete_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
