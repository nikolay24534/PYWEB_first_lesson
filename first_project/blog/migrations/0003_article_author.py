# Generated by Django 3.1.7 on 2021-03-26 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210314_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, related_name='authors', to='auth.user'),
            preserve_default=False,
        ),
    ]
