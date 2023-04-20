from django.forms import ModelForm
from .models import *


class ModelAllDisabledFormMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        form_fields = self.fields
        for key in form_fields.keys():
            form_fields[key].disabled = True
            form_fields[key].widget.attrs['class'] = 'form-control'


class SuratForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Laporan
        fields = '__all__'


class NikahForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Nikah
        fields = '__all__'


class Surat_KelahiranForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Surat_Kelahiran
        fields = '__all__'


class Surat_PindahForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Surat_Pindah
        fields = '__all__'


class SkckForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Skck
        fields = '__all__'


class Sktm_KesForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Sktm_Kes
        fields = '__all__'


class Surat_KematianForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Surat_Kematian
        fields = '__all__'


class SkuForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Sku
        fields = '__all__'


class DomisiliForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Domisili
        fields = '__all__'


class Beda_NamaForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Beda_Nama
        fields = '__all__'


class Sktm_PendForm(ModelAllDisabledFormMixin, ModelForm):
    class Meta:
        model = Sktm_Pend
        fields = '__all__'
