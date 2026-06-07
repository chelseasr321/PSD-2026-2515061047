A. Judul Program
“Implementasi Hash Map Data Mahasiswa Menggunakan Metode Separate Chaining”
 
B. Deskripsi Program
Program ini dibuat untuk mengelola data mahasiswa menggunakan struktur data Hash Map dengan metode Separate Chaining. Program menyediakan beberapa operasi utama yaitu menambahkan data mahasiswa (insert), mencari data mahasiswa berdasarkan NIM (search), menampilkan seluruh data mahasiswa (display), dan menghapus data mahasiswa berdasarkan NIM (remove). Data mahasiswa disimpan dalam bentuk pasangan key-value, di mana NIM digunakan sebagai key dan nama mahasiswa digunakan sebagai value. Untuk menentukan lokasi penyimpanan data, program menggunakan fungsi hash yang menghitung indeks bucket pada hash table. Jika terdapat lebih dari satu data yang memiliki indeks bucket yang sama (collision), program mengatasinya menggunakan metode Separate Chaining, yaitu menyimpan data-data tersebut dalam bentuk linked list pada bucket yang sama. Program ini menggunakan bahasa pemrograman Python dengan implementasi kombinasi Hash Table dan Linked List untuk mempermudah pengelolaan serta pencarian data mahasiswa secara lebih efisien. 

