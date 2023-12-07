    #CONDITION
nilai = int(input("Masukkan nilai : "))

def KonversiNilai(nilai):
    if nilai > 80:
        nilaiAkhir = "A"
    elif nilai > 60 and nilai <=80:
     nilaiAkhir = "B"
    else:
      nilaiAkhir = "E" 
    return nilaiAkhir

print(f'Nilai akhir : {KonversiNilai(nilai)}')


