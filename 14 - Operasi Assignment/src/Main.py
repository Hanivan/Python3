# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5
print("Nilai a = ",a)

a += 1 # artinya adalah a = a + 1
print("Nilai a += 1, nilai a: ",a)

a -= 2 # artinya adalah a = a - 2
print("Nilai a -= 2, nilai a: ",a)

a *= 5 # artinya adalah a = a * 5
print("Nilai a *= 5, nilai a: ",a)

a /= 2 # artinya adalah a = a / 2
print("Nilai a /= 2, nilai a: ",a)

b = 10
print("Nilai b = ",b)

# Modulus dan floor division
b %= 3
print("Nilai a %= 3, nilai b: ",b)

b = 10
print("Nilai b = ",b)

b //= 3
print("Nilai a //= 3, nilai b: ",b)

# Pangkat / Eksponen
a = 5
print("Nilai a = ",a)

a **= 3
print("Nilai a **= 3, nilai a: ",a)

# Operasi bitwise
 # OR
c = True
print("\nNilai c = ",c)

c |= False
print("Nilai c |= False, nilai c: ",c)

c = False
c |= False
print("Nilai c |= False, nilai c: ",c)

c = False
c |= False
print("Nilai c |= False, nilai c: ",c)

 # AND
c = True
print("\nNilai c = ",c)

c &= False
print("Nilai c &= False, nilai c: ",c)

c = True
print("Nilai c: ",c)

c &= True
print("Nilai c &= True, nilai c: ",c)

 # XOR
c = True
print("\nNilai c = ",c)

c ^= False
print("Nilai c ^= False, nilai c: ",c)

c = True
print("Nilai c: ",c)

c ^= True
print("Nilai c ^= True, nilai c: ",c)

# Geser geser
d = 0b0100
print("\nNilai d = ",format(d,'04b'))
d >>= 2
print("Nilai d >>= 2, nilai d: ",d)
d <<= 1
print("Nilai d <<= 1, nilai d: ",d)