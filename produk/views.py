from django.shortcuts import render, get_object_or_404, redirect
from .models import Produk, Kategori, Status
from .serializers import ProdukSerializer
from django.http import JsonResponse
from django import forms
from django.db.models import Max  
from django.shortcuts import render, redirect

# Form Validasi Produk
class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']

    def clean_nama_produk(self):
        nama = self.cleaned_data.get('nama_produk')
        if not nama:
            raise forms.ValidationError("Nama produk harus diisi!")
        return nama

    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        if not isinstance(harga, int):
            raise forms.ValidationError("Harga harus berupa angka!")
        return harga

# List Semua Produk

# 1. Halaman Utama (Bisa Dijual)
def produk_list(request):
    produk = Produk.objects.filter(status__nama_status='bisa dijual').select_related('kategori', 'status')
    context = {
        'produk': produk,
        'judul': 'Daftar Produk (Bisa Dijual)',
        'halaman': 'utama' 
    }
    return render(request, 'produk_list.html', context)

# 2. Halaman Kedua (Tidak Bisa Dijual)
def produk_tidak_jual(request):
    produk = Produk.objects.filter(status__nama_status='tidak bisa dijual').select_related('kategori', 'status')
    context = {
        'produk': produk,
        'judul': 'Arsip Produk (Tidak Bisa Dijual)',
        'halaman': 'arsip' 
    }
    return render(request, 'produk_list.html', context)

# Tambah Produk
def produk_tambah(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            # Jangan langsung simpan ke database 
            produk = form.save(commit=False)
            
            # AMBIL ID API TERBESAR (Agar ID baru tidak bentrok/null)
            max_id = Produk.objects.aggregate(Max('id_produk_api'))['id_produk_api__max']
            
            # Jika tabel kosong, mulai dari 1. Jika ada, tambah 1 dari yang terbesar.
            produk.id_produk_api = (max_id or 0) + 1
            
            produk.save()
            return redirect('produk_list')
    else:
        form = ProdukForm()
        
    return render(request, 'produk_form.html', {'form': form})

# Edit Produk
def produk_edit(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk_form.html', {'form': form})

# Hapus Produk
def produk_hapus(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    produk.delete()
    return redirect('produk_list')
