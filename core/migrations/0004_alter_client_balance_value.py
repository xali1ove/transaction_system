# Generated by Django 4.0.4 on 2022-05-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_client_balance_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='balance_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
