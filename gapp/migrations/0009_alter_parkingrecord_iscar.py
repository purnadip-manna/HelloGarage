# Generated by Django 4.1.1 on 2022-09-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gapp", "0008_alter_otp_carno"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parkingrecord",
            name="isCar",
            field=models.BooleanField(default=True),
        ),
    ]