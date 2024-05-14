# Generated by Django 5.0.6 on 2024-05-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UserSignIn", "0005_remove_customuser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="firstName",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name="customuser",
            name="lastName",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
