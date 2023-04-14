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

    path('penduduk/detail_pengajuan/<str:id>', views.detail_pengajuan,
         name="detail_pengajuan"),
]
