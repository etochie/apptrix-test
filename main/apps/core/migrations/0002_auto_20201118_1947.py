# Generated by Django 3.0.8 on 2020-11-18 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navbarmodel',
            options={'ordering': ['date']},
        ),
    ]
