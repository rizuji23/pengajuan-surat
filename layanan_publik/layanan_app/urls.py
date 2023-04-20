from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.logins, name="logins"),
    path('register', views.register, name="register"),
    path('do_login', views.do_login, name="do_login"),
    path('penduduk/dashboard', views.dashboard_penduduk,
         name="dashboard_penduduk_view"),
    path('add_pengajuan', views.add_pengajuan, name="add_pengajuan"),
    path('logout', views.logout_view, name="logout"),

    # save pengajuan
    path('save_nikah', views.save_nikah, name="save_nikah"),
    path('save_surat_kelahiran', views.save_surat_kelahiran,
         name="save_surat_kelahiran"),
    path('save_surat_pindah', views.save_surat_pindah,
         name="save_surat_pindah"),
    path('save_skck', views.save_skck,
         name="save_skck"),
    path('save_sku', views.save_sku,
         name="save_sku"),
    path('save_sktm_kes', views.save_sktm_kes,
         name="save_sktm_kes"),
    path('save_sktm_pend', views.save_sktm_pend,
         name="save_sktm_pend"),
    path('save_domisili', views.save_domisili,
         name="save_domisili"),
    path('save_beda_nama', views.save_beda_nama,
         name="save_beda_nama"),
    path('save_surat_kematian', views.save_surat_kematian,
         name="save_surat_kematian"),

    path('detail_pengajuan/<str:id>', views.detail_pengajuan,
         name="detail_pengajuan"),

    path('petugas/dashboard', views.dashboard_petugas,
         name="dashboard_petugas_view"),

    path('api/acc_surat', views.acc_surat, name="acc_surat"),
    path('api/tolak_surat', views.tolak_surat, name="tolak_surat"),

    path('list_done', views.list_surat_selesai,
         name="list_done"),

    path('kepala/dashboard', views.dashboard_kepala, name="dashboard_kepala"),

    path('download/surat', views.surat, name="surat"),
    path('download/surat/nikah/<str:id>',
         views.nikah_surat, name="nikah_surat"),
    path('download/surat/surat_kematian/<str:id>',
         views.surat_kematian, name="surat_kematian"),
    path('download/surat/surat_pindah/<str:id>',
         views.surat_pindah, name="surat_pindah"),
    path('download/surat/surat_kelahiran/<str:id>',
         views.surat_kelahiran, name="surat_kelahiran"),
    path('download/surat/skck/<str:id>',
         views.skck, name="skck"),
    path('download/surat/sku/<str:id>',
         views.sku, name="sku"),
    path('download/surat/sktm_kes/<str:id>',
         views.sktm_kes, name="sktm_kes"),
    path('download/surat/sktm_pend/<str:id>',
         views.sktm_pend, name="sktm_pend"),
    path('download/surat/domisili/<str:id>',
         views.domisili, name="domisili"),
    path('download/surat/beda_nama/<str:id>',
         views.beda_nama, name="beda_nama"),

]
