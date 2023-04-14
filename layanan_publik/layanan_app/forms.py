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
