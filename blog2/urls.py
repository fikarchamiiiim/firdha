"""blog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mainapp.views import BiodataMahasiswa, BiodataMahasiswaAPI, HomeView, MahasiswaCreate, MahasiswaDelete, MahasiswaUpdate, PakaiTemplate, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('mahasiswa/', BiodataMahasiswa.as_view(), name="mahasiswa"),
    path('tambah_mahasiswa/', MahasiswaCreate.as_view(), name="tambah_mahasiswa"),
    path('<pk>/update_mahasiswa/', MahasiswaUpdate.as_view(), name="update_mahasiswa"),
    path('<pk>/delete_mahasiswa/', MahasiswaDelete.as_view(), name="delete_mahasiswa"),
    path('pakaiTemplate/', PakaiTemplate.as_view(), name='pakai_template')

]
