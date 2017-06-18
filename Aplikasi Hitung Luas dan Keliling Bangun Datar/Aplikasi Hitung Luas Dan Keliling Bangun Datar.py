"""
Aplikasi Hitung Luas dan Keliling Bidang Datar
Dibuat Oleh : Prima Akbar Mashudi,ST

Deskripsi Aplikasi :
Aplikasi ini dibuat untuk menghitung 
properties bidang yaitu :
1. Persegi / Bujur Sangkar (bs)
2. Persegi Panjang (pp)
3. Segitiga (se)
4. Lingkaran (ling)
5. Jajar Genjang (jg)
6. Trapesium (tra)
7. Layang-layang (lay)
8. Belah Ketupat (bk)

"""
import math
import os

#Opsi Pilih Bidang Yang Akan Dihitung
#Propertinya

def hitung_bidang():
#Judul Aplikasi
     while True:
        print ("########################################")
        print ("APLIKASI HITUNG LUAS DAN KELILING BANGUN DATAR")
        print ("Oleh : Prima Akbar Mashudi,ST")
        print ("Bidang 2D (kode) :")
        print ("1. Persegi/Bujur Sangkar (bs)")
        print ("2. Persegi Panjang (pp)")
        print ("3. Segitiga (se)")
        print ("4. Lingkaran (ling)")
        print ("5. Jajar Genjang (jg)")
        print ("6. Trapesium (tra)")
        print ("7. Layang-Layang (lay)")
        print ("8. Belah Ketupat (bk)")
        print (" ")
        print ("[TEKAN CTR+C] Untuk Keluar Aplikasi")
        print ("########################################")
        pilihan=input("Masukan Kode Bidang :")
        if pilihan == "bs":
            print ("/// MENGHITUNG LUAS DAN KELILING BUJUR SANGKAR / PERSEGI /// ")
            print ("Persegi memiliki sisi sama panjang")
            try:
                 sisi_persegi=input("Panjang sisi (m) :")
                 if len(sisi_persegi)>0:
                     sisi_persegi=float(sisi_persegi)
                     luas_persegi=sisi_persegi**2
                     keliling_persegi=4*sisi_persegi
                     print ("Panjang Sisi : ",sisi_persegi," meter")
                     print ("Luas Persegi : ",luas_persegi," meter2")
                     print ("Keliling Persegi : ",keliling_persegi," meter")
                 else:
                     print ("Masukan Angka")
            except ValueError:
                 print ("!!!- Masukan Angka -!!!")
                 os.system('cls')
                 continue
                 
        elif pilihan == "pp":
            print ("/// MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG /// ")
            print ("Persegi Panjang memiliki panjang dan lebar yang berbeda")
            try:
                 panjang_pp=float(input("Panjang Persegi Panjang (m) : "))
                 lebar_pp=float(input("Lebar Persegi Panjang (m) : "))
            except ValueError:
                 print ("!!!- Masukan Angka -!!!")
                 os.system('cls')
                 continue
            luas_pp=panjang_pp*lebar_pp
            keliling_pp=2*(panjang_pp+lebar_pp)
            print("Panjang :",panjang_pp," meter")
            print("Lebar :",lebar_pp," meter")
            print("Luas Persegi Panjang :",luas_pp," m2")
            print("Keliling Persegi Panjang :",keliling_pp," meter")
        elif pilihan == "se":
            print ("/// MENGHITUNG LUAS DAN KELILING SEGITIGA /// ")
            print ("Segitiga memiliki panjang 3 sisi dan juga tinggi")
            print ("Jika sisi a adalah alas, b dan c adalah sisi miringnya, maka :")
            try :
                 alas_segitiga=float(input("Panjang Alas Segitiga/ Sisi a (m) : "))
                 sisi_b=float(input("Panjang Sisi Miring b (m) : "))
                 sisi_c=float(input("Panjang Sisi Miring c (m) : "))
                 tinggi_segitiga=float(input("Tinggi Segitiga (m) : "))
                 luas_segitiga=1/2 * (alas_segitiga * tinggi_segitiga)
                 keliling_segitiga= alas_segitiga + sisi_b + sisi_c
                 print ("Luas Segitinga :", luas_segitiga, " m2")
                 print ("Keliling Segitiga :", keliling_segitiga, "m")
            except ValueError:
                 print ("!!!- Masukan Angka -!!!")
                 os.system('cls')
                 continue
        elif pilihan == "ling":
            print ("/// MENGHITUNG LUAS DAN KELILING LINGKARAN /// ")
            print ("Lingkaran memiliki panjang jari-jari yang sama")
            try:
                 jari_jari=float(input("Jari-Jari Lingkaran (m) : "))
                 luas_lingkaran= 3.14 * jari_jari * jari_jari
                 keliling_lingkaran = 2 * 3.14 * jari_jari
                 print ("Luas Lingkaran : ", luas_lingkaran, " m2")
                 print ("Keliling Lingkaran : ", keliling_lingkaran, " m")
            except ValueError :
                 print ("!!!- Masukan Angka -!!!")
                 os.system('cls')
                 continue
        elif pilihan == "jg":
            print ("/// MENGHITUNG LUAS DAN KELILING JAJAR GENJANG /// ")
            print ("Jajar Genjang Memiliki 4 sisi dan tinggi, dimana tiap 2 sisi yang sejajar memiliki panjang yang sama")
            print ("Jika sisi a mewakili sisi alas jajar genjang yang mendatar dan sisi b mewakili sisi miringnya, maka :")
            try:
                 sisi_a_jajargenjang=float(input("Panjang sisi a mendatar (m) : "))
                 sisi_b_jajargenjang=float(input("Panjang sisi b miring (m) : "))
                 tinggi_jajargenjang=float(input("Tinggi Jajargenjang (m) : "))
                 luas_jajargenjang= sisi_a_jajargenjang * tinggi_jajargenjang
                 keliling_jajargenjang= 2 * (sisi_a_jajargenjang + sisi_b_jajargenjang)
                 print ("Luas Jajargenjang : ", luas_jajargenjang, " m2")
                 print ("Keliling Jajargenjang : ", keliling_jajargenjang, " m")
            except ValueError:
                 print ("!!!- Masukan Angka -!!!")
                 os.system('cls')
                 continue
        elif pilihan == "tra":
            print ("/// MENGHITUNG LUAS DAN KELILING TRAPESIUM /// ")
            print ("Trapesium memiliki 4 sisi, sisi alas (a), sisi yang sejajar dengan alas (c), dan 2 sisi miring (b dan d)")
            try:
                 sisi_a_tra=float(input("Panjang Sisi Alas Trapesium (m) : "))
                 sisi_c_tra=float(input("Panjang Sisi Sejajar Alas (m) : "))
                 sisi_b_tra=float(input("Panjang Sisi Miring Kanan (m) : "))
                 sisi_d_tra=float(input("Panjang Sisi Miring Kiri (m) : "))
                 tinggi_tra=float(input("Tinggi Trapesium (m) : "))
                 luas_tra= 1/2 * (sisi_a_tra + sisi_c_tra) * tinggi_tra
                 keliling_tra= sisi_a_tra + sisi_b_tra + sisi_c_tra + sisi_d_tra
                 print("Luas Trapesium : ", luas_tra, " m2" )
                 print("Keliling Trapesium : ", keliling_tra, " m" )
            except ValueError:
                 print("!!!- Masukan Angka -!!!")
                 os.system('cls')
                 continue
        elif pilihan == "lay":
             print ("/// MENGHITUNG LUAS DAN KELILING LAYANG-LAYANG /// ")
             print ("Layang-layang memiliki 4 sisi, dimana 2 sisi memiliki panjang yang berbeda, sisi a lebih panjang dibandingkan sisi b dan dua sisi lainnya yaitu sisi c sejajar sisi b dan sisi d sejajar dengan sisi a")
             print ("Layang-layang memiliki 2 diagonal dengan panjang yang berbeda, yaitu d1 dan d2")
             try:
                  d1_lay=float(input("Panjang Diagonal 1 (m) : "))
                  d2_lay=float(input("Panjang Diagonal 2 (m) : "))
                  sisi_a_lay=float(input("Panjang sisi terpanjang (m) : "))
                  sisi_b_lay=float(input("Panjang sisi terpendek (m) : "))
                  luas_lay= 1/2 * d1_lay * d2_lay
                  keliling_lay= 2 * (sisi_a_lay + sisi_b_lay)
                  print ("Luas Layang-Layang : ", luas_lay, " m2")
                  print ("Keliling Layang-Layang : ", keliling_lay, " m")
             except ValueError:
                 print ("!!!- Masukan Angka -!!!")
                 os.system('cls')
                 continue
        elif pilihan == "bk":
             print("/// MENGHITUNG LUAS DAN KELILING BELAH KETUPAT ///")
             print("Belah Ketupat memiliki 4 sisi yang sama panjang (sisi a) dengan 2 panjang diagonal yang berbeda, d1 dan d2")
             try:
                  d1_bk=float(input("Panjang Diagonal 1 (m) : "))
                  d2_bk=float(input("Panjang Diagonal 2 (m) : "))
                  sisi_a_bk=float(input("Panjang Sisi (m) : "))
                  luas_bk= 1/2 * d1_bk * d2_bk
                  keliling_bk = 4 * sisi_a_bk
                  print ("Luas Belah Ketupat : ", luas_bk, " m2")
                  print ("Keliling Belah Ketupat : ", keliling_bk, " m")
             except ValueError:
                  print ("!!!- Masukan Angka -!!!")
                  os.system('cls')
                  continue
        else :
            print ("!!!- Masukan Kode Dengan Benar -!!!")
        ulangi=input("Ulangi Program ? (y/n)")
        if ulangi=="y":
            os.system('cls')
            continue
        if ulangi=="n":
            print("APLIKASI KELUAR")
            break
        else:
            print ("Masukan y untuk lanjut atau n untuk keluar")
            
            

hitung_bidang()

