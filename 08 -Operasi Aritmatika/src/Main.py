# Operasi Aritmatika

a = 10
b = 3

# Operasi Pertambahan +
hasil = a + b
print(a,"+",b,"=",hasil)

# Operasi Pengurangan -
hasil = a - b
print(a,"-",b,"=",hasil)

# Operasi Perkalian *
hasil = a * b
print(a,"*",b,"=",hasil)

# Operasi Pembagian /
hasil = a / b
print(a,"/",b,"=",hasil)

# Operator Eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=",hasil)

# Operator Modulus (Sisa Pembagian) %
hasil = a % b
print(a,"%",b,"=",hasil)

# Operator Floor Division //
hasil = a // b
print(a,"//",b,"=",hasil)

# Prioritas Operasi, Operasi Precedence
# - ()
# - Exponen **
# - Perkalian dkk * / ** % //
# - Pertambahan/Pengurangan + -

x = 3
y = 2
z = 4
hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=',hasil)