# Generated by Django 2.1.5 on 2019-01-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190121_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stopped',
            field=models.BooleanField(default=False),
        ),
    ]