# Generated by Django 3.0.5 on 2020-04-29 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20200428_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='cnpj',
            new_name='CNPJ',
        ),
    ]
