# Generated by Django 3.1.7 on 2021-03-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0007_auto_20210312_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='comments',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
