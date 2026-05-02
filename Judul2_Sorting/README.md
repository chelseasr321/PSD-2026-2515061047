A. Judul Program
“Program Pengurutan Daftar Mata Kuliah Mahasiswa Teknik Informatika”

B. Deskripsi Program
Program ini dibuat untuk mengurutkan Daftar Mata Kuliah Mahasiswa Teknik Informatika dengan menggunakan salah satu jenis sorting yaitu Exchange Sort dimana pada jenis pengurutan ini kita mengambil satu elemen pada array lalu menjadikannya acuan untuk membandingkan dengan seluruh elemen lain pada array. Program ini menggunakan tipe data string, untuk pengurutan dengan tipe data string proses pengurutan dilakukan dengan melihat huruf elemen pertama pada data tersebut lalu menyesuaikan dengan urutan alfabet, jika pada elemen pertama terdapat huruf yang sama maka bisa melihat elemen kedua dan seterusnya hingga data berurutan.

C. Source Code 
<img width="1382" height="835" alt="Screenshot 2026-05-01 215912" src="https://github.com/user-attachments/assets/fa3d0bf3-1abc-4362-9e6e-4436d98fb248" />
<img width="1362" height="516" alt="Screenshot 2026-05-01 215937" src="https://github.com/user-attachments/assets/41e62ddd-e425-4bea-967b-d6dd48fcc415" />
Penjelasan Code Perbaris:
1. Fungsi untuk menukar elemen i dan j dalam array
2. Fungsi untuk menyimpan nilai i pada variabel sementara
3. Fungsi untuk mengganti nilai i dengan nilai j
4. Fungsi untuk mengganti nilai j dengan nilai i yang sebelumnya disimpan pada variabel sementara
5. -
6. -
7. Fungsi untuk mengurutkan elemen dengan metode exchange sort
8. Fungsi perulangan sesuai dengan jumlah data yg dimasukkan lalu dikurang 1, fungsi ini untuk menentukan posisi elemen yang sedang di cek
9. Fungsi untuk membandingkan elemen pertama dengan semua elemen setelahnya sampai index terakhir
10. Fungsi untuk menentukan urutan tersebut Ascending atau Descending
11. Fungsi untuk menukar posisi agar sesuai 
12. -
13. Fungsi untuk mencetak judul program yaitu “Program Pengurutan Daftar Mata Kuliah Mahasiswa Teknik Informatika”
14. -
15. Fungsi untuk menjalankan program
16. Program mencoba untuk menjalankan kode
17. n dipakai untuk menyimpan data yang akan diinput, fungsi selanjutnya untuk meminta user memasukkan jumlah mata kuliah
18. Fungsi untuk mengatasi jika input bukan berupa angka karena pada baris ke 17 tipe data yang diminta yaitu integer
19. Mencetak output “Input tidak valid!” jika yang diinputkan bukan angka
20. Fungsi untuk memberhentikan fungsi main
21. Membuat array kosong yang nantinya akan diisi dengan input oleh user
22. Mencetak teks “Masukkan Nama Mata Kuliah:” 
23. Fungsi untuk mengulang perintah sebanyak n kali
24. Membuat perulangan sampai kondisi tertentu terpenuhi
25. Program mencoba untuk menjalankan kode
26. a dipakai untuk menyimpan data yang akan diinput lalu fungsi selanjutnya untuk membuat user menginputkan nama Mata Kuliah yang bertipe string dengan {i+1} untuk menampilkan nomor urutan yang dimulai dari 1
27. Fungsi untuk menambahkan data a ke dalam array
28. Fungsi untuk menghentikan perulangan
29. Fungsi untuk mengatasi jika input bukan berupa teks atau huruf karena pada baris ke 26 tipe data yang digunakan adalah string
30. Mencetak output "Input tidak valid, silahkan masukkan ulang!” jika yang diinput bukan teks
31. Fungsi untuk mencetak daftar mata kuliah sebelum diurutkan
32. Untuk memanggil fungsi sorting
33. Fungsi untuk mencetak daftar mata kuliah setelah diurutkan
34. Fungsi perulangan untuk mengakses elemen array dari 0 sampai n-1
35. Fungsi untuk mengecek apakah elemen yang dicetak bukan elemen terakhir
36. Fungsi untuk menampilkan elemen dengan tambahan koma dibelakangnya
37. Fungsi untuk menjalankan perintah jika kondisi if tidak terpenuhi, disini fungsi else untuk menangani agar program tidak menambahkan koma di elemen terakhir
38. Fungsi untuk menampilkan elemen tanpa tambahan koma pada elemen terakhir
39. Fungsi untuk mengakhiri output dan memisahkan dari output berikutnya
40. -
41. -
42. Fungsi agar program bisa berjalan ketika di running
43. Memanggil variabel main

D. Output Program
<img width="1364" height="484" alt="Screenshot 2026-05-01 215852" src="https://github.com/user-attachments/assets/ee43d92c-4e0a-41df-8bb0-a1584ccff73e" />
Penjelasan Output:
Program ini dibuat untuk mengurutkan daftar mata kuliah mahasiswa, langkah pertama user akan diminta untuk menginputkan jumlah mata kuliah, pada gambar diatas nilai yang diinputkan yaitu 5, artinya ada 5 daftar mata kuliah yang diinputkan diantaranya adalah Kalkulus, Struktur Data, Rekayasa Perangkat Lunak, Aljabar Matriks dan Teknik Digital. Output memperlihatkan daftar mata kuliah sebelum diurutkan dengan tampilan acak seperti apa yang diinputkan sebelumnya, kemudian program ini menghasilkan output daftar mata kuliah yang sudah diurutkan yaitu Aljabar Matriks, Kalkulus, Rekayasa Perangkat Lunak, Struktur Data, Teknik Digital.

E. Link Youtube
https://youtu.be/c-YFqhkQIp8?si=l2CCWKwwZ5OnGh_O
