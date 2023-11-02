# Generated by Django 4.2.6 on 2023-10-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finances", "0002_restaurant"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Restaurant",
        ),
        migrations.AlterField(
            model_name="account",
            name="initial_balance",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]
