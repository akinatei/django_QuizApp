# Generated by Django 4.2.1 on 2024-04-25 11:53

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]