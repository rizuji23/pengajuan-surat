from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import uuid
from django.db.models import Count
from .forms import *
from django.db.models import Q
from django.contrib.auth.hashers import make_password
import datetime
import qrcode
from django.conf import settings
from django.forms.models import model_to_dict


def get_id():
    return str(uuid.uuid4())[:8]
# Create your views here.


def index(request):
    context = {
        'title': 'Pelayanan & Pengajuan Surat Desa Cileunyi'
    }
    return render(request, 'index.html', context)


def logins(request):
    context = {
        'title': 'Login',
    }

    return render(request, 'login.html', context)


def register(request):
    context = {
        'title': 'Pendaftaran Penduduk'
    }
    return render(request, 'register.html', context)


def do_register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        nik = request.POST['nik']
        jenis_kelamin = request.POST['jenis_kelamin']
        ttl = request.POST['ttl']
        agama = request.POST['agama']
        pekerjaan = request.POST['pekerjaan']
        status = request.POST['status']
        kewarganegaraan = request.POST['kewarganegaraan']
        alamat = request.POST['alamat']
        username = request.POST['username']
        email = request.POST['email']
        no_hp = request.POST['no_hp']
        password = request.POST['password']

        try:
            user_1 = User(username=username, email=email, password=make_password(password), first_name=first_name, last_name=last_name, nik=nik, jenis_kelamin=jenis_kelamin,
                          ttl=ttl, agama=agama, pekerjaan=pekerjaan, status=status, kewarganegaraan=kewarganegaraan, alamat=alamat, no_hp=no_hp, role=1)

            user_1.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Register penduduk berhasil.")
            return HttpResponseRedirect('register')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('register')

    else:
        return HttpResponseForbidden()


def do_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.get_role_display() == "Penduduk":
                return HttpResponseRedirect('penduduk/dashboard')
            elif user.get_role_display() == "Petugas Desa":
                return HttpResponseRedirect('petugas/dashboard')
            elif user.get_role_display() == "Kepala Desa":
                return HttpResponseRedirect('kepala/dashboard')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Username atau Password Salah!")
            return HttpResponseRedirect('login')
    else:
        return HttpResponseForbidden()


@login_required
def surat(request):
    return render(request, 'surat.html')


def nikah_surat(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Nikah, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)
    context = {
        'title': "SURAT KETERANGAN MENIKAH",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'kepala': get_kepala
    }
    return render(request, 'surat/nikah.html', context)


def surat_kematian(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Surat_Kematian, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)

    context = {
        'title': "SURAT KETERANGAN KEMATIAN",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'kepala': get_kepala
    }
    return render(request, 'surat/surat_kematian.html', context)


def surat_pindah(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Surat_Pindah, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)
    context = {
        'title': "SURAT KETERANGAN PINDAH",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'kepala': get_kepala
    }
    return render(request, 'surat/surat_pindah.html', context)


def surat_kelahiran(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Surat_Kelahiran, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)
    context = {
        'title': "SURAT KETERANGAN KELAHIRAN",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'kepala': get_kepala
    }
    return render(request, 'surat/surat_kelahiran.html', context)


def skck(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Skck, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)
    context = {
        'title': "SURAT KETERANGAN CATATAN KEPOLISIAN",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'kepala': get_kepala
    }
    return render(request, 'surat/skck.html', context)


def sku(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Sku, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)
    context = {
        'title': "SURAT KETERANGAN USAHA",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'get_kepala': get_kepala
    }
    return render(request, 'surat/sku.html', context)


def sktm_kes(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Sktm_Kes, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)
    context = {
        'title': "SURAT KETERANGAN TIDAK MAMPU",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'kepala': get_kepala
    }
    return render(request, 'surat/sktm_kes.html', context)


def sktm_pend(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Sktm_Pend, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)
    context = {
        'title': "SURAT KETERANGAN TIDAK MAMPU",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'kepala': get_kepala
    }
    return render(request, 'surat/sktm_pend.html', context)


