from django.forms import ModelForm
from django import forms
from .models import Peminjaman
from buku.models import Buku
from anggota.models import Anggota

class PeminjamanForm(ModelForm):
    # class meta untuk mendefinisikan ModelForm
    class Meta:
        model = Peminjaman
        fields = ['nrp', 'no_buku', 'tgl_pinjam', 'tgl_kembali']
        labels = {
            'nrp' : "NRP",
            'no_buku' : "No Buku",
            'tgl_pinjam' : "Tanggal Peminjaman",
            'tgl_kembali' : "Tanggal Pengembalian",
        }
        error_messages = {
            'nrp' : {
                'required' : 'NRP harus diisi'
            },
            'no_buku' : {
                'required' : 'No Buku harus diisi'
            },
            'tgl_pinjam' : {
                'required' : 'Tanggal Peminjaman harus diisi'
            },
            'tgl_kembali' : {
                'required' : 'Tanggal Pengembalian harus diisi'
            }
        }