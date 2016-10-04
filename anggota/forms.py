from django.forms import ModelForm
from django import forms
from .models import Anggota

class AnggotaForm(ModelForm):
    # class meta untuk mendefinisikan ModelForm
    class Meta:
        model = Anggota
        fields = ['nrp', 'nama', 'alamat', 'no_telp','foto']
        # labels = {
        #     'nrp' : "NRP",
        #     'nama' : "Nama",
        #     'alamat' : "Alamat",
        #     'no_telp' : "No Telpon",
        #     'foto' : "Foto"
        # }
        widgets = {
            'alamat': forms.Textarea(attrs={ 'cols':50, 'rows': 10 }),
        }
