# Generated by Django 4.2 on 2023-04-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "layanan_app",
            "0006_beda_nama_dokumen_pembeda_beda_nama_kk_beda_nama_ktp_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (1, "Penduduk"),
                    (2, "Petugas Desa"),
                    (3, "Kepala Desa"),
                    (0, "Admin"),
                ],
                null=True,
            ),
        ),
    ]
