from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from peminjaman.models import Akun, Petugas

# Create your views here.
def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = Akun.objects.get(akun=user.id)
                    login(request, user)

                    request.session['petugas_id'] = akun.petugas.id
                    request.session['jenis_akun'] = akun.jenis_akun
                    request.session['username'] = request.POST['username']
                except:
                    messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administrator')
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
    petugas = Petugas.objects.get(id=request.session['petugas_id'])
    # select * from petugas where id = '1'
    # return render(request,'profil.html', {"petugas":petugas})

    return render(request,'profil.html', {"petugas":petugas})



def hello(request):
    return render(request, "hello.html")

def hasil(request):
    if request.method=="POST":
        context = {
            "user":request.POST['username'],
            "pass":request.POST['pass']
        }
    return render(request, "hasil.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def result(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)