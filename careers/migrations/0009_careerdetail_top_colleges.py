# Generated by Django 5.1.1 on 2025-02-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("careers", "0008_remove_careerdetail_skills_required"),
    ]

    operations = [
        migrations.AddField(
            model_name="careerdetail",
            name="top_colleges",
            field=models.JSONField(default=list),
        ),
    ]
