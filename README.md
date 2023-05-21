# BoyerMoore-SaitamaCode
#Satria Aditama Prasetya - 11210910000019 (TI UIN 21)

Algoritma Boyer-Moore tidak menggunakan rumus perhitungan yang khusus seperti pada algoritma matematis. Namun, terdapat beberapa aturan atau prinsip yang digunakan dalam algoritma ini: Tabel Bad Character Shift: Untuk setiap karakter dalam pola, tabel ini memetakan karakter ke pergeseran yang harus dilakukan jika terjadi ketidakcocokan pada karakter tersebut. Pergeseran ini didasarkan pada kemunculan terakhir karakter dalam pola. Aturan Good Suffix: Aturan ini digunakan ketika ada kesamaan sufiks dalam pola yang cocok dengan sufiks dalam teks. Aturan ini memanfaatkan informasi tentang sufiks yang cocok sebelumnya untuk menentukan pergeseran yang harus dilakukan. Pada dasarnya, algoritma Boyer-Moore mencoba memaksimalkan pergeseran yang dilakukan untuk menghindari perbandingan ulang yang tidak perlu. Dengan memanfaatkan tabel bad character shift dan aturan good suffix, algoritma ini dapat mencapai efisiensi yang tinggi dalam pencarian pola dalam teks.

Algoritma Boyer-Moore digunakan untuk melakukan pencarian pola atau string matching dalam sebuah teks. Untuk memahami perhitungannya secara manual, berikut adalah contoh perhitungan langkah demi langkah menggunakan algoritma Boyer-Moore.

Misalkan kita memiliki teks ABCDABDABDABE dan pola yang ingin dicari adalah ABDABE.

Langkah 1: Membuat tabel bad character shift

markdown
Copy code
Karakter  | Shift
-----------------
A         | 4
B         | 1
D         | 0
E         | 5
Tabel ini berisi pergeseran yang harus dilakukan jika terjadi ketidakcocokan pada karakter pola dengan karakter teks. Jika karakter pola tidak ada dalam teks, maka pergeseran dilakukan sejauh panjang pola.

Langkah 2: Memulai pencarian

Membandingkan pola dengan teks mulai dari posisi paling kanan pola.
Jika seluruh karakter cocok, maka pola ditemukan di teks.
Jika terjadi ketidakcocokan pada karakter tertentu, kita menggunakan tabel bad character shift untuk menentukan pergeseran yang harus dilakukan.
Berikut adalah perhitungan langkah demi langkah menggunakan contoh di atas:

Langkah 1:

makefile
Copy code
Teks: ABCDABDABDABE
Pola:     ABDABE
Langkah 2:

Membandingkan karakter terakhir pola (E) dengan karakter teks di posisi yang sama.
Ketidakcocokan terjadi karena E tidak sama dengan D.
Menggunakan tabel bad character shift, pergeseran yang harus dilakukan adalah 5 (panjang pola).
Langkah 3:

makefile
Copy code
Teks: ABCDABDABDABE
Pola:    ABDABE
Langkah 4:

Membandingkan karakter terakhir pola (E) dengan karakter teks di posisi yang sama.
Ketidakcocokan terjadi karena E tidak sama dengan B.
Menggunakan tabel bad character shift, pergeseran yang harus dilakukan adalah 5 (panjang pola).
Langkah 5:

makefile
Copy code
Teks: ABCDABDABDABE
Pola:   ABDABE
Langkah 6:

Membandingkan karakter terakhir pola (E) dengan karakter teks di posisi yang sama.
Ketidakcocokan terjadi karena E tidak sama dengan A.
Menggunakan tabel bad character shift, pergeseran yang harus dilakukan adalah 4.
Langkah 7:

makefile
Copy code
Teks: ABCDABDABDABE
Pola:  ABDABE
Langkah 8:

Membandingkan karakter terakhir pola (E) dengan karakter teks di posisi yang sama.
Ketidakcocokan terjadi karena E tidak sama dengan B.
Menggunakan tabel bad character shift, pergeseran yang harus dilakukan adalah 1.
Langkah 9:

makefile
Copy code
Teks: ABCDABDABDABE
Pola: ABDABE
Langkah 10:

Membandingkan karakter terakhir pola (E) dengan karakter teks di posisi yang sama.
Cocok! Seluruh karakter pola cocok dengan karakter
