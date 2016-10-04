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
from hello.views import (
    index,
    create,
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.profil),
    url(r'^login/', home_views.login_view),
    url(r'^logout/', home_views.logout_view),
    url(r'^daftar_peminjaman/', peminjaman_views.daftar_peminjaman, name='daftar_peminjaman'),
    url(r'^tambah_peminjaman/', peminjaman_views.tambah_peminjaman, name='tambah_peminjaman'),
    url(r'^tambah_anggota/', a_views.tambah_anggota, name='tambah_anggota'),
    url(r'^daftar_anggota/', a_views.daftar_anggota, name='daftar_anggota'),
    url(r'^tambah_buku/', b_views.tambah_buku, name='tambah_buku'),
    url(r'^daftar_buku/', b_views.daftar_buku, name='daftar_buku'),
    url(r'^(?P<nrp>\d+)/$', a_views.detail, name='detail'),
    url(r'^(?P<nrp>\d+)/edit/$', a_views.update, name='update'),
    url(r'^hello/', index, name='hello'),
    url(r'^result/', create, name='hasil'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # url(r'^$', home.hello),
    # url(r'^(?P<question_id>[0-9]+)/$', home.detail),
    # url(r'^(?P<question_id>[0-9]+)/results/$', home.result),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', home.vote),
# ]
