# Generated by Django 3.2.3 on 2021-06-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20210603_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_tarjeta',
            name='dia_corte',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c_tarjeta',
            name='fecha_valida',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c_tarjeta',
            name='num_tarjeta',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='c_tarjeta',
            name='saldo',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='d_tarjeta',
            name='fecha_valida',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='d_tarjeta',
            name='num_tarjeta',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]