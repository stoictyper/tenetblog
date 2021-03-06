# Generated by Django 3.1.1 on 2020-09-14 10:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='aimage',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Add picture'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
