# Generated by Django 2.2.6 on 2019-10-22 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0015_merge_20191022_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='athletic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA'),
        ),
    ]
