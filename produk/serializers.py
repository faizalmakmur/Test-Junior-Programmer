from rest_framework import serializers
from .models import Produk

class ProdukSerializer(serializers.ModelSerializer):
    kategori = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    
    class Meta:
        model = Produk
        fields = ['id', 'nama_produk', 'harga', 'kategori', 'status']
