#CONDITION
nilai = int(input("Masukkan nilai : "))
if nilai > 80:
    nilaiAkhir = "A"
elif nilai > 60 and nilai <=80:
    nilaiAkhir = "B"
elif nilai < 60 and nilai >40:
    nilaiAkhir = "C"
elif nilai <= 40 and nilai >20:
    nilaiAkhir = "D"
else:
    nilaiAkhir = "E" 

print(f'Nilai akhir : {nilaiAkhir}')


