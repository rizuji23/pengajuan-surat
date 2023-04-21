# Generated by Django 4.2 on 2023-04-21 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("layanan_app", "0012_alter_user_ttl"),
    ]

    operations = [
        migrations.AddField(
            model_name="laporan",
            name="id_kepala",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="id_kepala_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="laporan",
            name="id_petugas",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="id_petugas_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]