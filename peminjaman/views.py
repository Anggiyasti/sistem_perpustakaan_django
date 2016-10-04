from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from peminjaman.models import Peminjaman
from anggota.models import Anggota
from buku.models import Buku
from peminjaman.forms import PeminjamanForm

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def daftar_peminjaman(request):
    daftar_peminjaman = None

    if request.method == 'POST':
        bulan = request.POST['bulan']
        tahun = request.POST['tahun']
        daftar_peminjaman = Peminjaman.objects.filter(tgl_pinjam__year=tahun, tgl_pinjam__month=bulan)

    return render(request, 'daftar_peminjaman.html', {'daftar_peminjaman':daftar_peminjaman})

@login_required(login_url=settings.LOGIN_URL)
def tambah_peminjaman(request):
    if request.method == 'POST':
        form_data = request.POST
        try:
            anggota = Anggota.objects.get(id=request.POST.get('nrp'))
        except Anggota.DoesNotExist:
            anggota = None
        try:
            buku = Buku.objects.get(id=request.POST.get('no_buku'))
        except Buku.DoesNotExist:
            buku = None

        form = PeminjamanForm(form_data)
        if form.is_valid():
            peminjaman = Peminjaman(
                nrp = anggota,
                no_buku = buku,
                tgl_pinjam = request.POST['tgl_pinjam'],
                tgl_kembali = request.POST['tgl_kembali'],
            )

            peminjaman.save()
            return redirect('daftar_peminjaman')
    else:
        form = PeminjamanForm()

    return render(request, 'tambah_peminjaman.html', {'form':form})