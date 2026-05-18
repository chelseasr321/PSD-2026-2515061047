A. Judul Program
“Implementasi Stack Array pada Riwayat Browser”
 
B. Deskripsi Program
Program ini dibuat untuk mengelola riwayat browser menggunakan stack array. Setiap halaman web yang dibuka akan disimpan ke dalam stack sebagai riwayat pencarian. Sistem bekerja dengan konsep LIFO (Last In First Out), yaitu halaman terakhir yang dibuka akan menjadi halaman teratas pencarian atau halaman pertama yang dapat diakses kembali. Pada program ini terdapat beberapa menu, seperti mencari halaman website, melihat riwayat halaman yang telah dibuka, menghapus halaman yang terakhir di akses, melihat halaman yang pertama diakses serta menu keluar dari browser. 

C. Source Code 
<img width="848" height="441" alt="Screenshot 2026-05-17 105126" src="https://github.com/user-attachments/assets/4ab5a706-2f11-471c-bef6-5490455fa1e2" />
<img width="845" height="424" alt="Screenshot 2026-05-17 105143" src="https://github.com/user-attachments/assets/e47d1e95-5024-415d-9e75-33dd06289cb9" />
<img width="848" height="143" alt="Screenshot 2026-05-17 105153" src="https://github.com/user-attachments/assets/18cd86c4-2443-45ff-b608-f3ac16764939" />

Penjelasan Code Perbaris:
1. Fungsi untuk membuat class StackArray
2. Digunakan untuk menyiapkan stack di awal program, pada baris diatas kapasitas maksimal stack adalah 5
3. Variabel max digunakan untuk menyimpan kapasitas maksimal pada baris sebelumnya yaitu 5
4. Membuat array kosong untuk menyimpan data
5. Fungsi untuk menentukan posisi awal top stack, menggunakan -1 karena index array pada python di mulai dari 0
6. -
7. Fungsi untuk mengecek apakah stack kosong
8. Mengembalikan nilai true jika top_idx stack sama dengan -1 yang berarti stack kosong
9. -
10. Fungsi untuk mengecek apakah stack penuh
11. Mengembalikan nilai true jika stack mencapai batas index akhir
12. -
13. Fungsi untuk menambahkan halaman baru ke stack
14. Fungsi untuk mengecek apakah stack sudah penuh sebelum menambahkan data
15. Fungsi untuk menampilkan kata “Halaman Gagal Ditambahkan” ketika stack penuh
16. Fungsi untuk menghentikan proses penambahan data jika stack penuh
17. Fungsi untuk memindahkan posisi top ke index berikutnya saat menambahkan data baru ke stack.
18. Fungsi untuk menyimpan data baru ke dalam stack sesuai posisi top saat ini.
19. Fungsi untuk menampilkan halaman baru berhasil dibuka
20. -
21. Fungsi untuk menghapus halaman yang terakhir di akses
22. Fungsi untuk mengecek apakah stack kosong sebelum menghapus data
23. Fungsi untuk mencetak kata “Tidak ada riwayat pencarian” ketika stack dalam keadaan kosong
24. Fungsi return untuk memberhentikan fungsi jika stack kosong
25. Fungsi untuk menampilkan halaman dengan posisi teratas yang berhasil dihapus, ketika stack tidak dalam keadaan kosong
26. Fungsi untuk menurunkan posisi top, dimana jika posisi paling atas di hapus maka posisi top turun ke data sebelumnya
27. -
28. Fungsi untuk melihat halaman paling atas
29. Fungsi untuk mengecek apakah stack kosong
30. Fungsi untuk menampilkan pesan “Tidak ada riwayat pencarian” jika stack kosong
31. Fungsi untuk menghentikan proses pencarian jika stack kosong
32. Fungsi untuk menampilkan halaman teratas pada stack
33. -
34. Fungsi untuk menampilkan seluruh isi stack
35. Fungsi untuk mengecek apakah stack kosong
36. Fungsi untuk menampilkan pesan “Tidak ada riwayat pencarian” jika stack kosong
37. Fungsi untuk menghentikan proses pencarian jika stack kosong
38. Fungsi untuk menampilkan kata “Riwayat pencarian: “
39. Melakukan perulangan untuk menampilkan data pencarian keseluruhan, dari paling bawah atau terakhir masuk sampai yang pertama
40. Fungsi untuk mengambil isi stack di posisi index i untuk ditampilkan, kemudian fungsi end=", " if i != 0 else "" untuk memberi pemisah koma antar riwayat, kemudian pada riwayat halaman yang terakhir di akses tidak menggunkan koma
41. -
42. Fungsi untuk membuat baris baru agar output lebih rapi
43. -
44. -
45. Membuat fungsi main atau fungsi utama program
46. Fungsi untuk membuat objek StackArray untuk menyimpan riwayat browser
47. Variabel pilih untuk menyimpan pilihan menu yang diinputkan user
48. Fungsi perulangan yang digunakan agar menu terus tampil sampai user memilih menu keluar
49. Menampilkan judul program “Implementasi Stack Array pada Riwayat Browser” 
50. Fungsi untuk menampilkan menu pertama “1. Masuk ke halaman”
51. Fungsi untuk menampilkan menu kedua “2. Hapus halaman terakhir”
52. Fungsi untuk menampilkan menu ketiga “3. Tampilkan halaman pertama”
53. Fungsi untuk menampilkan menu keempat “4. Tampilkan halaman”
54. Fungsi untuk menampilkan menu kelima “5. Keluar dari browser”
55. Fungsi untuk mencoba menjalankan program
56. Fungsi untuk meminta input menu dari user
57. Fungsi untuk menangani kesalahan input jika yang diinput bukan berupa angka
58. Fungsi untuk menampilkan pesan “Input tidak valid” jika yang diinput bukan berupa angka
59. Fungsi untuk mengulang perulangan dari awal jika terjadi error tanpa menjalankan kode dibawahnya
60. Fungsi jika user menginputkan angka 1
61. Fungsi untuk mencoba menjalankan program
62. Fungsi untuk meminta user menginputkan halaman yang akan dibuka ketika sebelumnya pengguna menginput angka 1 atau menu masuk ke halaman
63. Fungsi untuk menambahkan data kedalam stack
64. Fungsi untuk menangani kesalahan input jika yang diinput bukan berupa kata
65. Fungsi untuk menampilkan pesan “Input tidak valid” jika yang diinput bukan berupa kata
66. Fungsi yang dijalankan ketika user memilih menu kedua yaitu menu hapus halaman terakhir
67. Memanggil fungsi pop untuk menghapus halaman terakhir
68. Fungsi yang dijalankan ketika user memilih menu ketiga yaitu melihat halaman teratas
69. Memanggil fungsi peek untuk menampilkan halaman teratas
70. Fungsi yang dijalankan ketika user memilih menu keempat yaitu menu untuk menampilkan seluruh riwayat halaman yang diakses
71. Memanggil fungsi display untuk menampilkan seluruh riwayat halaman
72. Fungsi yang dijalankan ketika user memilih menu kelima yaitu keluar dari browser
73. Fungsi untuk menampilkan pesan “Riwayat pencarian ditutup”
74. Jika user memilih pilihan menu yang tidak tersedia
75. Program menampilkan pesan “Pilihan tidak valid”
76. -
77. -
78. Fungsi untuk menjalankan program
79. Memanggil variabel main

