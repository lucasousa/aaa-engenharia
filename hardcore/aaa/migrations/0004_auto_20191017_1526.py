# Generated by Django 2.2.6 on 2019-10-17 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aaa', '0003_auto_20191017_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aaa',
            options={'ordering': ['name'], 'verbose_name': 'AAA', 'verbose_name_plural': 'AAAs'},
        ),
    ]
