# Generated by Django 4.1.1 on 2022-09-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gapp", "0003_parkingrecord_iscar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parkingrecord",
            name="exittime",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]