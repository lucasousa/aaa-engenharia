# Generated by Django 2.2.6 on 2019-10-22 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0006_merge_20191022_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='athletic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA'),
        ),
    ]