# Generated by Django 5.0.6 on 2024-05-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UserSignIn", "0003_customuser_groups_customuser_is_superuser_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]