# Generated by Django 3.2 on 2021-05-11 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant_details',
            name='Carrer_goals',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]