# Latihan konversi satuan temperatur
# Program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius: '))
print("Suhu adalah",celcius,"Celcius")

# Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah",reamur,"Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah",kelvin,"Kelvin")

# PR Nihh

print("\nPEKERJAAN RUMAH\n")
fahrenheitPr = float(input('Masukkan suhu dalam fahrenheit: '))
print("Suhu adalah",fahrenheitPr,"Fahrenheit")

# Kelvin
kelvinPr = (5/9 * (fahrenheitPr - 32)) + 273
print("Suhu adalah",kelvinPr,"Kelvin")

# Kelvin to Fahrenheit
kelvinPr1 = float(input('Masukkan suhu dalam kelvin: '))
print("Suhu dalam kelvin adalah",kelvinPr1,"Kelvin")

# Fahrenheit
fahrenheitPr1 = (9/5 * (kelvinPr1 - 273)) + 32
print("Suhu dalam fahrenheit adalah",fahrenheitPr1,"Fahrenheit")