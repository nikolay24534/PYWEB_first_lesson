# Generated by Django 3.1.7 on 2021-03-14 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статьи', 'verbose_name_plural': 'Статьи'},
        ),
    ]