def domisili(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Domisili, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)
    context = {
        'title': "SURAT KETERANGAN DOMISILI",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'kepala': get_kepala
    }
    return render(request, 'surat/domisili.html', context)


def beda_nama(request, id):
    get_user = get_object_or_404(User, username=request.user)
    get_laporan = get_object_or_404(Laporan, id_laporan=id)
    get_data = get_object_or_404(Beda_Nama, id_laporan_id=get_laporan.id)
    get_kepala = get_object_or_404(User, id=get_laporan.id_kepala_id)
    context = {
        'title': "SURAT KETERANGAN BEDA NAMA",
        'kode_surat': get_laporan.kode_surat,
        'laporan': get_laporan,
        'data': get_data,
        'user': get_user,
        'kepala': get_kepala
    }
    return render(request, 'surat/beda_nama.html', context)


@login_required
def dashboard_penduduk(request):
    get_detail = get_object_or_404(User, username=request.user, role=1)
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
def dashboard_petugas(request):
    get_detail = get_object_or_404(User, username=request.user, role=2)
    get_laporan = Laporan.objects.filter(Q(is_active=0) | Q(
        is_active=2) | Q(is_active=3)).order_by('-id')

    count_all = Laporan.objects.all().count()
    count_not = Laporan.objects.filter(is_active=0).count()
    count_done = Laporan.objects.filter(is_active=1).count()

    context = {
        'title': 'Dashboard Petugas',
        'data': get_detail,
        'laporan': get_laporan,
        'count_all': count_all,
        'count_not': count_not,
        'count_done': count_done
    }
    return render(request, 'dashboard_petugas.html', context)


@login_required
def dashboard_kepala(request):
    get_detail = get_object_or_404(User, username=request.user, role=3)
    get_laporan = Laporan.objects.filter(Q(is_active=0) | Q(
        is_active=2) | Q(is_active=3)).order_by('-id')

    count_all = Laporan.objects.all().count()
    count_not = Laporan.objects.filter(is_active=0).count()
    count_done = Laporan.objects.filter(is_active=1).count()

    context = {
        'title': 'Dashboard Kepala',
        'data': get_detail,
        'laporan': get_laporan,
        'count_all': count_all,
        'count_not': count_not,
        'count_done': count_done
    }
    return render(request, 'dashboard_kepala.html', context)


@login_required
def list_surat_selesai(request):
    get_detail = get_object_or_404(
        User, Q(role=2) | Q(role=3), username=request.user)
    get_laporan = Laporan.objects.filter(Q(is_active=1)).order_by('-id')

    count_all = Laporan.objects.all().count()
    count_not = Laporan.objects.filter(is_active=0).count()
    count_done = Laporan.objects.filter(is_active=1).count()

    context = {
        'title': 'Dashboard Petugas',
        'data': get_detail,
        'laporan': get_laporan,
        'count_all': count_all,
        'count_not': count_not,
        'count_done': count_done
    }

    return render(request, 'list_surat_selesai.html', context)


def get_detail_form(type_laporan, **kwargs):
    if type_laporan == 'nikah':
        instance = Nikah.objects.get(**kwargs)
        return NikahForm(instance=instance)
    elif type_laporan == 'surat_kelahiran':
        instance = Surat_Kelahiran.objects.get(**kwargs)
        return Surat_KelahiranForm(instance=instance)
    elif type_laporan == 'surat_pindah':
        instance = Surat_Pindah.objects.get(**kwargs)
        return Surat_PindahForm(instance=instance)
    elif type_laporan == 'skck':
        instance = Skck.objects.get(**kwargs)
        return SkckForm(instance=instance)
    elif type_laporan == 'sku':
        instance = Sku.objects.get(**kwargs)
        return SkuForm(instance=instance)
    elif type_laporan == 'sktm_kes':
        instance = Sktm_Kes.objects.get(**kwargs)
        return Sktm_KesForm(instance=instance)
    elif type_laporan == 'sktm_pend':
        instance = Sktm_Pend.objects.get(**kwargs)
        return Sktm_PendForm(instance=instance)
    elif type_laporan == 'domisili':
        instance = Domisili.objects.get(**kwargs)
        return DomisiliForm(instance=instance)
    elif type_laporan == 'beda_nama':
        instance = Beda_Nama.objects.get(**kwargs)
        return Beda_NamaForm(instance=instance)
    elif type_laporan == 'surat_kematian':
        instance = Surat_Kematian.objects.get(**kwargs)
        return Surat_KematianForm(instance=instance)


