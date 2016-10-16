from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import os.path
from anggota.models import *
from buku.models import Buku



# Create your models here.
class Peminjaman (models.Model):
    nrp = models.ForeignKey(Anggota)
    no_buku = models.ForeignKey(Buku)
    tgl_pinjam = models.DateField()
    tgl_kembali = models.DateField()
    status = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nrp.nama

class Petugas (models.Model):
    HAK_AKSES_CHOICES = (
        ('admin', 'Admin'),
        ('petugas', 'Petugas'),
    )

    nama = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=10, choices=HAK_AKSES_CHOICES)
    foto = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT,"upload"), blank=True)

    def __str__(self):
        return self.nama

class Akun (models.Model):
    JENIS_AKUN_CHOICES = (
        ('petugas', 'Petugas'),
        ('admin', 'Admin'),
    )

    akun = models.ForeignKey(User)
    petugas = models.ForeignKey(Petugas)
    jenis_akun = models.CharField(max_length=9, choices=JENIS_AKUN_CHOICES)

    def __str__(self):
        return self.petugas.nama



