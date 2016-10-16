from django.contrib import admin
from .models import Buku

# Register your models here.
class BukuAdmin (admin.ModelAdmin):
    list_display = ['no_buku','judul_buku', 'pengarang', 'jenis_buku', 'jumlah']
    list_filter = ['jenis_buku']
    search_fields = ['no_buku', 'judul_buku']
    list_per_page = 25

admin.site.register(Buku, BukuAdmin)