@login_required
def download_report(request):
    if request.method == "POST":
        filter_laporan = request.POST['filter']

        if filter_laporan == "0":
            hari_ini = datetime.datetime.now().date()
            laporan = Laporan.objects.filter(created_at__date=hari_ini)
            count_setuju = Laporan.objects.filter(
                created_at__date=hari_ini, is_active=1).count()
            count_tolak = Laporan.objects.filter(
                created_at__date=hari_ini, is_active=3).count()
            context = {
                'data': laporan,
                'date': hari_ini,
                'count_setuju': count_setuju,
                'count_tolak': count_tolak
            }

            return render(request, 'download_report.html', context)

        elif filter_laporan == "1":
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            laporan = Laporan.objects.filter(
                created_at__range=(start_date, end_date))
            count_setuju = Laporan.objects.filter(
                created_at__range=(start_date, end_date), is_active=1).count()
            count_tolak = Laporan.objects.filter(
                created_at__range=(start_date, end_date), is_active=3).count()
            context = {
                'data': laporan,
                'date': "{} ~ {}".format(start_date, end_date),
                'count_setuju': count_setuju,
                'count_tolak': count_tolak
            }

            return render(request, 'download_report.html', context)

        else:
            return HttpResponse('error invalid')
    else:
        return HttpResponseForbidden()


@login_required
def data_user(request):
    get_detail = get_object_or_404(
        User, Q(role=2) | Q(role=3), username=request.user)
    user = User.objects.filter(
        Q(is_active=1), Q(role=1)).order_by('-id')

    count_all = User.objects.filter(
        Q(is_active=1), Q(role=1)).count()

    context = {
        'title': 'Dashboard Petugas',
        'data': get_detail,
        'user': user,
        'count_all': count_all,

    }

    return render(request, 'data_user.html', context)


@login_required
def delete_user(request, id):
    get_detail = get_object_or_404(
        User, Q(role=2) | Q(role=3), username=request.user)
    get_user = User.objects.get(id=id)
    get_user.delete()

    messages.add_message(request, messages.SUCCESS,
                         "Penduduk berhasil dihapus.")
    return HttpResponseRedirect('/data_user')


@login_required
def add_pengajuan(request):
    get_detail = get_object_or_404(User, username=request.user)
    get_penduduk = User.objects.filter(role=1)
    context = {
        'title': 'Tambah Pengajuan Surat',
        'data': get_detail,
        'penduduk': get_penduduk,
    }

    return render(request, 'add_pengajuan.html', context)


@login_required
def get_user(request):
    id = request.GET['id']
    get_penduduk = get_object_or_404(User, id=id)
    return JsonResponse({'status': True, 'data': model_to_dict(get_penduduk)})


@login_required
def detail_pengajuan(request, id):
    get_detail = get_object_or_404(User, username=request.user)
    get_laporan = Laporan.objects.get(id_laporan=id)
    form = SuratForm(instance=get_laporan)
    detail_form = get_detail_form(
        get_laporan.jenis_surat, id_laporan_id=get_laporan.id)
    context = {
        'title': 'Tambah Pengajuan Surat',
        'data': get_detail,
        'form': form,
        'detail_form': detail_form,
        'data_laporan': get_laporan
    }

    return render(request, 'detail_pengajuan.html', context)


