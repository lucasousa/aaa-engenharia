# Generated by Django 2.2.6 on 2019-10-22 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0012_merge_20191018_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='athletic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA'),
        ),
    ]
