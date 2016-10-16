from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import os.path

# Create your models here.
class Anggota (models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('laki-laki', 'Laki-laki'),
        ('perempuan', 'Perempuan'),
    )

    nrp = models.CharField(max_length=9)
    nama = models.CharField(max_length=45)
    alamat = models.TextField(blank=True)
    no_telp = models.CharField(max_length=12)
    foto = models.FileField(null=True, blank=True)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES, null=True)
    # foto = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT,"upload"), blank=True)

    def __str__(self):
        return self.nrp