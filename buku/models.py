from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Buku (models.Model):
    JENIS_BUKU_CHOICES = (
        ('kp', 'Kerja Praktek'),
        ('ta', 'Tugas Akhir'),
        ('bi', 'Buku Ilmiah'),
    )

    no_buku = models.CharField(max_length=10)
    judul_buku = models.CharField(max_length=100)
    pengarang = models.CharField(max_length=100)
    jenis_buku = models.CharField(max_length=5, choices=JENIS_BUKU_CHOICES)

    def __str__(self):
        return self.no_buku
