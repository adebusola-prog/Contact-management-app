# Generated by Django 4.1.3 on 2022-11-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contactapp", "0004_alter_profile_contact_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="address",
            field=models.TextField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="contact_image",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile_pics",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
    ]
