import os
import django
import requests
import hashlib
from datetime import datetime

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from produk.models import Produk, Kategori, Status

# Login API
username = input("Masukkan username terbaru: ")
today = datetime.today()
password_plain = f"bisacoding-{today.day:02d}-{today.month:02d}-{str(today.year)[-2:]}"
password_md5 = hashlib.md5(password_plain.encode()).hexdigest()

url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
data = {"username": username, "password": password_md5}

response = requests.post(url, data=data)
if response.status_code != 200:
    print("Gagal ambil data API:", response.text)
    exit()

api_data = response.json()['data']

# Simpan ke database
for item in api_data:
    # Ambil atau buat kategori
    kategori_obj, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
    # Ambil atau buat status
    status_obj, _ = Status.objects.get_or_create(nama_status=item['status'])
    # Buat produk
    Produk.objects.update_or_create(
        nama_produk=item['nama_produk'],
        defaults={
            'harga': int(item['harga']),
            'kategori': kategori_obj,
            'status': status_obj
        }
    )

print("Data API berhasil disimpan ke database!")
