# Generated by Django 5.0 on 2023-12-30 17:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("urna", "0002_alter_candidato_numero"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidato",
            name="numero",
            field=models.IntegerField(
                unique=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(99),
                ],
                verbose_name="Número",
            ),
        ),
    ]
