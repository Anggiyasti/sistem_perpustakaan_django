from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q

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
        # print("Buku : ", daftar_peminjaman)
        # print("Nama", dbuku)
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

@login_required(login_url=settings.LOGIN_URL)
def tambah_peminjaman1(request):
    daftar_peminjaman = Anggota.objects.all()

    query = request.GET.get("q")
    if query:
        daftar_peminjaman = daftar_peminjaman.filter(
            Q(nrp__icontains=query) |
            Q(nama__icontains=query)
            ).distinct()
    context = {
        "d_pinjam":daftar_peminjaman,
    }
    return render(request, 'tambah_peminjaman.html', context)

@login_required(login_url=settings.LOGIN_URL)
def update(request, nrp=None):
    instance = get_object_or_404(Anggota, nrp=nrp)
    form = PeminjamanForm(request.POST or None, request.FILES or None, instance=instance)
    daftar_buku = Buku.objects.all()
    query = request.GET.get("q")
    if query:
        daftar_buku = daftar_buku.filter(
            Q(no_buku__icontains=query) |
            Q(judul_buku__icontains=query)
            ).distinct()
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/daftar_peminjaman')
    context = {
        "instance" :instance,
        "form":form,
        "d_buku":daftar_buku
    }

    return render(request,'tambah_peminjaman.html', context)

@login_required(login_url=settings.LOGIN_URL)
def detail(request, nrp=None):
    instance = get_object_or_404(Anggota, nrp=nrp)
    daftar_buku = Buku.objects.all()
    query = request.GET.get("q")
    if query:
        daftar_buku = daftar_buku.filter(
            Q(no_buku__icontains=query) |
            Q(judul_buku__icontains=query)
            ).distinct()
    context = {
        "instance" :instance,
        "d_buku":daftar_buku
    }

    return render(request,'pinjam_detail.html', context)

# def tambah_coba(request):
#     if request.method == 'POST':
#         # try:
#         #     anggota = Anggota.objects.get(id=request.POST.get('nrp'))
#         # except Anggota.DoesNotExist:
#         #     anggota = None
#         # try:
#         #     buku = Buku.objects.get(id=request.POST.get('no_buku'))
#         # except Buku.DoesNotExist:
#         #     buku = None
#         a = Anggota(nrp=request.POST['nrp'])
#         a.save()
#         b = Buku(no_buku=request.POST['no_buku'])
#         b.save()
#         pinjam = Peminjaman(
#                 nrp = a,
#                 no_buku = b,
#                 tgl_pinjam = request.POST['tgl_pinjam'],
#                 tgl_kembali = request.POST['tgl_kembali'],
#             )
#         print("nrp")
#
#         pinjam.save()
#         return redirect('daftar_peminjaman')
#
#     # return render(request, 'tambah_peminjaman.html', {'form':form})
#     return render(request, 'pinjam_detail.html')


#fungsi coba
@login_required(login_url=settings.LOGIN_URL)
def daftar_coba(request):
    daftar_anggota = Anggota.objects.all()

    query = request.GET.get("q")
    if query:
        daftar_anggota = daftar_anggota.filter(
            Q(nama__icontains=query) |
            Q(nrp__icontains=query)
            ).distinct()
    context = {
        "d_anggota":daftar_anggota,
    }
    return render(request, 'coba/daftar_coba.html', context)

@login_required(login_url=settings.LOGIN_URL)
def getData(request):
    if request.method == "POST":
        context = {
            'nrp': request.POST["nrp"]
        }
    return render(request, 'coba/daftar_coba.html', context)

@login_required(login_url=settings.LOGIN_URL)
def updateCoba(request, nrp=None):
    instance = get_object_or_404(Anggota, nrp=nrp)
    daftar_buku = Buku.objects.all()
    query = request.GET.get("q2")
    if query:
        daftar_buku = daftar_buku.filter(
            Q(no_buku__icontains=query) |
            Q(judul_buku__icontains=query)
            ).distinct()

    context = {
        "instance" :instance,
        "d_buku":daftar_buku
    }

    return render(request,'coba/tambah_pinjam.html', context)

@login_required(login_url=settings.LOGIN_URL)
def tambahCoba(request):
    if request.method == 'POST':
        try:
            anggota = Anggota.objects.get(nrp=request.POST.get('nrp'))
        except Anggota.DoesNotExist:
            anggota = None
        try:
            buku = Buku.objects.get(no_buku=request.POST.get('no_buku'))
        except Buku.DoesNotExist:
            buku = None
        # a = Anggota(nrp=request.POST['nrp'])
        # p = Peminjaman(nrp = a)
        # # p.save()
        # b = Buku(no_buku=request.POST['no_buku'])
        pinjam = Peminjaman(
                nrp = anggota,
                no_buku = buku,
                tgl_pinjam = request.POST['tgl_pinjam'],
                tgl_kembali = request.POST['tgl_kembali'],
            )
        print("nrp")

        pinjam.save()
        return redirect('/')

    return render(request, 'coba/tambah_pinjam.html')
