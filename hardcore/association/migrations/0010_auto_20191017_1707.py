# Generated by Django 2.2.6 on 2019-10-17 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0009_auto_20191017_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='athletic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA'),
        ),
    ]
