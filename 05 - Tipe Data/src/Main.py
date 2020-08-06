# a = 10, a adalah variabel dengan nilai 10

#Tipe data: Angka satuan/Bilangan bulat (Integer)
dataInteger = 11
print("data: ",dataInteger, ", bertipe: ",type(dataInteger))

#Tipe data: Angka dengan koma/Bilangan pecahan (float)
dataFloat = 1.5
print("data: ",dataFloat, ", bertipe: ",type(dataFloat))

#Tipe data: Kumpulan karakter (string)
dataString = "ucup 10" # angka 10 akan dianggap string
print("data: ",dataString, ", bertipe: ",type(dataString))

#Tipe data: Bilangan biner, True/False (bool)
dataBool = True
print("data: ",dataBool, ", bertipe: ",type(dataBool))

## Tipe data khusus

# Bilangan Kompleks, Buat anak matematika
dataComplex = complex(5,6)
print("data: ",dataComplex, ", bertipe: ",type(dataComplex))

# Tipe data dari bahasa C
from ctypes import c_double

dataC_Double = c_double(10.5)
print("data: ",dataC_Double, ", bertipe: ",type(dataC_Double))