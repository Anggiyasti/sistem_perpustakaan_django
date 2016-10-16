from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q

from anggota.models import Anggota
from anggota.forms import AnggotaForm

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def daftar_anggota(request):
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
    return render(request, 'daftar_anggota.html', context)

@login_required(login_url=settings.LOGIN_URL)
def tambah_anggota(request):
    if request.method == 'POST':
        # form_data = request.POST
        form = AnggotaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            a = Anggota()
            a.nrp = form.cleaned_data['nrp']
            a.nama = form.cleaned_data['nama']
            a.alamat = form.cleaned_data['alamat']
            a.no_telp = form.cleaned_data['no_telp']
            a.jenis_kelamin = form.cleaned_data['jenis_kelamin']
            a.foto = form.cleaned_data['foto']
            a.save()
            # success =True
            # nrp = form.cleaned_data['nrp']
            # nama = form.cleaned_data['nama']
            # alamat = form.cleaned_data['alamat']
            # no_telp = form.cleaned_data['no_telp']
            # jenis_kelamin = form.cleaned_data['jenis_kelamin']
            # foto = form.cleaned_data['foto']
            # # anggota = form.save(commit=False)
            # # anggota.save()
            # anggota = Anggota (
            #     nrp = nrp,
            #     nama = nama,
            #     alamat = alamat,
            #     no_telp = no_telp,
            #     jenis_kelamin = jenis_kelamin,
            #     foto = foto
            # )
            # anggota.save()

            return redirect('/daftar_anggota/')
    else:
        form = AnggotaForm()

    return render(request, 'tambah_anggota.html', {'form':form})

@login_required(login_url=settings.LOGIN_URL)
def detail(request, nrp=None):
    instance = get_object_or_404(Anggota, nrp=nrp)

    context = {
        "instance" :instance
    }

    return render(request,'anggota_detail.html', context)

# def update(request, nrp=None):
#     instance = get_object_or_404(Anggota, nrp=nrp)
#     form = AnggotaForm(request.POST or None, request.FILES or None, instance=instance)
#     if form.is_valid():
#         instance = form.save()
#         instance.save()
#         return HttpResponseRedirect('/daftar_anggota')
#     context = {
#         "instance" :instance,
#         "form":form
#     }
#
#     return render(request,'tambah_anggota.html', context)

@login_required(login_url=settings.LOGIN_URL)
def update(request, nrp=None):
    instance = get_object_or_404(Anggota, nrp=nrp)
    form = AnggotaForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/daftar_anggota')
    context = {
        "instance" :instance,
        "form":form
    }
    return render(request,'tambah_anggota.html', context)

@login_required(login_url=settings.LOGIN_URL)
def post_edit(request, nrp):
    post = get_object_or_404(Anggota, nrp=nrp)
    if request.method == "POST":
        form = AnggotaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.nrp = request.nrp
            post.nama = request.nama
            post.alamat = request.alamat
            post.no_telp = request.no_telp
            post.save()
            return redirect('daftar_anggota', nrp=post.nrp)
    else:
        form = AnggotaForm(instance=post)
    return render(request, 'tambah_anggota.html', {'form': form})