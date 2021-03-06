"""perpustakaanta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from anggota import views as a_views
from buku import views as b_views
from peminjaman import views as peminjaman_views
from home import views as home_views
from buku.views import (
    index,
    create,
    hitungDenda,
    hD
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.profil),
    url(r'^login/', home_views.login_view),
    url(r'^logout/', home_views.logout_view),
    url(r'^daftar_peminjaman/', peminjaman_views.daftar_peminjaman, name='daftar_peminjaman'),
    url(r'^tambah_peminjaman/', peminjaman_views.tambah_peminjaman1, name='tambah_peminjaman'),
    url(r'^tambah_anggota/', a_views.tambah_anggota, name='tambah_anggota'),
    url(r'^daftar_anggota/', a_views.daftar_anggota, name='daftar_anggota'),
    url(r'^tambah_buku/', b_views.tambah_buku, name='tambah_buku'),
    url(r'^daftar_buku/', b_views.daftar_buku, name='daftar_buku'),
    url(r'^a_detail/(?P<nrp>\d+)/$', a_views.detail, name='detail'),
    url(r'^anggota/(?P<nrp>\d+)/edit/$', a_views.update, name='updateA'),
    url(r'^buku/', index, name='buku'),
    url(r'^result/', create, name='hasil'),
    # url(r'^tambah_coba/', peminjaman_views.tambah_coba),
    url(r'^denda/', hitungDenda, name='hitungdenda'),
    url(r'^hd/', hD, name='hD'),

    url(r'^post/(?P<nrp>\d+)/edit/$', a_views.post_edit, name='post_edit'),

    #url coba
    url(r'^daftar_coba/', peminjaman_views.daftar_coba, name='daftar_coba'),
    url(r'^coba/(?P<nrp>\d+)/edit/$', peminjaman_views.updateCoba, name='updateCoba'),
    url(r'^tambahcoba/', peminjaman_views.tambahCoba, name='tambahCoba'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # url(r'^$', home.buku),
    # url(r'^(?P<question_id>[0-9]+)/$', home.detail),
    # url(r'^(?P<question_id>[0-9]+)/results/$', home.result),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', home.vote),
# ]
