from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    PENDUDUK = 1
    PETUGAS_DESA = 2
    KEPALA_DESA = 3
    ADMIN = 0

    ROLE_CHOICES = (
        (PENDUDUK, 'Penduduk'),
        (PETUGAS_DESA, 'Petugas Desa'),
        (KEPALA_DESA, 'Kepala Desa'),
        (ADMIN, 'Admin')
    )

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True)
    nik = models.BigIntegerField(null=True)
    alamat = models.TextField(null=True)
    jenis_kelamin = models.CharField(null=True, max_length=50)
    no_hp = models.BigIntegerField(null=True)
    ttl = models.CharField(max_length=100, null=True)
    agama = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    pekerjaan = models.CharField(max_length=100, null=True)
    kewarganegaraan = models.CharField(max_length=100, null=True)


class Laporan(models.Model):
    ACTIVE_CHOICES = (
        (0, 'not_active'),
        (1, 'active'),
        (2, 'progress_kepala_desa'),
        (3, 'ditolak')
    )

    id = models.AutoField(primary_key=True)
    id_laporan = models.CharField(max_length=100)
    kode_surat = models.CharField(max_length=100, null=True)
    jenis_surat = models.CharField(max_length=100)
    id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_active = models.PositiveSmallIntegerField(
        choices=ACTIVE_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.jenis_surat + ' (' + self.id_user.first_name + ' ' + self.id_user.last_name + ')'

    def get_nik(self):
        return self.id_user.nik


class Nikah(models.Model):
    id = models.AutoField(primary_key=True)
    id_nikah = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    nik = models.BigIntegerField()
    mempelai_pria = models.CharField(max_length=100)
    mempelai_wanita = models.CharField(max_length=100)
    nama_wali = models.CharField(max_length=100)
    surat_rt_rw = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp = models.FileField(
        max_length=200, upload_to='all/', null=True)
    kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    akta_lahir = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ijazah = models.FileField(
        max_length=200, upload_to='all/', null=True)
    foto_pas_1 = models.FileField(
        max_length=200, upload_to='all/', null=True)
    foto_pas_2 = models.FileField(
        max_length=200, upload_to='all/', null=True)
    surat_belum_nikah = models.FileField(
        max_length=200, upload_to='all/', null=True)
    surat_persetujuan = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Surat_Kelahiran(models.Model):
    id = models.AutoField(primary_key=True)
    id_surat_kelahiran = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    nik = models.BigIntegerField()
    nama_bayi = models.CharField(max_length=100)
    ttl = models.CharField(max_length=100)
    jenis_kelamin_anak = models.CharField(max_length=100)
    hari_jam_lahir = models.CharField(max_length=100)
    anak_ke = models.IntegerField()
    nama_ayah = models.CharField(max_length=100)
    nama_ibu = models.CharField(max_length=100)
    surat_rt_rw = models.FileField(
        max_length=200, upload_to='all/', null=True)
    surat_dokter = models.FileField(
        max_length=200, upload_to='all/', null=True)
    kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Surat_Pindah(models.Model):
    id = models.AutoField(primary_key=True)
    id_surat_pindah = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    nik = models.BigIntegerField()
    alamat_asal = models.TextField()
    pindah_ke = models.TextField()
    pengikut = models.TextField()
    keterangan = models.TextField()
    surat_rt_rw = models.FileField(
        max_length=200, upload_to='all/', null=True)
    kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp = models.FileField(
        max_length=200, upload_to='all/', null=True)
    pas_foto = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Skck(models.Model):
    id = models.AutoField(primary_key=True)
    id_skck = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    nik = models.BigIntegerField()
    keterangan = models.TextField()
    keperluan = models.TextField()
    sim = models.FileField(
        max_length=200, upload_to='all/', null=True)
    kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    akta = models.FileField(
        max_length=200, upload_to='all/', null=True)
    pas_foto = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sktm_Kes(models.Model):
    id = models.AutoField(primary_key=True)
    id_sktm_kes = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    nik = models.BigIntegerField()
    nama_anggota_keluarga = models.CharField(max_length=100)
    hubungan = models.CharField(max_length=100)
    keterangan = models.TextField()
    surat_pengantar = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp = models.FileField(
        max_length=200, upload_to='all/', null=True)
    kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Surat_Kematian(models.Model):
    id = models.AutoField(primary_key=True)
    id_surat_kematian = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    nik = models.BigIntegerField()
    nama_wafat = models.CharField(max_length=100)
    penyebab = models.CharField(max_length=100)
    hari_tanggal_wafat = models.CharField(max_length=100)
    pelapor = models.CharField(max_length=100)
    hubungan_pelapor = models.CharField(max_length=100)
    surat_keterangan = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp_kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp_pasangan = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp_kk_pelapor = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sku(models.Model):
    id = models.AutoField(primary_key=True)
    id_sku = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    nik = models.BigIntegerField()
    nama_usaha = models.CharField(max_length=100)
    jenis_usaha = models.CharField(max_length=100)
    alamat_usaha = models.CharField(max_length=100)
    keterangan = models.TextField()
    surat_pengantar = models.FileField(
        max_length=200, upload_to='all/', null=True)
    kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp = models.FileField(
        max_length=200, upload_to='all/', null=True)
    pas_foto = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Domisili(models.Model):
    id = models.AutoField(primary_key=True)
    id_domisili = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(
        Laporan, on_delete=models.CASCADE, null=True)
    nik = models.BigIntegerField(max_length=100)
    keterangan = models.TextField()
    masa_berlaku = models.CharField(max_length=100)
    kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp = models.FileField(
        max_length=200, upload_to='all/', null=True)
    pas_foto = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Beda_Nama(models.Model):
    id = models.AutoField(primary_key=True)
    id_beda_nama = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    nik = models.BigIntegerField()
    dokumen_keliru = models.FileField(
        max_length=200, upload_to='dokumen_keliru/', null=True)
    dokumen_benar = models.FileField(
        max_length=200, upload_to='dokumen_benar/', null=True)
    keterangan = models.TextField()
    surat_pengantar = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp = models.FileField(
        max_length=200, upload_to='all/', null=True)
    kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    dokumen_pembeda = models.FileField(
        max_length=200, upload_to='all/', null=True)
    surat_pernyataan = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sktm_Pend(models.Model):
    id = models.AutoField(primary_key=True)
    id_sktm_pend = models.CharField(max_length=100)
    id_laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE)
    nik = models.BigIntegerField()
    nama_tanggungan = models.CharField(max_length=100)
    jml_tanggungan = models.IntegerField()
    hubungan_tanggungan = models.CharField(max_length=100)
    keterangan = models.TextField()
    surat_pengantar = models.FileField(
        max_length=200, upload_to='all/', null=True)
    ktp = models.FileField(
        max_length=200, upload_to='all/', null=True)
    kk = models.FileField(
        max_length=200, upload_to='all/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
