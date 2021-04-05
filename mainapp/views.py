from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from rest_framework.views import APIView
from .serializers import MahasiswaSerializers
from rest_framework.response import Response
from .models import Mahasiswa
from django.db.models import Q

# Create your views here.
class BiodataMahasiswa(TemplateView):
    template_name = "biodata_mahasiswa.html"

    def get(self, request, *args, **kwargs):
        # Get All Objects
        list_mahasiswa = Mahasiswa.objects.all()
        # ===> SELECT * FROM Mahasiswa

        # yang perempuan
        # list_mahasiswa = Mahasiswa.objects.filter(Q(jenis_kelamin = 'Perempuan') & Q(umur__lte = 21))

        # yang kurang dari 22
        # list_mahasiswa_kurang_dari_22 = Mahasiswa.objects.filter(umur__lte = 22)

        # ambil 1 object yang namanya "jihad"
        # list_mahasiswa = Mahasiswa.objects.get(nama = 'jihad') 

        a = 5 + 10

        context = {
            'list_mahasiswa' : list_mahasiswa,
            # 'list_mahasiswa_kurang_dari_22' : list_mahasiswa_kurang_dari_22,
            'nama_gue' : a,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        nama = request.POST.get("nama")
        kelas = request.POST.get("kelas")
        npm = request.POST.get("npm")
        umur = request.POST.get("umur")
        cita_cita = request.POST.get("cita")
        jenis_kelamin = request.POST.get("jeniskelamin")

        data = Mahasiswa(nama=nama, kelas=kelas, npm=npm, umur=umur, cita_cita=cita_cita, jenis_kelamin=jenis_kelamin)
        data.save()

        return HttpResponseRedirect(reverse('home'))

class MahasiswaCreate(CreateView):
    model = Mahasiswa
    fields = ["nama", "kelas", "npm", "umur","cita_cita", "jenis_kelamin"]

# class MahasiswaUpdate(UpdateView):
#     model = Mahasiswa
#     fields = ["nama", "kelas", "npm", "umur","cita_cita", "jenis_kelamin"]

class MahasiswaUpdate(TemplateView):
    template_name = "mahasiswa_update.html"

    def get(self, request, pk, *args, **kwargs):
        data_mahasiswa = Mahasiswa.objects.get(id=pk)

        context = {
            'data_mahasiswa' : data_mahasiswa,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, pk, *args, **kwargs):


        nama = request.POST.get("nama")
        kelas = request.POST.get("kelas")
        npm = request.POST.get("npm")
        umur = request.POST.get("umur")
        cita_cita = request.POST.get("cita")
        jenis_kelamin = request.POST.get("jeniskelamin")

        data_mahasiswa = Mahasiswa.objects.filter(id=pk).update(nama=nama, kelas=kelas, npm=npm, umur=umur, cita_cita=cita_cita, jenis_kelamin=jenis_kelamin)

        return HttpResponseRedirect(reverse('mahasiswa'))

# class MahasiswaDelete(DeleteView):
#     model = Mahasiswa

#     success_url = "/"

class MahasiswaDelete(View):
    def get(self, request, pk, *args, **kwargs):
        data_mahasiswa = Mahasiswa.objects.get(id = pk)
        data_mahasiswa.delete()

        return HttpResponseRedirect(reverse('mahasiswa'))

class BiodataMahasiswaAPI(APIView):
    def get(self, *args, **kwargs):
        list_mahasiswa_api = Mahasiswa.objects.all()
        serializer = MahasiswaSerializers(list_mahasiswa_api, many=True)
        return Response(serializer.data)

class PakaiTemplate(TemplateView):
    template_name = 'index.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'