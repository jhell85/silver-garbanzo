# Generated by Django 3.2.7 on 2021-09-22 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ebook',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ebooks.ebook'),
            preserve_default=False,
        ),
    ]