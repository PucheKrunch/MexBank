# Generated by Django 3.2.3 on 2021-06-03 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_empleado_superior_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_tarjeta',
            name='saldo',
            field=models.FloatField(default=0),
        ),
    ]
