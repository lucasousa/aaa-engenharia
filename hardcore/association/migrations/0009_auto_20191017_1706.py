# Generated by Django 2.2.6 on 2019-10-17 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0008_auto_20191017_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='athletic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA'),
        ),
    ]