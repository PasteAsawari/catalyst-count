# Generated by Django 4.2.6 on 2023-10-31 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='current_employee_estimate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='total_employee_estimate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='year_founded',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
