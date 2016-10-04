from django.forms import ModelForm
from django import forms
from .models import Buku

class BukuForm(ModelForm):
    # class meta untuk mendefinisikan ModelForm
    class Meta:
        model = Buku
        fields = ['no_buku', 'judul_buku', 'pengarang', 'jenis_buku']
        labels = {
            'no_buku' : "No Buku",
            'judul_buku' : "Judul Buku",
            'pengarang' : "Pengarang",
            'jenis_buku' : "Jenis Buku",
        }
        error_messages = {
            'no_buku' : {
                'required' : 'No Buku harus diisi'
            },
            'judul_buku' : {
                'required' : 'Judul Buku harus diisi'
            },
            'pengarang' : {
                'required' : 'Pengarang harus diisi'
            },
            'jenis_buku' : {
                'required' : 'Jenis Buku harus diisi'
            }
        }