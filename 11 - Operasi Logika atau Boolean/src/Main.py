# Operasi logika atau boolean

# not, or, and, xor

# NOT
print('=====NOT=====') # NOT = Kebalikan dari nilai sebenarnya
a = True
c = not a
print('data a =',a)
print('--------------NOT')
print('data c =',c)

# OR
print('=====OR=====') # OR = Jika salah satu nilai benar, maka true
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or b
print(a,' OR',b,' =',c)

# AND
print('=====AND=====') # AND = Kedua nilai harus bernilai benar/true
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)

# XOR
print('=====XOR=====') # XOR = Jika salah satu yang bernilai true, maka true. Sisanya False
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)