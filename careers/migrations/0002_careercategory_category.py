# Generated by Django 5.1.1 on 2025-02-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("careers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="careercategory",
            name="category",
            field=models.CharField(
                choices=[
                    ("Science", "Science"),
                    ("Commerce", "Commerce"),
                    ("Arts", "Arts"),
                    ("Vocational", "Vocational"),
                    ("Other", "Other"),
                ],
                default="Other",
                max_length=50,
            ),
        ),
    ]