@login_required
def detail_user(request, id):
    get_detail = get_object_or_404(
        User, Q(role=2) | Q(role=3), username=request.user)
    get_laporan = User.objects.get(id=id)
    form = UserDetailForm(instance=get_laporan)
    context = {
        'title': 'Detail User',
        'data': get_detail,
        'form': form,
    }

    return render(request, 'detail_user.html', context)


@login_required
def add_user(request):
    get_detail = get_object_or_404(
        User, Q(role=2) | Q(role=3), username=request.user)
    form = UserForm()
    context = {
        'title': 'Tambah Data User',
        'data': get_detail,
        'form': form,
    }

    return render(request, 'add_user.html', context)


@login_required
def report(request):
    get_detail = get_object_or_404(
        User, Q(role=2) | Q(role=3), username=request.user)
    context = {
        'title': 'Report Laporan',
        'data': get_detail,
    }

    return render(request, 'report.html', context)


@login_required
def edit_user(request, id):
    get_detail = get_object_or_404(
        User, Q(role=2) | Q(role=3), username=request.user)
    get_user = get_object_or_404(User, id=id)
    form = UserForm(instance=get_user)
    context = {
        'title': 'Edit Data User',
        'data': get_detail,
        'form': form,
        'id': id
    }

    return render(request, 'edit_user.html', context)


