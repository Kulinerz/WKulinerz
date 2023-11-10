# SISTEM KREDIT RUMAH

def cicilan():

    # MEMINTA INPUT DARI PENGGUNA
    harga_rumah = float(input("Masukan Harga Rumah :"))
    jangka_waktu = int(input("Masukan Periode Cicilan Berapa Tahun: "))

    # BUNGA TETAP 10%
    bunga = 0.1

    # MENGHITUNG BERAPA YANG HARUS DIBAYARKAN PADA TIAP TAHUN 
    cicilan = harga_rumah / jangka_waktu

    # MENGHITUNG BIAYA CICILAN YANNG HARUS DIBAYARKAN PERTAHUN BESERTA DENGAN BUNGA NYA
    cicilan_tahunan = cicilan + (cicilan * bunga)

    # TOTAL HARGA RUMAH YANG HARUS DIBAYARKAN UNTUK MELUNASI RUMAH
    total_hargaRumah = harga_rumah + (harga_rumah * bunga)   

    # MENAMPILKAN HASIL CICILAN YANG HARUS DIBAYARKAN TIAP TAHUN
    print(f"Cicilan tiap tahun {cicilan_tahunan}")

    # MENAMPILKAN PERIODE CICILAN DAN TOTAL CICILAN YANG HARUS DILUNASI
    print(f"Total cicilan selama {jangka_waktu} tahun : {total_hargaRumah}")

    # OUTPUT PROGRAM
    i = 1
    while i <= jangka_waktu:
        total_cicilan = i * cicilan_tahunan
        print(f' cicilan ke-{i} {total_cicilan}' )
        i+= 1


        if(total_hargaRumah == total_cicilan):
            # MENAMPILKAN HASIL JIKA TOTAL CICILAN SUDAH SAMA DENGAN TOTAL HARGA RUMAH
            print("Rumah Anda Telah Lunas")
        else:
            # MENAMPILKAN HASIL JIKA TOTAL CICILAN TIDAK SAMA DENGAN TOTAL HARGA RUMAH
            print("Rumah Anda Belum Lunas")

    return cicilan_tahunan

cicilan()

        



# hasil_seleksi = seleksi_nilai(nilai_mahasiswa)
# print(f"Mahasiswa dengan nilai {nilai_mahasiswa} dinyatakan {hasil_seleksi}")