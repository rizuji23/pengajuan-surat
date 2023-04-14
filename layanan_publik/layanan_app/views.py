from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import uuid
from django.db.models import Count
from .forms import *


def get_id():
    return str(uuid.uuid4())[:8]
# Create your views here.


def index(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'login.html', context)


def logins(request):
    context = {
        'title': 'Home',
    }

    return render(request, 'login.html', context)


def register(request):
    context = {
        'title': 'Pendaftaran'
    }
    return render(request, 'register.html', context)


def do_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.get_role_display() == "Penduduk":
                return HttpResponseRedirect('penduduk/dashboard')

        else:
            messages.add_message(request, messages.ERROR,
                                 "Username atau Password Salah!")
            return HttpResponseRedirect('login')
    else:
        return HttpResponseForbidden()


@login_required
def dashboard_penduduk(request):
    get_detail = get_object_or_404(User, username=request.user)
    get_laporan = Laporan.objects.filter(
        id_user_id=request.user.pk).order_by('-id')

    count_all = Laporan.objects.filter(
        id_user_id=request.user.pk).count()
    count_not = Laporan.objects.filter(
        id_user_id=request.user.pk, is_active=0).count()
    count_done = Laporan.objects.filter(
        id_user_id=request.user.pk, is_active=1).count()

    context = {
        'title': 'Dashboard Penduduk',
        'data': get_detail,
        'laporan': get_laporan,
        'count_all': count_all,
        'count_not': count_not,
        'count_done': count_done
    }
    return render(request, 'dashboard_penduduk.html', context)


@login_required
def add_pengajuan(request):
    get_detail = get_object_or_404(User, username=request.user)
    context = {
        'title': 'Tambah Pengajuan Surat',
        'data': get_detail
    }

    return render(request, 'add_pengajuan.html', context)


@login_required
def detail_pengajuan(request, id):
    get_detail = get_object_or_404(User, username=request.user)
    get_laporan = Laporan.objects.get(id_laporan=id)
    form = SuratForm(instance=get_laporan)
    context = {
        'title': 'Tambah Pengajuan Surat',
        'data': get_detail,
        'form': form
    }

    return render(request, 'detail_pengajuan.html', context)


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('login')


