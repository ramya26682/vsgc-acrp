# Generated by Django 2.1.1 on 2020-09-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acrpapp', '0002_auto_20200908_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designapp',
            name='Upload',
            field=models.FileField(max_length=256, null=True, upload_to=''),
        ),
    ]
