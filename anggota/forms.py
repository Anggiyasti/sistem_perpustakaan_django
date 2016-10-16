from django.forms import ModelForm, widgets
from django import forms
from .models import Anggota

class AnggotaForm(ModelForm):
    # class meta untuk mendefinisikan ModelForm
    class Meta:

        model = Anggota
        JENIS_KELAMIN_CHOICES = (
        ('laki-laki', 'Laki-laki'),
        ('perempuan', 'Perempuan'),
         )
        fields = ['nrp', 'nama', 'alamat', 'no_telp','foto', 'jenis_kelamin']
        # labels = {
        #     'nrp' : "NRP",
        #     'nama' : "Nama",
        #     'alamat' : "Alamat",
        #     'no_telp' : "No Telpon",
        #     'foto' : "Foto"
        # }

        alamat= forms.Textarea(attrs={ 'cols':50, 'rows': 10 })
        jenis_kelamin = forms.TypedChoiceField(choices = JENIS_KELAMIN_CHOICES, widget = forms.RadioSelect)

# class AnggotaForm(forms.Form):
#         JENIS_KELAMIN_CHOICES = (
#                     ('laki-laki', 'Laki-laki'),
#                     ('perempuan', 'Perempuan'),
#                      )
#
#         nrp = forms.CharField()
#         nama = forms.CharField()
#         alamat = forms.CharField(widget=forms.Textarea)
#         no_telp = forms.CharField()
#         jenis_kelamin = forms.ChoiceField(
#             choices=JENIS_KELAMIN_CHOICES, widget=forms.RadioSelect(attrs={'class' : 'Radio'})
#         )
#         foto =forms.ImageField()



