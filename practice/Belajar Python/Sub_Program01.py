# conversi celcius ke fahrenheit/fahrenheit ke celcius

print("ketik 1 untuk konversi celcius ke fahrenheit")
print("ketik 2 untuk konversi fahrenheit ke celcius")
nilai = float(input("Pilih Menu : "))
if nilai == 1:

    print ("=====Konversi Celcius=====")
    celcius = float(input("Masukkan Temperature Dalam Bentuk Fahrenheit :"))
    fahrenheit = (1.8) * (celcius + 32)
    print("Temperature Dalam Bentuk Fahrenheit :", fahrenheit)

elif nilai == 2:
    print ("=====Konversi Fahrenheit=====")
    fahrenheit = float(input("Masukkan Temperature Dalam Bentuk Celcius :"))
    celcius = (5/9) * (fahrenheit - 32)
    print("Temperature Dalam Bentuk Celcius :", celcius)

else:
    print("Menu Tidak Ditemukan")