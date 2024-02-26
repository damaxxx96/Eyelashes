# Generated by Django 4.2.2 on 2024-02-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnotherModel",
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
                ("modelname", models.CharField(max_length=100)),
                ("content", models.DecimalField(decimal_places=2, max_digits=6)),
                ("count", models.IntegerField()),
            ],
        ),
    ]