@login_required
def do_add_user(request):
    get_object_or_404(
        User, Q(role=2) | Q(role=3), username=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.instance.role = 1
                form.instance.password = make_password(form.password)
                form.save()
            except Exception as e:
                messages.add_message(request, messages.ERROR,
                                     "Error: " + str(e))
                return HttpResponseRedirect('/data_user')

            messages.add_message(request, messages.SUCCESS,
                                 "Penduduk berhasil ditambah.")
            return HttpResponseRedirect('/data_user')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Penduduk gagal ditambah.")
            return HttpResponseRedirect('/data_user')

    else:
        return HttpResponseForbidden()


@login_required
def do_edit_user(request, id):
    get_object_or_404(
        User, Q(role=2) | Q(role=3), username=request.user)
    if request.method == 'POST':
        get_user = get_object_or_404(User, id=id)
        form = UserForm(request.POST or None, instance=get_user)
        if form.is_valid():
            try:
                form.fields.pop('password')
                form.save()
            except Exception as e:
                messages.add_message(request, messages.ERROR,
                                     "Error: " + str(e))
                return HttpResponseRedirect('/data_user')

            messages.add_message(request, messages.SUCCESS,
                                 "Penduduk berhasil ditambah.")
            return HttpResponseRedirect('/data_user')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Penduduk gagal ditambah.")
            return HttpResponseRedirect('/data_user')

    else:
        return HttpResponseForbidden()


def qr_generate(id_laporan):
    url = "http://localhost:8000/verify/{}".format(id_laporan)
    img = qrcode.make(url)
    img_name = "qr_{}.png".format(id_laporan)
    try:
        img.save(settings.MEDIA_ROOT + '/' + img_name)
        return True
    except Exception as e:
        return e


@login_required
def acc_surat(request):
    if request.method == 'POST':
        get_detail = get_object_or_404(
            User, Q(role=2) | Q(role=3), username=request.user)
        id_laporan = request.POST['id_laporan']
        status = request.POST['status']
        change = get_object_or_404(Laporan, id_laporan=id_laporan)

        if status == 'petugas':
            # change status to acc kepala desa
            try:
                change.is_active = 2
                change.save()
                return JsonResponse({'status': True, 'data': "created"})
            except Exception as e:
                messages.add_message(request, messages.ERROR,
                                     "Terjadi kesalahan " + str(e))
                return JsonResponse({'status': False, 'data': str(e)})
        else:
            qr = qr_generate(id_laporan)
            if qr:
                try:
                    change.is_active = 1
                    change.id_kepala_id = get_detail.id
                    change.save()
                    return JsonResponse({'status': True, 'data': "created"})
                except Exception as e:
                    return JsonResponse({'status': False, 'data': str(e)})
    else:
        return HttpResponseForbidden()


@login_required
def tolak_surat(request):
    if request.method == 'POST':
        get_detail = get_object_or_404(
            User, Q(role=2) | Q(role=3), username=request.user)
        id_laporan = request.POST['id_laporan']
        status = request.POST['status']
        change = get_object_or_404(Laporan, id_laporan=id_laporan)

        if status == 'petugas':
            # change status to acc kepala desa
            try:
                change.is_active = 3
                change.save()
                return JsonResponse({'status': True, 'data': "created"})
            except Exception as e:
                messages.add_message(request, messages.ERROR,
                                     "Terjadi kesalahan " + str(e))
                return JsonResponse({'status': False, 'data': str(e)})
        else:
            try:
                change.is_active = 3
                change.save()
                return JsonResponse({'status': True, 'data': "created"})
            except Exception as e:
                return JsonResponse({'status': False, 'data': str(e)})
    else:
        return HttpResponseForbidden()


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('login')


def get_code_surat():
    last_data = Laporan.objects.last()
    return "511.1/0{}/Ekbang".format(int(last_data.id) + 1)

def verify(request, id):
    get_laporan = get_object_or_404(Laporan, id_laporan=id)

    context = {
        'data': get_laporan,
    }

    return render(request, 'verify.html', context)


@login_required
def save_nikah(request):
    if request.method == "POST":
        print(request.POST)
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
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
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save nikah
            id_nikah = get_id()
            nikah = Nikah(id_nikah=id_nikah, id_laporan_id=get_laporan.id, nik=nik,
                          mempelai_pria=mempelai_pria, mempelai_wanita=mempelai_wanita, nama_wali=nama_wali, surat_rt_rw=surat_rt_rw, ktp=ktp, kk=kk, akta_lahir=akta_lahir, ijazah=ijazah, foto_pas_1=foto_pas_1, foto_pas_2=foto_pas_2, surat_belum_nikah=surat_belum_nikah, surat_persetujuan=surat_persetujuan)
            nikah.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

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
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
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
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_surat_kelahiran = get_id()
            child_laporan = Surat_Kelahiran(id_surat_kelahiran=id_surat_kelahiran, id_laporan_id=get_laporan.id, nik=nik,
                                            nama_bayi=nama_bayi, ttl=tanggal_lahir, jenis_kelamin_anak=jenis_kelamin_anak, hari_jam_lahir=hari_jam_lahir, anak_ke=anak_ke, nama_ayah=nama_ayah, nama_ibu=nama_ibu, surat_rt_rw=surat_rt_rw, surat_dokter=surat_dokter, kk=kk, ktp=ktp)
            child_laporan.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

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
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
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
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_surat_pindah = get_id()
            child_laporan = Surat_Pindah(id_surat_pindah=id_surat_pindah, id_laporan_id=get_laporan.id, nik=nik,
                                         alamat_asal=alamat_asal, pindah_ke=pindah_ke, pengikut=pengikut, keterangan=keterangan, surat_rt_rw=surat_rt_rw, kk=kk, ktp=ktp, pas_foto=pas_foto)
            child_laporan.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

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
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
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
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_skck = get_id()
            child_laporan = Skck(id_skck=id_skck, id_laporan_id=get_laporan.id, nik=nik,
                                 keterangan=keterangan, keperluan=keperluan, sim=sim, kk=kk, akta=akta, pas_foto=pas_foto)
            child_laporan.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

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
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
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
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_sku = get_id()
            child_laporan = Sku(id_sku=id_sku, id_laporan_id=get_laporan.id, nik=nik,
                                nama_usaha=nama_usaha, jenis_usaha=jenis_usaha, alamat_usaha=alamat_usaha, keterangan=keterangan, surat_pengantar=surat_pengantar, kk=kk, ktp=ktp, pas_foto=pas_foto)
            child_laporan.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

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
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
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
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_sktm_kes = get_id()
            child_laporan = Sktm_Kes(id_sktm_kes=id_sktm_kes, id_laporan_id=get_laporan.id, nik=nik,
                                     nama_anggota_keluarga=nama_anggota_keluarga, hubungan=hubungan, keterangan=keterangan, surat_pengantar=surat_pengantar, ktp=ktp, kk=kk)
            child_laporan.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

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
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
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
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_sktm_pend = get_id()
            child_laporan = Sktm_Pend(id_sktm_pend=id_sktm_pend, id_laporan_id=get_laporan.id, nik=nik,
                                      nama_tanggungan=nama_tanggungan, jml_tanggungan=jml_tanggungan, hubungan_tanggungan=hubungan_tanggungan, keterangan=keterangan, surat_pengantar=surat_pengantar, ktp=ktp, kk=kk)
            child_laporan.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

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
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
        keterangan = request.POST['keterangan']
        masa_berlaku = request.POST['masa_berlaku']
        jenis_surat = request.POST['jenis_surat']
        kk = request.FILES['kk']
        ktp = request.FILES['ktp']
        pas_foto = request.FILES['pas_foto']

        id_laporan = get_id()

        # save to laporan
        try:
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_domisili = get_id()
            child_laporan = Domisili(id_domisili=id_domisili, id_laporan_id=get_laporan.id, nik=nik,
                                     keterangan=keterangan, masa_berlaku=masa_berlaku, kk=kk, ktp=ktp, pas_foto=pas_foto)
            child_laporan.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

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
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
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
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_beda_nama = get_id()
            child_laporan = Beda_Nama(id_beda_nama=id_beda_nama, id_laporan_id=get_laporan.id, nik=nik,
                                      dokumen_keliru=dokumen_keliru, dokumen_benar=dokumen_benar, keterangan=keterangan, surat_pengantar=surat_pengantar, ktp=ktp, kk=kk, dokumen_pembeda=dokumen_pembeda, surat_pernyataan=surat_pernyataan)
            child_laporan.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

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
        nik = request.POST['nik']
        get_detail = get_object_or_404(User, nik=nik)
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
            kode_surat = get_code_surat()
            laporan = Laporan(id_laporan=id_laporan, kode_surat=kode_surat, jenis_surat=jenis_surat,
                              id_user_id=get_detail.pk, is_active=0)
            laporan.save()

            # get laporan
            get_laporan = get_object_or_404(Laporan, id_laporan=id_laporan)

            # save child laporan
            id_surat_kematian = get_id()
            child_laporan = Surat_Kematian(id_surat_kematian=id_surat_kematian, id_laporan_id=get_laporan.id, nik=nik,
                                           nama_wafat=nama_wafat, penyebab=penyebab, hari_tanggal_wafat=hari_tanggal_wafat, pelapor=pelapor, hubungan_pelapor=hubungan_pelapor, surat_keterangan=surat_keterangan, ktp_kk=ktp_kk, ktp_pasangan=ktp_pasangan, ktp_kk_pelapor=ktp_kk_pelapor)
            child_laporan.save()

            if request.user.role == 1:
                messages.add_message(request, messages.SUCCESS,
                                     "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('penduduk/dashboard')
            elif request.user.role == 2:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('petugas/dashboard')
            elif request.user.role == 3:
                messages.add_message(
                    request, messages.SUCCESS, "Pengajuan Surat berhasil.")
                return HttpResponseRedirect('kepala/dashboard')

        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 "Terjadi kesalahan " + str(e))
            return HttpResponseRedirect('penduduk/dashboard')

    else:
        return HttpResponseForbidden()
