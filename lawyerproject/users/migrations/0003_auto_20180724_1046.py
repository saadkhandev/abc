# Generated by Django 2.0.7 on 2018-07-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180724_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
