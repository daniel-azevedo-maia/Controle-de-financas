# Generated by Django 3.2.9 on 2023-04-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlefinancas', '0005_auto_20230415_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='comprovante',
            field=models.FileField(upload_to='comprovantes/'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='comprovante',
            field=models.FileField(upload_to='comprovantes/'),
        ),
    ]
