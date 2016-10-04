from django.contrib import admin
from peminjaman.models import *

# Register your models here.
class PeminjamanAdmin (admin.ModelAdmin):
    list_display = ['nrp','no_buku', 'tgl_pinjam', 'tgl_kembali']
    list_filter = ['tgl_pinjam']
    search_fields = ['nrp', 'no_buku']
    list_per_page = 25

admin.site.register(Peminjaman, PeminjamanAdmin)

class PetugasAdmin (admin.ModelAdmin):
    list_display = ['nama','jabatan', 'foto']
    list_filter = ['jabatan']
    search_fields = ['nama', 'jabatan']
    list_per_page = 25

admin.site.register(Petugas, PetugasAdmin)

class AkunAdmin (admin.ModelAdmin):
    list_display = ['akun','petugas', 'jenis_akun']
    list_filter = ['jenis_akun']
    search_fields = []
    list_per_page = 25

admin.site.register(Akun, AkunAdmin)