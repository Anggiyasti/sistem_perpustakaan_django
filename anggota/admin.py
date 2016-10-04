from django.contrib import admin
from anggota.models import *
# Register your models here.
class AnggotaAdmin (admin.ModelAdmin):
    list_display = ['nrp','nama', 'alamat', 'no_telp', 'foto']
    list_filter = ()
    search_fields = ['nrp', 'nama']
    list_per_page = 25

admin.site.register(Anggota, AnggotaAdmin)