D. Output Program
<img width="845" height="443" alt="Screenshot 2026-05-17 105316" src="https://github.com/user-attachments/assets/c56d5e9e-f67a-4e1a-ba59-d9d5065ef8fe" />
<img width="842" height="448" alt="Screenshot 2026-05-17 105333" src="https://github.com/user-attachments/assets/c721dc26-cd08-4dbf-bbeb-72d23a7f0821" />
<img width="843" height="200" alt="Screenshot 2026-05-17 105348" src="https://github.com/user-attachments/assets/47ec6709-341c-4a14-add0-f16053e7e9a1" />

Penjelasan Output:
Program menampilkan judul program yaitu “Implementasi Stack Array Pada Riwayat Browser” kemudian program menampilkan 5 pilihan menu yaitu 1. Masuk ke halaman, 2. Hapus halaman terakhir, 3. Tampilkan halaman pertama, 4. Tampilkan halaman dan 5. Keluar dari browser. User menginputkan menu 1 dan menginput halaman yang akan dicari yaitu Youtube kemudian program menampilkan output Halaman Youtube berhasil dibuka. User kembali menginputkan menu 1 dan menginput halaman yang akan dicari yaitu Github kemudian program menampilkan output Halaman Github berhasil dibuka. User menginputkan menu 1 dan menginput halaman yang akan dicari yaitu Vclass kemudian program menampilkan output Halaman Vclass berhasil dibuka. User menginputkan menu 1 dan menginput halaman yang akan dicari yaitu Spotify kemudian program menampilkan output Halaman Spotify berhasil dibuka. User menginputkan menu 1 dan menginput halaman yang akan dicari yaitu Google Scholar kemudian program menampilkan output Google Scholar berhasil dibuka. User menginputkan menu 4 kemudian program menampilkan output riwayat pencarian secara keseluruhan yaitu Riwayat Pencarian: Google Scholar, Spotify, Vclass, Github, Youtube. User menginputkan menu 2 yaitu menu untuk menghapus halaman terakhir kemudian program menampilkan output Halaman Google Scholar berhasil dihapus. User menginputkan menu 3 yaitu tampilkan halaman pertama kemudian program menampilkan output Halaman teratas adalah: Spotify. User menginputkan menu 4 yaitu tampilkan halaman, output menampilkan riwayat pencarian halaman terbaru yaitu Riwayat Pencarian: Spotify, Vclass, Github, Youtube. User menginputkan menu 5 yaitu menu keluar dari browser.  kemudian program menampilkan output Riwayat pencarian ditutup.

E. Link Youtube
https://youtu.be/A7lJxoj0kPY
