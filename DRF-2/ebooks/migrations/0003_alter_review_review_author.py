# Generated by Django 3.2.7 on 2021-09-23 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ebooks', '0002_review_ebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
