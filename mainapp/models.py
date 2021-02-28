from django.db import models
from django.urls import reverse

# Create your models here.

JENIS_KELAMIN = (
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan'),
)

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=5)
    npm = models.CharField(max_length=8)
    umur = models.IntegerField()
    cita_cita = models.TextField()
    jenis_kelamin = models.CharField(max_length=50, choices=JENIS_KELAMIN)

    def get_absolute_url(self):
        return reverse("home")
