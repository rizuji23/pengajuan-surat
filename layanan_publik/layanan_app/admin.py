from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.


class CustomUser(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'role'
    )

    fieldsets = (
        (("Personal Info"), {
         "fields": ("first_name", "last_name", "nik", 'no_hp', 'jenis_kelamin', 'alamat')}),
        (("Account Info"), {
         "fields": ("username", "email", "password", "role")}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role'),
            },
        ),
    )


class NikahCustom(admin.ModelAdmin):
    list_display = ('nik', 'mempelai_pria', 'mempelai_wanita',
                    'nama_wali', 'created_at', 'updated_at')


class SuratKelahiranCustom(admin.ModelAdmin):
    list_display = ('nik', 'nama_bayi', 'nama_ibu', 'nama_ayah',
                    'anak_ke', 'created_at', 'updated_at')


class SuratPindahCustom(admin.ModelAdmin):
    list_display = ('nik', 'alamat_asal', 'pindah_ke', 'pengikut',
                    'keterangan', 'created_at', 'updated_at')


class SkckCustom(admin.ModelAdmin):
    list_display = ('nik', 'keterangan', 'keperluan',
                    'created_at', 'updated_at')


class SkuCustom(admin.ModelAdmin):
    list_display = ('nik', 'nama_usaha', 'jenis_usaha',
                    'alamat_usaha', 'keterangan', 'created_at', 'updated_at')


class SktmKesCustom(admin.ModelAdmin):
    list_display = ('nik', 'nama_anggota_keluarga', 'hubungan',
                    'keterangan', 'created_at', 'updated_at')


class SktmPendCustom(admin.ModelAdmin):
    list_display = ('nik', 'nama_tanggungan', 'jml_tanggungan',
                    'hubungan_tanggungan', 'keterangan', 'created_at', 'updated_at')


class DomisiliCustom(admin.ModelAdmin):
    list_display = ('nik', 'keterangan', 'masa_berlaku',
                    'created_at', 'updated_at')


class BedaNamaCustom(admin.ModelAdmin):
    list_display = ('nik', 'dokumen_keliru', 'dokumen_benar',
                    'keterangan', 'created_at', 'updated_at')


class SuratKematianCustom(admin.ModelAdmin):
    list_display = ('nik', 'nama_wafat', 'penyebab', 'hari_tanggal_wafat',
                    'pelapor', 'hubungan_pelapor', 'created_at', 'updated_at')


class LaporanCustom(admin.ModelAdmin):
    list_display = ('id_laporan', 'get_nik', 'id_user', 'jenis_surat',
                    'is_active', 'created_at', 'updated_at')


admin.site.register(User, CustomUser)
admin.site.register(Nikah, NikahCustom)
admin.site.register(Surat_Kelahiran, SuratKelahiranCustom)
admin.site.register(Surat_Pindah, SuratPindahCustom)
admin.site.register(Skck, SkckCustom)
admin.site.register(Sku, SkuCustom)
admin.site.register(Sktm_Kes, SktmKesCustom)
admin.site.register(Sktm_Pend, SktmPendCustom)
admin.site.register(Domisili, DomisiliCustom)
admin.site.register(Beda_Nama, BedaNamaCustom)
admin.site.register(Surat_Kematian, SuratKematianCustom)
admin.site.register(Laporan, LaporanCustom)
