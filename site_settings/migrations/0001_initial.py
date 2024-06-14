# Generated by Django 5.0.1 on 2024-01-20 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialMediaSetting",
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
                (
                    "facebook",
                    models.URLField(blank=True, help_text="Enter your Facebook URL"),
                ),
                (
                    "twitter",
                    models.URLField(blank=True, help_text="Enter your Twitter URL"),
                ),
                (
                    "youtube",
                    models.URLField(blank=True, help_text="Enter your Youtube URL"),
                ),
                (
                    "instagram",
                    models.URLField(blank=True, help_text="Enter your Instagram URL"),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
