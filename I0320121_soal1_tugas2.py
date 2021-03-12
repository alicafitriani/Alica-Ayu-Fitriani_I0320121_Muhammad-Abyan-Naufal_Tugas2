import math

#menampilkan informasi program
print("\nMenghitung Luas Persegi Panjang\n")

#input nilai panjang dan lebar
p = float(input("Masukkan Panjangnya ="))
l = float(input("Masukkan Lebarnya ="))

#menghitung luas persegi panjang
luas_persegipanjang = p * l

#menampilkan hasil perhitungan luas persegi panjang ke layar
print("Luas persegi panjang = ",luas_persegipanjang)


#menampilkan informasi program
print("\nMenghitung Luas Lingkaran\n")

#input nilai jari-jari
r = float(input("Masukkan nilai jari-jari ="))

#menghitung luas lingkaran
luas_lingkaran = 3.14 * (r ** 2)

#menampilkan hasil perhitungan luas lingkaran ke layar
print("Luas lingkaran = ",luas_lingkaran)


#menampilkan informasi program
print("\nMenghitung Luas Kubus\n")

#input nilai rusuk
s = float(input("Masukkan panjang rusuknya ="))

#menghitung luas kubus
luas_kubus = 6*s*s

#menampilkan hasil perhitungan luas kubus ke layar
print("Luas kubus = ",luas_kubus)


#menampilkan informasi program
print("\nMenghitung Konversi Suhu Celcius ke Fahrenheit\n")

#input nilai suhu dalam celcius
C = float(input("Masukkan nilai suhu celcius ="))

#menghitung konversi suhu celcius ke fahrenheit
F = (9/5) * C + 32

#menampilkan hasil konversi suhu celcius ke fahrenheit ke layar
print("Suhu Celcius = ", C)
print("Suhu Fahrenheit = ", F)


#menampilkan informasi program
print("\nMenghitung Konversi Suhu Reamur ke Kelvin\n")

#input nilai suhu dalam reamur
R = float(input("Masukkan nilai suhu reamur ="))

#menghitung konversi suhu reamur ke kelvin
K = (5/4) * R + 273

#menampilkan hasil konversi suhu reamur ke kelvin ke layar
print("Suhu Reamur = ", R)
print("Suhu Kelvin = ", K)

