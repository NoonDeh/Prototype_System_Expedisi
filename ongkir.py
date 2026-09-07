print("================================")
print("        ONGKIR EXPEDISI         ") 
print("================================")
print(f"Ketentuan: ")
print(f"- Reguler Ongkir = Rp10.000 + Rp5.000/5kg + Rp5.000/5km ")
print(f"- Express Ongkir = Rp10.000 + Rp7.000/5kg + Rp7.000/5km ")
print()



berat = float(input("Masukkan berat paket (kg): "))
jarak = float(input("Jarak (km): "))
pengiriman = str(input("jenis pengiriman \n1.reguler \n2.express \nPilih: "))
pengiriman = pengiriman.lower()

if pengiriman == "1":
    pengiriman = "reguler"
elif pengiriman == "2":
    pengiriman = "express"

if pengiriman == "reguler" or pengiriman == "express":
    if berat <= 0:
        print("Masukkan berat paket yang benar")
    else:
        if pengiriman == "reguler" or pengiriman == "1" :
            if berat % 5 == 0:
                if jarak % 5 == 0:
                    ongkir = (berat / 5) + (jarak / 5)
                else:
                    jarak_hitung = jarak + 5
                    ongkir = (berat / 5) + (round(jarak_hitung / 5))
                        
            else:
                berat_hitung = berat + 5
                ongkir = round(berat_hitung / 5) * 5              
                if jarak % 5 == 0:
                    ongkir = (round(berat_hitung / 5)) + (jarak / 5)
                else:
                    jarak_hitung = jarak + 5
                    ongkir = (round(berat_hitung / 5)) + (round(jarak_hitung / 5))

            hitung_ongkir = 10000 + (ongkir * 5000)

        elif pengiriman == "express" or pengiriman == "2":
            if berat % 5 == 0:
                if jarak % 5 == 0:
                    ongkir = (berat / 5) + (jarak / 5)
                else:
                    jarak_hitung = jarak + 5
                    ongkir = (berat / 5) + (round(jarak_hitung / 5))
                        
            else:
                berat_hitung = berat + 5
                ongkir = round(berat_hitung / 5) * 5              
                if jarak % 5 == 0:
                    ongkir = (round(berat_hitung / 5)) + (jarak / 5)
                else:
                    jarak += 5
                    ongkir = (round(berat_hitung / 5)) + (round(jarak / 5))

            hitung_ongkir = 10000 + (ongkir * 7000)

            print("================================")
            print("       HASIL TRANSAKSI          ") 
            print("================================")
            print(f"Berat Paket: {berat}kg")
            print(f"Lokasi Pengiriman: {jarak}km")
            print(f"Tipe Pengiriman: {pengiriman}")
            print(f"Harga Ongkir: Rp{hitung_ongkir}")
            print("================================")
            print()
        else:
            print("Masukkan zona dengan benar")
