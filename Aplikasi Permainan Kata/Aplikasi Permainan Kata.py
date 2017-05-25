"""
Aplikasi Permainan Kata
Diprogram oleh : Prima Akbar Mashudi,ST

Deskripsi :
Aplikasi Permainan Kata merupakan aplikasi berbasis python sederhana yang prinsipnya mengubah karakter kata yang dimasukan user menjadi sebuah kata dimana kata pertama akan dipindahkan ke akhir kata ditambah dengan imbuhan belakang
Hasi kata baru lowercase
Contohnya :
User menginput kata "DAPUR"
Maka kata baru yang dihasilkan menjadi "apurdoh"

"""
#===================Judul Aplikasi======================================
print ("APLIKASI PERMAINAN KATA")
#=======================================================================

kata=raw_input("Silahkan Masukan Kata Yang Anda Inginkan :").lower() #Perintah untuk memasukan input dari user
imbuhan_belakang="oh"

if len(kata) > 0 and kata.isalpha(): #Untuk memfilter kata apabila kosong atau berisi angka
    kata_baru=kata[1:len(kata)]
    kata_pertama=kata[0]
    print "Hasil:", kata_baru + kata_pertama + imbuhan_belakang
else :
    print "Tidak boleh kosong atau berisi angka"

#Selesai
#Happy Coding with Python
#Email : primakbar@yahoo.com
#Handphone : 081312014810


