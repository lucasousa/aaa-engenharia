# Generated by Django 2.2.8 on 2019-12-06 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0026_auto_20191206_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='athletic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA'),
        ),
    ]