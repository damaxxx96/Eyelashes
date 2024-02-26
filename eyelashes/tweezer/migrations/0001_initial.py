# Generated by Django 4.2.2 on 2024-02-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ColorModel",
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
                ("color", models.CharField(max_length=50)),
                ("count", models.IntegerField()),
            ],
        ),
    ]