C. Source Code 
<img width="729" height="430" alt="Screenshot 2026-06-07 105952" src="https://github.com/user-attachments/assets/5e16ef7c-d920-482b-80a7-c28e20d553cf" />
<img width="727" height="416" alt="Screenshot 2026-06-07 110003" src="https://github.com/user-attachments/assets/3cb5f8cd-c4a7-4540-ae28-124f6f6cf54a" />
<img width="731" height="431" alt="Screenshot 2026-06-07 110025" src="https://github.com/user-attachments/assets/afd8a0e4-4e53-4533-b264-de85bcd04a6e" />
Penjelasan Code Perbaris:
1. Membuat class Node yang berfungsi untuk menyimpan data pada linked list.
2. Constructor __init__ digunakan untuk menginisialisasi objek Node ketika dibuat.
3. Variabel key digunakan untuk menyimpan kunci data.
4. Variabel value digunakan untuk menyimpan nilai atau informasi yang terkait dengan key.
5. Variabel next digunakan sebagai penunjuk ke node berikutnya pada linked list.
6. -
7. -
8. Membuat class HashMapSeparateChaining sebagai struktur utama hash map.
9. Menginisialisasi hash map.
10. Variabel SIZE digunakan untuk menentukan jumlah kotak penyimpanan yang tersedia.
11. List table dibuat untuk menyimpan seluruh kotak penyimpanan pada hash table.
12. -
13. Fungsi hash_function digunakan untuk menentukan posisi penyimpanan data.
14. Melakukan operasi modulo. hasil indeks kemudian dikembalikan oleh fungsi.
15. -
16. Fungsi insert digunakan untuk menambahkan data baru ke hash map.
17. Pertama, program menghitung indeks kotak penyimpanan berdasarkan key.
18. Program mengambil data pertama pada kotak penyimpanan tersebut.
19. Dilakukan perulangan untuk menelusuri linked list pada kotak penyimpanan.
20. Program memeriksa apakah key yang dimasukkan sudah ada.
21. Jika key sudah ada, maka value akan diperbarui.
22. Proses insert dihentikan karena data sudah diperbarui.
23. Jika belum ditemukan, program berpindah ke node berikutnya.
24. Jika key belum ada, maka dibuat node baru.
25. Node baru dihubungkan dengan node yang sebelumnya berada di kotak penyimpanan.
26. Node baru dijadikan sebagai node pertama pada kotak penyimpanan tersebut.
27. -
28. Fungsi search digunakan untuk mencari data berdasarkan key.
29. Program menghitung indeks kotak penyimpanan dari key yang dicari.
30. Program mengambil node pertama pada kotak penyimpanan tersebut.
31. Perulangan dilakukan untuk menelusuri linked list.
32. Program membandingkan key yang dicari dengan key pada node.
33. Jika ditemukan, data langsung dikembalikan.
34. Jika belum ditemukan, program melanjutkan pencarian ke node berikutnya.
35. Jika seluruh node sudah dicek dan tidak ditemukan, fungsi mengembalikan nilai None.
36. -
37. Fungsi remove_key digunakan untuk menghapus data dari hash map.
38. Program menghitung indeks kotak penyimpanan berdasarkan key.
39. Program mengambil node pertama pada kotak penyimpanan tersebut.
40. Variabel prev digunakan untuk menyimpan node sebelumnya.
41. Perulangan dilakukan untuk mencari data yang akan dihapus.
42. Program memeriksa apakah key yang dicari ditemukan.
43. Jika node yang dihapus berada di posisi pertama kotak penyimpanan.
44. Maka head kotak penyimpanan diarahkan ke node berikutnya.
45. Jika kondisi sebelumnya tidak terpenuhi
46. Hubungan antar node diperbarui.
47. Fungsi mengembalikan nilai True sebagai tanda bahwa penghapusan berhasil.
48. Jika belum ditemukan, prev diperbarui.
49. Program berpindah ke node berikutnya.
50. Jika data tidak ditemukan, fungsi mengembalikan nilai False.
51. -
52. Fungsi display digunakan untuk menampilkan seluruh isi hash table.
53. Program menampilkan judul output.
54. Perulangan dilakukan untuk setiap kotak penyimpanan.
55. Nomor kotak penyimpanan ditampilkan terlebih dahulu.
56. Program mengambil node pertama pada kotak penyimpanan.
57. Linked list ditelusuri satu per satu.
58. Setiap key dan value ditampilkan ke layar.
59. Program berpindah ke node berikutnya hingga akhir linked list.
60. Setelah selesai, ditampilkan NULL sebagai penanda akhir linked list.
61. -
62. -
63. Fungsi main merupakan fungsi utama program.
64. Pada bagian ini dibuat objek hash map bernama mahasiswa.
65. Data mahasiswa Andi dimasukkan ke dalam hash map.
66. Data mahasiswa Budi dimasukkan ke dalam hash map.
67. Data mahasiswa Citra dimasukkan ke dalam hash map.
68. Data mahasiswa Dina dimasukkan ke dalam hash map.
69. -
70. Seluruh data yang telah dimasukkan ditampilkan menggunakan fungsi display.
71.-
72. Program melakukan pencarian terhadap NIM milik Budi.
73. Hasil pencarian disimpan pada variabel hasil.
74. Program memeriksa apakah data ditemukan.
75. Jika ditemukan, nama mahasiswa ditampilkan.
76. Jika tidak ditemukan, program menampilkan pesan bahwa data tidak ada.
77. -
78. Program menghapus data mahasiswa Budi menggunakan fungsi remove_key.
79. Setelah penghapusan selesai, ditampilkan informasi bahwa data telah dihapus.
80. Fungsi display dipanggil kembali untuk melihat kondisi hash table terbaru.
81. -
82. -
83. Agar program berjalan ketika di running
84. Memanggil fungsi main

D. Output Program
<img width="722" height="401" alt="Screenshot 2026-06-07 105704" src="https://github.com/user-attachments/assets/7bdc838e-32ea-4920-aaa8-c3eb7c242bbb" />
Penjelasan Output:
Program diawali dengan menampilkan isi Hash Table yang berisi data mahasiswa Andi, Budi, Citra, dan Dina. Pada output terlihat bahwa Andi, Budi, dan Citra berada pada bucket yang sama karena memiliki hasil hash yang sama, sehingga disimpan menggunakan metode Separate Chaining dalam bentuk linked list. Sementara itu, Dina berada pada bucket yang berbeda.
Selanjutnya program melakukan pencarian data mahasiswa dengan NIM 2217051011 dan berhasil menemukan data atas nama Budi, yang ditunjukkan oleh output "Mahasiswa Ditemukan = Budi". Setelah itu, program menghapus data Budi menggunakan fungsi remove_key(). Hasil tampilan akhir menunjukkan bahwa data Budi sudah berhasil dihapus dari bucket 1, sedangkan data mahasiswa lainnya tetap tersimpan dan tidak mengalami perubahan. Hal ini menunjukkan bahwa proses penyimpanan, pencarian, dan penghapusan data pada Hash Map telah berjalan dengan baik.

E. Link Youtube
