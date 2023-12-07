def sewaKamera():
    global total_harga
    global lama_sewa
    global barang
    print("""
            Sewa Kamera : 

            1. DSLR : 200.000 /hari
            2. Mirrorless : 300.000 / hari
            3. Action Cam : 350.000 / hari
            4. Analogo : 400.000 / hari
            5. 360 : 120.000 / hari
            6. Kamera Underwater : 231.000 / hari

            Note : 
            - Diskon 17% apabila menyewa kamera mirrorless 3 hari atau lebih.
            - Diskon 12% apabila menyewa kamera 360 selama 2 hari atau lebih.
            - Diskon 64% apabila menyewa kamera underwater selama 5 hari atau lebih.
        """)
    
    pilihan = int(input("Pilih Kamera : "))
    lama_sewa = int(input("Lama Sewa : ")) 


    if pilihan == 1:    
        total_harga = lama_sewa * 200000
        barang = "DSLR"
    elif pilihan == 2:
        total_harga = lama_sewa   * 300000
        if lama_sewa > 3:
            diskon = total_harga * 0.17
            total_harga = total_harga - diskon
        barang = "Mirrorless"
    elif pilihan == 3:
        total_harga = lama_sewa * 350000
        barang = "Action Cam"
    elif pilihan == 4:
        total_harga = lama_sewa * 400000
        barang = "Analogo"
    elif pilihan == 5:
        total_harga = lama_sewa * 120000
        if lama_sewa > 2:
            diskon = total_harga * 0.12
            total_harga = total_harga - diskon
        barang = "360"
    elif pilihan == 6:
        total_harga = lama_sewa * 231000
        if lama_sewa > 5:
            diskon = total_harga * 0.12
            total_harga = total_harga - diskon
        barang = "Kamera Underwater"
    else:
        print("Pilihan Anda Tidak Ada")
        sewaKamera()

sewaKamera()
total_keseluruhan = total_harga

print("Total yang harus diabayar: Rp", total_keseluruhan)
print("========== NOTA SEWA =========")
print ("Kamera\t\t:",barang)
print ("Lama Sewa\t:",lama_sewa, "Hari")
print ("Tagihan\t\t: Rp",total_keseluruhan)
print("==================================")