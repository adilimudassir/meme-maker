# Generated by Django 4.1 on 2022-08-24 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("meme", "0008_alter_meme_name_alter_submission_memeid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="memeID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="meme.meme"
            ),
        ),
    ]
