# Generated by Django 4.2 on 2023-05-06 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("layanan_app", "0015_laporan_count_download"),
    ]

    operations = [
        migrations.AlterField(
            model_name="laporan",
            name="count_download",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
