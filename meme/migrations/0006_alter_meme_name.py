# Generated by Django 4.1 on 2022-08-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meme", "0005_alter_meme_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meme",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
