# Generated by Django 3.2 on 2021-05-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_applicant_details_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant_details',
            name='Upload',
            field=models.FileField(max_length=256, null=True, upload_to='media/upload'),
        ),
    ]