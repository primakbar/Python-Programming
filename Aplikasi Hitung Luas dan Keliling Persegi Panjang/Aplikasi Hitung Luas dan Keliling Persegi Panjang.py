"""
Program Sederhana Mencari Luas dan Keliling Persegi Panjang
Dibuat oleh : Prima Akbar Mashudi,ST

"""
print ("APLIKASI PENGHITUNG LUAS DAN KELILING PERSEGI PANJANG")
print ("Oleh : Prima Akbar Mashudi,ST")

#Panjang Lebar Dalam Satuan Meter
#Masukan Data Panjang dan Lebar Dalam Satuan Meter
panjang_meter = float (input("Masukan Data Panjang Dalam Meter :")) #Sesuaikan input panjang yang diinginkan
lebar_meter = float(input("Masukan Data Lebar Dalam Meter :")) #Sesuaikan input lebar yang diinginkan


#Rumus Menghitung Luas Persegi Panjang = Panjang x Lebar

#Luas Dalam m2
luas_m2=panjang_meter * lebar_meter
luas_m2="%.2f" % luas_m2 #Tipenya String

#Mengubah string ke float menggunakan perintah float()
#Luas Dalam Ha
luas_ha= float(luas_m2) / 10000.00 #pembagi harus 2 desimal
luas_ha = "%.2f" % luas_ha #Tipenya String

#Rumus menghitung keliling persegi panjang = 2 x (panjang+lebar)
keliling_meter = float(2 * (panjang_meter+lebar_meter))

#Presentasi Hasil
print "Berikut Hasil Perhitungan Luas dan Keliling Dengan Data Sebagai Berikut :"
print "Panjang :", panjang_meter, "meter"
print "Lebar :", lebar_meter, "meter"
print "Luas :", luas_m2, "m2", "atau sama dengan", luas_ha, "hektar"
print "Keliling :", keliling_meter, "meter"
#Selesai
#Dibuat oleh : Prima Akbar Mashudi,ST
#Email : primakbar@yahoo.com
#Handphone : 081312014810