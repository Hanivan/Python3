# Kita belajar Casting Tipe Data
# Merubah dari satu tipe ke tipe lain\
# Tipe data = int, float, str, bool

# INTEGER
print("============INTEGER================")
dataInt = 9
print("Data =",dataInt,", type =",type(dataInt))

dataFloat = float(dataInt)
print("Data =",dataFloat,", type =",type(dataFloat))

dataStr = str(dataInt)
print("Data =",dataStr,", type =",type(dataStr))

dataBool = bool(dataInt) # Jika nilai int lebih dari 0, maka true, Jika sama dengan 0, maka false
print("Data =",dataBool,", type =",type(dataBool))


# FLOAT
print("===============FLOAT================")
dataFloat = 9.5
print("Data =",dataFloat,", type =",type(dataFloat))

dataInt = int(dataFloat) # akan dibulatkan ke bawah
print("Data =",dataInt,", type =",type(dataInt))

dataStr = str(dataFloat)
print("Data =",dataStr,", type =",type(dataStr))

dataBool = bool(dataFloat) # Jika nilai int lebih dari 0, maka true, Jika sama dengan 0, maka false
print("Data =",dataBool,", type =",type(dataBool))


# BOOLEAN
print("===============BOOLEAN==============")
dataBool = True
print("Data =",dataBool,", type =",type(dataBool))

dataInt = int(dataBool) # akan dibulatkan ke bawah
print("Data =",dataInt,", type =",type(dataInt))

dataStr = str(dataBool)
print("Data =",dataStr,", type =",type(dataStr))

dataFloat = float(dataBool) # Jika nilai int lebih dari 0, maka true, Jika sama dengan 0, maka false
print("Data =",dataFloat,", type =",type(dataFloat))

# STRING
print("===============STRING==============")
dataStr = "10"
print("Data =",dataStr,", type =",type(dataStr))

dataInt = int(dataStr) # string harus angka
print("Data =",dataInt,", type =",type(dataInt))

dataFloat = float(dataStr) # string harus angka
print("Data =",dataFloat,", type =",type(dataFloat))

dataBool = bool(dataStr) # False jika string kosong
print("Data =",dataBool,", type =",type(dataBool))