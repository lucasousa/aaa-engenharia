# Generated by Django 2.2.6 on 2019-12-06 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0011_auto_20191024_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='athletic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA'),
        ),
    ]
