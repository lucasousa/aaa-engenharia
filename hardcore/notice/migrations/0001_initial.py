# Generated by Django 2.2.6 on 2019-10-18 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aaa', '0009_auto_20191017_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('athletic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['published_date'],
            },
        ),
    ]
