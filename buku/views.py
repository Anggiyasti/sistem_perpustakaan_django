from django.shortcuts import render, redirect, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import BukuForm
from .models import Buku


# Create your views here.
def index(request):
    return render(request, "post.html")

def create(request):
    if request.method=="POST":
        context = {
            "nama":request.POST["nama"],
            "pass":request.POST["pass"]
        }
    return render(request, "post.html", context)

def hD(request):
    return render(request, "denda.html")
def hitungDenda(request):
    if request.method == "POST":
        date_format = "%d/%m/%Y"
        a = datetime.strptime(request.POST["tgl_pinjam"], date_format)
        b = datetime.strptime(request.POST["tgl_kembali"], date_format)
        hitung = b-a
        denda = hitung.days * 200
        context = {
            "pinjam":request.POST["tgl_pinjam"],
            "kembali":request.POST["tgl_kembali"],
            "denda":denda
        }
    return render(request, "denda.html", context)

@login_required(login_url=settings.LOGIN_URL)
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
