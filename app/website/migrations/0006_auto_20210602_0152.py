# Generated by Django 3.2.3 on 2021-06-02 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210602_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_tarjeta',
            name='cliente_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.cliente'),
        ),
        migrations.AddField(
            model_name='c_tarjeta',
            name='num_tarjeta',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='d_tarjeta',
            name='cliente_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.cliente'),
        ),
        migrations.AddField(
            model_name='d_tarjeta',
            name='num_tarjeta',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
