import requests
import hashlib
from datetime import datetime

# Input username 
username = input("Masukkan username terbaru: ")

# Generate password MD5 
today = datetime.today()
password_plain = f"bisacoding-{today.day:02d}-{today.month:02d}-{str(today.year)[-2:]}"
password_md5 = hashlib.md5(password_plain.encode()).hexdigest()

# URL API
url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

# Data login dikirim sebagai value POST
data = {
    "username": username,
    "password": password_md5
}

# Kirim request POST
response = requests.post(url, data=data)

if response.status_code == 200:
    print("Berhasil ambil data:")
    print(response.json())
else:
    print("Gagal ambil data. Status code:", response.status_code)
    print(response.text)
