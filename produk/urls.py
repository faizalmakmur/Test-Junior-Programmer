from django.urls import path
from . import views

urlpatterns = [
    # Halaman 1: Utama
    path('', views.produk_list, name='produk_list'),
    
    # Halaman 2: Tidak Bisa Dijual 
    path('arsip/', views.produk_tidak_jual, name='produk_tidak_jual'),

    # (Tambah, Edit, Hapus)
    path('tambah/', views.produk_tambah, name='produk_tambah'),
    path('edit/<int:pk>/', views.produk_edit, name='produk_edit'),
    path('hapus/<int:pk>/', views.produk_hapus, name='produk_hapus'),
]