@login_required
def save_nikah(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        mempelai_pria = request.POST['mempelai_pria']
        mempelai_wanita = request.POST['mempelai_wanita']
        nama_wali = request.POST['nama_wali']
        jenis_surat = request.POST['jenis_surat']
        surat_rt_rw = request.FILES['surat_rt_rw']
        ktp = request.FILES['ktp']
        kk = request.FILES['kk']
        akta_lahir = request.FILES['akta_lahir']
        ijazah = request.FILES['ijazah']
        foto_pas_1 = request.FILES['foto_pas_1']
        foto_pas_2 = request.FILES['foto_pas_2']
        surat_belum_nikah = request.FILES['surat_belum_nikah']
        surat_persetujuan = request.FILES['surat_persetujuan']
        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save nikah
            id_nikah = get_id()
            nikah = Nikah(id_nikah=id_nikah, id_laporan_id=get_laporan.id, nik=nik,
                          mempelai_pria=mempelai_pria, mempelai_wanita=mempelai_wanita, nama_wali=nama_wali, surat_rt_rw=surat_rt_rw, ktp=ktp, kk=kk, akta_lahir=akta_lahir, ijazah=ijazah, foto_pas_1=foto_pas_1, foto_pas_2=foto_pas_2, surat_belum_nikah=surat_belum_nikah, surat_persetujuan=surat_persetujuan)
            nikah.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()


@login_required
def save_surat_kelahiran(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        nama_bayi = request.POST['nama_bayi']
        tanggal_lahir = request.POST['tanggal_lahir']
        jenis_kelamin_anak = request.POST['jenis_kelamin_anak']
        hari_jam_lahir = request.POST['hari_jam_lahir']
        anak_ke = request.POST['anak_ke']
        nama_ibu = request.POST['nama_ibu']
        nama_ayah = request.POST['nama_ayah']
        jenis_surat = request.POST['jenis_surat']
        surat_rt_rw = request.FILES['surat_rt_rw']
        surat_dokter = request.FILES['surat_dokter']
        kk = request.FILES['kk']
        ktp = request.FILES['ktp']
        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_surat_kelahiran = get_id()
            child_laporan = Surat_Kelahiran(id_surat_kelahiran=id_surat_kelahiran, id_laporan_id=get_laporan.id, nik=nik,
                                            nama_bayi=nama_bayi, ttl=tanggal_lahir, jenis_kelamin_anak=jenis_kelamin_anak, hari_jam_lahir=hari_jam_lahir, anak_ke=anak_ke, nama_ayah=nama_ayah, nama_ibu=nama_ibu, surat_rt_rw=surat_rt_rw, surat_dokter=surat_dokter, kk=kk, ktp=ktp)
            child_laporan.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()


@login_required
def save_surat_pindah(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        alamat_asal = request.POST['alamat_asal']
        pindah_ke = request.POST['pindah_ke']
        pengikut = request.POST['pengikut']
        keterangan = request.POST['keterangan']
        jenis_surat = request.POST['jenis_surat']
        surat_rt_rw = request.FILES['surat_rt_rw']
        kk = request.FILES['kk']
        ktp = request.FILES['ktp']
        pas_foto = request.FILES['pas_foto']
        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_surat_pindah = get_id()
            child_laporan = Surat_Pindah(id_surat_pindah=id_surat_pindah, id_laporan_id=get_laporan.id, nik=nik,
                                         alamat_asal=alamat_asal, pindah_ke=pindah_ke, pengikut=pengikut, keterangan=keterangan, surat_rt_rw=surat_rt_rw, kk=kk, ktp=ktp, pas_foto=pas_foto)
            child_laporan.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()


@login_required
def save_skck(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        keperluan = request.POST['keperluan']
        keterangan = request.POST['keterangan']
        jenis_surat = request.POST['jenis_surat']
        sim = request.FILES['sim']
        kk = request.FILES['kk']
        akta = request.FILES['akta']
        pas_foto = request.FILES['pas_foto']
        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_skck = get_id()
            child_laporan = Skck(id_skck=id_skck, id_laporan_id=get_laporan.id, nik=nik,
                                 keterangan=keterangan, keperluan=keperluan, sim=sim, kk=kk, akta=akta, pas_foto=pas_foto)
            child_laporan.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()


@login_required
def save_sku(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        nama_usaha = request.POST['nama_usaha']
        jenis_usaha = request.POST['jenis_usaha']
        alamat_usaha = request.POST['alamat_usaha']
        keterangan = request.POST['keterangan']
        jenis_surat = request.POST['jenis_surat']
        surat_pengantar = request.FILES['surat_pengantar']
        kk = request.FILES['kk']
        ktp = request.FILES['ktp']
        pas_foto = request.FILES['pas_foto']
        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_sku = get_id()
            child_laporan = Sku(id_sku=id_sku, id_laporan_id=get_laporan.id, nik=nik,
                                nama_usaha=nama_usaha, jenis_usaha=jenis_usaha, alamat_usaha=alamat_usaha, keterangan=keterangan, surat_pengantar=surat_pengantar, kk=kk, ktp=ktp, pas_foto=pas_foto)
            child_laporan.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()


@login_required
def save_sktm_kes(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        nama_anggota_keluarga = request.POST['nama_anggota_keluarga']
        hubungan = request.POST['hubungan']
        keterangan = request.POST['keterangan']
        jenis_surat = request.POST['jenis_surat']
        surat_pengantar = request.FILES['surat_pengantar']
        ktp = request.FILES['ktp']
        kk = request.FILES['kk']
        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_sktm_kes = get_id()
            child_laporan = Sktm_Kes(id_sktm_kes=id_sktm_kes, id_laporan_id=get_laporan.id, nik=nik,
                                     nama_anggota_keluarga=nama_anggota_keluarga, hubungan=hubungan, keterangan=keterangan, surat_pengantar=surat_pengantar, ktp=ktp, kk=kk)
            child_laporan.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()


@login_required
def save_sktm_pend(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        nama_tanggungan = request.POST['nama_tanggungan']
        jml_tanggungan = request.POST['jml_tanggungan']
        hubungan_tanggungan = request.POST['hubungan_tanggungan']
        keterangan = request.POST['keterangan']
        jenis_surat = request.POST['jenis_surat']
        surat_pengantar = request.FILES['surat_pengantar']
        ktp = request.FILES['ktp']
        kk = request.FILES['kk']
        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_sktm_pend = get_id()
            child_laporan = Sktm_Pend(id_sktm_pend=id_sktm_pend, id_laporan_id=get_laporan.id, nik=nik,
                                      nama_tanggungan=nama_tanggungan, jml_tanggungan=jml_tanggungan, hubungan_tanggungan=hubungan_tanggungan, keterangan=keterangan, surat_pengantar=surat_pengantar, ktp=ktp, kk=kk)
            child_laporan.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()


@login_required
def save_domisili(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        keterangan = request.POST['keterangan']
        masa_berlaku = request.POST['masa_berlaku']
        jenis_surat = request.POST['jenis_surat']
        kk = request.FILES['kk']
        ktp = request.FILES['ktp']
        pas_foto = request.FILES['pas_foto']

        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_domisili = get_id()
            child_laporan = Domisili(id_domisili=id_domisili, id_laporan_id=get_laporan.id, nik=nik,
                                     keterangan=keterangan, masa_berlaku=masa_berlaku, kk=kk, ktp=ktp, pas_foto=pas_foto)
            child_laporan.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()


@login_required
def save_beda_nama(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        dokumen_keliru = request.FILES['dokumen_keliru']
        dokumen_benar = request.FILES['dokumen_benar']
        keterangan = request.POST['keterangan']
        jenis_surat = request.POST['jenis_surat']
        surat_pengantar = request.FILES['surat_pengantar']
        ktp = request.FILES['ktp']
        kk = request.FILES['kk']
        dokumen_pembeda = request.FILES['dokumen_pembeda']
        surat_pernyataan = request.FILES['surat_pernyataan']
        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_beda_nama = get_id()
            child_laporan = Beda_Nama(id_beda_nama=id_beda_nama, id_laporan_id=get_laporan.id, nik=nik,
                                      dokumen_keliru=dokumen_keliru, dokumen_benar=dokumen_benar, keterangan=keterangan, surat_pengantar=surat_pengantar, ktp=ktp, kk=kk, dokumen_pembeda=dokumen_pembeda, surat_pernyataan=surat_pernyataan)
            child_laporan.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()


@login_required
def save_surat_kematian(request):
    if request.method == "POST":
        print(request.POST)
        get_detail = get_object_or_404(User, username=request.user)
        nik = request.POST['nik']
        nama_wafat = request.POST['nama_wafat']
        penyebab = request.POST['penyebab']
        hari_tanggal_wafat = request.POST['hari_tanggal_wafat']
        pelapor = request.POST['pelapor']
        hubungan_pelapor = request.POST['hubungan_pelapor']
        jenis_surat = request.POST['jenis_surat']
        surat_keterangan = request.FILES['surat_keterangan']
        ktp_kk = request.FILES['ktp_kk']
        ktp_pasangan = request.FILES['ktp_pasangan']
        ktp_kk_pelapor = request.FILES['ktp_kk_pelapor']
        id_laporan = get_id()

        # save to laporan
        try:
            laporan = Laporan(id_laporan=id_laporan, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_surat_kematian = get_id()
            child_laporan = Surat_Kematian(id_surat_kematian=id_surat_kematian, id_laporan_id=get_laporan.id, nik=nik,
                                           nama_wafat=nama_wafat, penyebab=penyebab, hari_tanggal_wafat=hari_tanggal_wafat, pelapor=pelapor, hubungan_pelapor=hubungan_pelapor, surat_keterangan=surat_keterangan, ktp_kk=ktp_kk, ktp_pasangan=ktp_pasangan, ktp_kk_pelapor=ktp_kk_pelapor)
            child_laporan.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Pengajuan Surat berhasil.")
            return HttpResponseRedirect('penduduk/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()
