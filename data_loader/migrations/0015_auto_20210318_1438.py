# Generated by Django 3.1.7 on 2021-03-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0014_auto_20210315_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='action_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='d_done',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='d_next',
            field=models.DateField(),
        ),
    ]
