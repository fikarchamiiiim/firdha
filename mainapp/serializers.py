from rest_framework import serializers
from .models import Mahasiswa

class MahasiswaSerializers(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(MahasiswaSerializers, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Mahasiswa
        fields = '__all__'