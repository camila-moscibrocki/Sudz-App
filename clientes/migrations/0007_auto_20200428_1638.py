# Generated by Django 3.0.5 on 2020-04-28 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20180210_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='age',
            new_name='cnpj',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='last_name',
            new_name='razao_social',
        ),
        migrations.RemoveField(
            model_name='person',
            name='salary',
        ),
    ]
