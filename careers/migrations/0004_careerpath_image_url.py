# Generated by Django 5.1.1 on 2025-02-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("careers", "0003_alter_careerpath_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="careerpath",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
