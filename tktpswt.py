import os

loop = True

while loop:
  def menu():
    print("\n-------------------------------")
    print("\n TRAVELIO BOOK FLIGHT TICKET")
    print("\n-------------------------------")
    print("1. Jakarta")
    print("2. Bandung")
    print("3. Yogyakarta")
    print("4. Surabaya")
    print("5. Exit")
    print("\n-------------------------------")

  def pesan():
    jmlh_tiket = int(input("Masukkan Jumlah Tiket: "))
    num_array= list()
    num = input("Jumlah Penumpang: ")
    print("Masukkan Nama Pemesan: ")
    for i in range (int(num)):
      i += 1
      n = input("orang ke {} :".format(i))
      num_array.append(str(n))
    total_tiket = jmlh_tiket*harga
    os.system('cls')
    print("\n---------------------------------------------")
    print("Anda telah berhasil melakukan pembelian tiket")
    print("-----------------------------------------------")
    print(" Nama Pemesan :".format(len(num_array)))
    for a in num_array:
      print(("- {}").format(a))
    print("Total Harga","Rp.",(total_tiket))
  menu()
  tujuan = int(input("Masukkan Pilihan [1-5]: "))

  if ((tujuan) == 1):
    print("\n-----------------------------------------------------")
    print("\nKode Nama\tKota\t\tHarga")
    print("\nPesawat\tTujuan\t\Tiket")
    print("\n--------------------------------------------------------")
    print("n101.  Garuda\tJakarta\tRp.1.500.000")
    print("n102.  Citilink\tJakarta\tRp.975.000")
    print("n103.  Lion Air\tJakarta\tRp.920.000")
    print("n104.  Citilink\tJakarta\tRp.750.000")
    print("\n-------------------------------------------------------")
    no_pesawat = int(input("Masukan kode penerbangan : "))


    if ((no_pesawat) == 101):
      harga = 1500000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()


    elif ((no_pesawat) == 102):
      harga = 975000
      print("")
      print("---------------------------------")
      print("anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()

    elif ((no_pesawat) == 103):
      harga = 920000
      print("")
      print("---------------------------------")
      print("anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()

    elif ((no_pesawat) == 104):
      harga = 750000
      print("")
      print("---------------------------------")
      print("anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()
    else :
      os.system('cls')
      print("Kode penerbangan tidak ada dalam daftar")

  elif ((tujuan) == 2):
    print("\n----------------------------------------------------------")
    print("\nKode  Nama\tKota\t\tHarga")
    print("\n      Pesawat\tTujuan\t\tTiket")
    print("\n----------------------------------------------------------")
    print("\n201. Citilink\tBandung \tRp.2.000.000")
    print("\n202. NAM air\tBandung \tRp.900.000")
    print("\n203. Garuda\tBandung \tRp.1.200.000")
    print("\n----------------------------------------------------------")
    no_pesawat = int(input("Masukan kode penerbangan :"))

    if ((no_pesawat) == 201):
      harga = 2000000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()

    elif ((no_pesawat) == 202):
      harga = 900000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()
      
    elif ((no_pesawat) == 203):
      harga = 1200000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()
      
    else :
      os.system('cls')
      print("Kode penerbangan tidak ada dalam daftar")

  elif ((tujuan) == 3):
    print("\n-------------------------------------------------------")
    print("\nKode  Nama\tKota\t\tHarga")
    print("\n      Pesawat\tTujuan\t\tTiket")
    print("\n-------------------------------------------------------")
    print("\n301. Citilink\tYogyakarta \tRp.1.000.000")
    print("\n302. Lion Air\tYogyakarta \tRp.800.000")
    print("\n303. Garuda\tYogyakarta \tRp.1.600.000")
    print("\n-------------------------------------------------------")
    no_pesawat = int(input("Masukan kode penerbangan :"))

    if ((no_pesawat) == 301):
      harga = 1000000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()

    elif ((no_pesawat) == 302):
      harga = 800000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()

    elif ((no_pesawat) == 303):
      harga = 1600000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()

    else :
      os.system('cls')
      print("Kode penerbangan tidak ada dalam daftar")



  elif ((tujuan) == 4):
    print("\n-------------------------------------------------------")
    print("\nKode  Nama\tKota\t\tHarga")
    print("\n      Pesawat\tTujuan\t\tTiket")
    print("\n-------------------------------------------------------")
    print("\n401. Garuda\tSurabaya \tRp.1.200.000")
    print("\n402. Lion Air\tSurabaya \tRp.1.000.000")
    print("\n403. Merpati\tSurabaya \tRp.1.800.000")
    print("\n-------------------------------------------------------")
    no_pesawat = int(input("Masukan kode penerbangan :"))



    if ((no_pesawat) == 401):
      harga = 1000000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()

    elif ((no_pesawat) == 402):
      harga = 800000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()

    elif ((no_pesawat) == 403):
      harga = 800000
      print("")
      print("---------------------------------")
      print("Anda memilih kode penerbangan",+int(no_pesawat))
      print("---------------------------------")
      pesan()

    else :
      os.system('cls')
      print("Kode penerbangan tidak ada dalam daftar")


  elif ((tujuan) == 5):
    os.system('cls')
    print("Terima kasih telah menggunakan Travelio!")
    loop = False

  else  :
    os.system('cls')
    print("*** Pilihan tidak ada dalam daftar ***")

# Run the application
root.mainloop()


  