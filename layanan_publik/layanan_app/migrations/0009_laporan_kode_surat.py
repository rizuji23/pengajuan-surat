# Generated by Django 4.2 on 2023-04-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("layanan_app", "0008_alter_laporan_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="laporan",
            name="kode_surat",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
