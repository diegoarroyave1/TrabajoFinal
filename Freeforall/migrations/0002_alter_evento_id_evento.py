# Generated by Django 4.0.6 on 2022-11-01 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freeforall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='id_evento',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
