# Generated by Django 3.0.8 on 2021-08-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210813_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=2, default='', max_digits=8),
        ),
    ]
