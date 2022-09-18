# Generated by Django 4.1.1 on 2022-09-18 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Garage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("bike_slots", models.IntegerField(default=0)),
                ("car_slots", models.IntegerField(default=0)),
                ("f_bike_slots", models.IntegerField(default=0)),
                ("f_car_slots", models.IntegerField(default=0)),
                ("bike_rate", models.DecimalField(decimal_places=2, max_digits=5)),
                ("car_rate", models.DecimalField(decimal_places=2, max_digits=5)),
                ("address", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ParkingRecord",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("phnno", models.BigIntegerField()),
                ("carno", models.CharField(max_length=15)),
                ("regtime", models.DateTimeField(auto_now_add=True)),
                ("exittime", models.DateTimeField()),
                ("slotno", models.CharField(max_length=10)),
                ("amt", models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ("ispaid", models.BooleanField(default=False)),
                (
                    "garage_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="gapp.garage"
                    ),
                ),
            ],
        ),
    ]
