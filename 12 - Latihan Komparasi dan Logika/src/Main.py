# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3-------10++++++

inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n-> "))

# ++++++3--------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# ---------------10++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# ++++++3-------10++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ", isCorrect)

print("\n",10*"=","\n")

# ------3+++++++10-------
# Kasus irisan
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3\ndan\nlebih kurang dari 10\n-> "))

# ------3+++++++++++++++
# Lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 =", isLebihDari)

# ++++++++++++++10--------
# Kurang dari 10
isKurangDari = (inputUser < 10)
print("Kurang dari 10 =", isKurangDari)

# ------3+++++++10-------
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan: ", isCorrect)

# PR Nihhh

print("\n",10*"=PR","\n")

# --------0+++++++++5-------8+++++++11-------
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 0 dan kurang dari 5\natau\nlebih dari 8 dan kurang dari 11-> "))

# Memeriksa angka lebih dari 0 dan kurang dari 5
# --------0+++++++5------
isNilai1 = (inputUser > 0 and inputUser < 5)
print("Lebih dari 0 dan kurang dari 5 =", isNilai1)

# Memeriksa angka lebih dari 8 dan kurang dari 11
# -------8+++++++++11----------
isNilai2 = (inputUser > 8 and inputUser < 11)
print("Lebih dari 8 dan kurang dari 11 =", isNilai2)

isCorrect = isNilai1 or isNilai2
print("Angka yang anda masukkan: ", isCorrect)

# ++++++++0---------5+++++++8-------11+++++++
inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 0 dan lebih dari 5\natau\nkurang dari 8 dan lebih dari 11-> "))

# Memeriksa angka kurang dari 0 dan lebih dari 5
# ++++++0---------5++++++
isNilai1 = (inputUser < 0 or inputUser > 5)
print("Kurang dari 0 dan lebih dari 5 =", isNilai1)

# Memeriksa angka kurang dari 8 dan lebih dari 11
# ++++++++8---------11+++++++++
isNilai2 = (inputUser < 8 or inputUser > 11)
print("Kurang dari 8 dan lebih dari 11 =", isNilai2)

isCorrect = isNilai1 and isNilai2
print("Angka yang anda masukkan: ", isCorrect)