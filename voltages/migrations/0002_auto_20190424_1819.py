# Generated by Django 2.2 on 2019-04-24 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voltages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
