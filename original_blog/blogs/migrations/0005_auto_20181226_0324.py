# Generated by Django 2.1.1 on 2018-12-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20181225_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='origin',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
