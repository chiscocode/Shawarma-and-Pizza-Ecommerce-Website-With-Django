# Generated by Django 3.0.8 on 2021-08-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210811_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid_amount',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='order',
            name='ref',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]