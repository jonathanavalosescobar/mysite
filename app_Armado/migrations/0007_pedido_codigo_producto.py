# Generated by Django 2.1.3 on 2019-11-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Armado', '0006_auto_20191110_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='codigo_producto',
            field=models.CharField(default=4, max_length=4),
            preserve_default=False,
        ),
    ]