# Epsode input user

# Data yang masukkan pasti string
data = input("Masukkan data: ")
print("Data =",data,", type =",type(data))

# Jika kita ingin mengambil int, maka
angka = float(input("Masukkan angka: "))
angka = int(input("Masukkan angka: "))
print("Data =",angka,", type =",type(angka))

# Bagaimana dengan boolean?
biner = bool(int(input("Masukkan nilai boolean: "))) # Harus diubah dulu ke string agar bisa membaca nilai true/false
print("Data =",biner,", type =",type(biner))