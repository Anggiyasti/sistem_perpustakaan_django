from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from buku.models import Buku
from buku.forms import BukuForm

# Create your views here.
def daftar_buku(request):
    d_buku = Buku.objects.all()

    return render(request, "daftar_buku.html", {'daftar_buku' : d_buku})

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.method == 'POST':
        fom_data = request.POST
        form = BukuForm(fom_data)
        if form.is_valid():
            buku = Buku(
                no_buku = request.POST['no_buku'],
                judul_buku = request.POST['judul_buku'],
                pengarang = request.POST['pengarang'],
                jenis_buku = request.POST['jenis_buku'],
            )
        buku.save()
        return redirect('/daftar_buku/')
    else:
        form = BukuForm()

    return render(request, 'tambah_buku.html', {'form':form})

