# Generated by Django 4.2.6 on 2023-10-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleprojectapp', '0002_level_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='desc',
            field=models.TextField(),
        ),
    ]
