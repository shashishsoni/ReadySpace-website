# Generated by Django 5.0.2 on 2024-02-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_rename_attribution_testimonial_attribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='attribution',
            field=models.CharField(max_length=150),
        ),
    ]