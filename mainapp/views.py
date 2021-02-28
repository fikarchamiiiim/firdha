from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from rest_framework.views import APIView
from .serializers import MahasiswaSerializers

from rest_framework.response import Response

from .models import Mahasiswa

# Create your views here.
class BiodataMahasiswa(TemplateView):
    template_name = "biodata_mahasiswa.html"

    def get(self, request, *args, **kwargs):
        list_mahasiswa = Mahasiswa.objects.all()

        context = {
            'list_mahasiswa' : list_mahasiswa,
        }

        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     nama = request.POST.get("nama")
    #     kelas = request.POST.get("kelas")
    #     npm = request.POST.get("npm")
    #     umur = request.POST.get("umur")
    #     cita_cita = request.POST.get("cita")
    #     jenis_kelamin = request.POST.get("jeniskelamin")

    #     data = Mahasiswa(nama=nama, kelas=kelas, npm=npm, umur=umur, cita_cita=cita_cita, jenis_kelamin=jenis_kelamin)
    #     data.save()

    #     return HttpResponseRedirect(reverse('home'))

class MahasiswaCreate(CreateView):
    model = Mahasiswa
    fields = ["nama", "kelas", "npm", "umur","cita_cita", "jenis_kelamin"]

class MahasiswaUpdate(UpdateView):
    model = Mahasiswa
    fields = ["nama", "kelas", "npm", "umur","cita_cita", "jenis_kelamin"]

class MahasiswaDelete(DeleteView):
    model = Mahasiswa

    success_url = "/"

class BiodataMahasiswaAPI(APIView):
    def get(self, *args, **kwargs):
        list_mahasiswa_api = Mahasiswa.objects.all()
        serializer = MahasiswaSerializers(list_mahasiswa_api, many=True)
        return Response(serializer.data)