# Generated by Django 3.2.9 on 2021-11-18 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20211118_1458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
