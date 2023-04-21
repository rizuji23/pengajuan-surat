from django import forms
from .models import *


class ModelAllDisabledFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        form_fields = self.fields
        for key in form_fields.keys():
            form_fields[key].disabled = True
            form_fields[key].widget.attrs['class'] = 'form-control'


class ModelAllClassMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        form_fields = self.fields
        for key in form_fields.keys():
            form_fields[key].widget.attrs['class'] = 'form-control'


class UserDetailForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'nik', 'jenis_kelamin', 'ttl',
                  'pekerjaan', 'status', 'agama', 'email', 'no_hp', 'alamat')


class UserForm(ModelAllClassMixin, forms.ModelForm):
    JENIS_KELAMIN = (
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan')
    )

    STATUS = (
        ('Menikah', 'Menikah'),
        ('Belum Menikah', 'Belum Menikah')
    )
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    nik = forms.CharField(max_length=30, widget=forms.NumberInput)
    jenis_kelamin = forms.ChoiceField(
        choices=JENIS_KELAMIN, widget=forms.Select)
    ttl = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    pekerjaan = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select)
    agama = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100, widget=forms.EmailInput)
    no_hp = forms.CharField(max_length=100, widget=forms.NumberInput)
    alamat = forms.CharField(widget=forms.Textarea)

    username = forms.CharField(max_length=100)
    password = forms.CharField(
        max_length=100, widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'nik', 'jenis_kelamin', 'ttl',
                  'pekerjaan', 'status', 'agama', 'email', 'no_hp', 'alamat', 'username', 'password')


class SuratForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Laporan
        fields = '__all__'


class NikahForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Nikah
        fields = '__all__'


class Surat_KelahiranForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Surat_Kelahiran
        fields = '__all__'


class Surat_PindahForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Surat_Pindah
        fields = '__all__'


class SkckForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Skck
        fields = '__all__'


class Sktm_KesForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Sktm_Kes
        fields = '__all__'


class Surat_KematianForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Surat_Kematian
        fields = '__all__'


class SkuForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Sku
        fields = '__all__'


class DomisiliForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Domisili
        fields = '__all__'


class Beda_NamaForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Beda_Nama
        fields = '__all__'


class Sktm_PendForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Sktm_Pend
        fields = '__all__'
