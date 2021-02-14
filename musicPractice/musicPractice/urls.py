"""musicPractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newapp import views

app_name = "newapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = "homepage"),
    path('band/', views.band_page, name = "band_page"),
    path('create-band/', views.create_band, name = "create_band"),
    path('create-album/', views.create_album, name ="create_album"),
    path('album/', views.album_page, name = "album_page"),
]
