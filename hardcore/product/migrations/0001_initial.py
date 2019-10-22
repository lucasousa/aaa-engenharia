# Generated by Django 2.2.6 on 2019-10-22 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aaa', '0009_auto_20191017_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(upload_to='')),
                ('athletic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['name'],
            },
        ),
    ]
