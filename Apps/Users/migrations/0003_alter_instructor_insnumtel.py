# Generated by Django 4.0.6 on 2022-08-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_cliente_clicode_alter_cliente_cliema_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='InsNumTel',
            field=models.IntegerField(),
        ),
    ]
