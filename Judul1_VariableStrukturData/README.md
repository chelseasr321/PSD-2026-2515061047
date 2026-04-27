A. Judul Program
“PROGRAM PENGOLAHAN DATA NILAI MAHASISWA TEKNIK INFORMATIKA”

B. Deskripsi Program
Program ini dibuat untuk mengelola data nilai mahasiswa Teknik Informatika dengan 7 menu yaitu Input Data Mahasiswa yang diminta untuk menginput nama dan NPM mahasiswa, Lihat Address Data Nilai untuk melihat alamat nilai mahasiswa pada sistem, Lihat Address Tiap Nilai Mata Kuliah untuk melihat alamat nilai tiap nilai mata kuliah, Input Nilai Mahasiswa untuk menginputkan nilai mata kuliah sebanyak 10 nilai, Tampilkan Semua Nilai untuk menampilkan hasil nilai tertinggi, terendah, dan rata-rata, Cek Nilai Mata Kuliah Tertentu untuk mengecek nilai berdasarkan indeks dan terakhir menu Keluar. Program ini menggunakan bahasa pemrograman python dengan percobaan List 1D.

C. Source Code 
<img width="1920" height="1008" alt="Screenshot 2026-04-27 161230" src="https://github.com/user-attachments/assets/4300b784-1bf5-47b6-afa6-38def0698ae3" />
<img width="1920" height="1008" alt="Screenshot 2026-04-27 161252" src="https://github.com/user-attachments/assets/fa927513-d67f-4d31-bb56-4bdbcca3d61d" />
<img width="1920" height="1008" alt="Screenshot 2026-04-27 161304" src="https://github.com/user-attachments/assets/f28305bf-a5d8-493b-b9cd-88eb88598a32" />

Penjelasan Code Perbaris:
1. Membuat fungsi menu untuk menampilkan daftar pilihan program 
2. Membuat fungsi print judul program
3. Membuat fungsi print menu
4. Membuat fungsi print Input Data Mahasiswa
5. Membuat fungsi print Lihat Address Data Nilai
6. Membuat fungsi print Lihat Address Tiap Nilai Mata Kuliah
7. Membuat fungsi print Input Nilai Mahasiswa
8. Membuat fungsi print Tampilkan Semua Nilai
9. Membuat fungsi print Cek Nilai Mata Kuliah Tertentu
10. Membuat fungsi print Keluar
11. -
12. Membuat fungsi main untuk menjalankan program
13. Membuat list berisi 10 elemen
14. Untuk mengontrol perulangan program
15. -
16. Berarti program akan terus berjalan sampai running = false
17. Memanggil fungsi menu
18. Program mencoba menjalankan kode
19. Membuat fungsi pilihan menu
20. Fungsi untuk mengatasi jika input bukan berupa angka
21. Membuat fungsi print masukkan angka valid jika yang dimasukkan bukan angka
22. Untuk mengembalikan ke perulangan
23. -
24. Membuat fungsi untuk menjalankan program jika pilihan menu yang diinput adalah angka 1
25. Membuat fungsi input nama mahasiswa
26. Membuat fungsi menginput NPM mahasiswa
27. -
28. Membuat fungsi untuk menjalankan program jika pilihan menu yang diinput adalah angka 2
29. Membuat fungsi untuk menampilkan alamat data nilai siswa pada sistem
30. -
31. Membuat fungsi untuk menjalankan program jika pilihan menu yang diinput adalah angka 3
32. Membuat perulangan untuk menghasilkan 10 elemen
33. Membuat fungsi untuk print address dari 10 nilai mata kuliah
34. -
35. Membuat fungsi untuk menjalankan program jika pilihan menu yang diinput adalah angka 4
36. Membuat fungsi print 10 nilai mata kuliah
37. Membuat perulangan untuk menghasilkan 10 elemen
38. Membuat perulangan selama program benar
39.Program mencoba menjalankan kode
40. Membuat fungsi untuk menginput nilai mata kuliah
41. Untuk menghentikan perulangan
42. Fungsi untuk mengatasi jika input bukan berupa angka
43. Membuat fungsi print input tidak valid, silahkan masukkan nilai
44. -
45. Membuat fungsi untuk menjalankan program jika pilihan menu yang diinput adalah angka 5
46. Membuat fungsi print Hasil nilai mahasiswa
47. Membuat fungsi print nama mahasiswa yang sudah diinputkan dengan memanggil variabel nam
48. Membuat fungsi print NPM dengan memanggil variabel npm
49. Membuat fungsi print Daftar nilai dengan memanggil variabel a
50. Membuat fungsi print nilai tertinggi, menghitung nilai tertinggi dengan fungsi max(a)
51. Membuat fungsi print nilai terendah, menghitung nilai terendah dengan fungsi min(a)
52. Membuat fungsi print rata rata, menghitung nilai rata rata dengan fungsi sum(a)/len(a)
53. -
54. Membuat fungsi untuk menjalankan program jika pilihan menu yang diinput adalah angka 6
55. Membuat fungsi untuk mengecek nilai mata kuliah dengan menginputkan index
56. Program mencoba menjalankan kode
57. Membuat fungsi untuk print nilai mata kuliah sesuai index yang diinputkan
58. Fungsi untuk mengatasi jika input bukan berupa angka
59. Membuat fungsi print input harus berupa angka jika yang diinputkan bukan angka
60. -
61. Membuat fungsi untuk menjalankan program jika pilihan menu yang diinput adalah angka 7
62. Untuk menghentikan perulangan
63. Membuat fungsi untuk print program selesai
64. Menjalankan kode ketika kondisi sebelumnya tidak terpenuhi
65. Membuat fungsi print pilihan tidak valid
66. -
67. Agar program berjalan ketika di running
68. Memanggil variabel main

D. Output Program
<img width="1920" height="1008" alt="Screenshot 2026-04-27 172427" src="https://github.com/user-attachments/assets/c8d4ec9d-cf77-48d9-9605-c0842dfce677" />
<img width="1920" height="1008" alt="Screenshot 2026-04-27 161406" src="https://github.com/user-attachments/assets/f78479e3-db1f-4d6f-9556-bc87a0c2635a" />
<img width="1920" height="1008" alt="Screenshot 2026-04-27 161419" src="https://github.com/user-attachments/assets/ced63339-0aa9-4363-8c4c-fc47e4e7a6a9" />
<img width="1920" height="1008" alt="Screenshot 2026-04-27 161429" src="https://github.com/user-attachments/assets/8e9afaf8-edeb-425a-b990-b7ced2f4a95b" />
Penjelasan Output:
Program menampilkan 7 menu jika kita menginputkan angka 1 pada pilihan menu maka menghasilkan output untuk menginput nama mahasiswa dan NPM. Lalu jika kita menginputkan angka 2 pada pilihan menu akan menghasilkan output address dari data nilai siswa. Jika kita menginputkan angka 3 pada pilihan menu maka akan menampilkan 10 address dengan index dari 0-9. Jika menginputkan angka 4  pada pilihan menu, kita akan diminta menginputkan 10 nilai mata kuliah dengan index 0-9. Lalu ketika kita menginputkan angka 5 pada pilihan menu akan menampilkan data mahasiswa, seperti Nama, NPM, Daftar nilai, Nilai tertinggi, Nilai terendah dan Rata rata nilai mahasiswa. Lalu saat menginputkan angka 6 pada pilihan menu, kita bisa mengecek nilai mata kuliah mahasiswa dengan menginputkan index, pada output diatas index yang di cek adalah index ke 2 dan menampilkan nilai mata kuliah 95 sesuai dengan data nilai sebelumnya yaitu: a[0] = 70, a[1] = 80, a[2] = 95, a[3] = 85, a[4] = 80, a[5] = 90, a[6] = 70, a[7] = 75, a[8] = 80, a[9] = 90. Terakhir jika kita menginputkan angka 7 terdapat menu keluar berarti maka program telah selesai.

E. Link Youtube
https://youtu.be/qKahwSsBgrk?si=EItROJp7aeABuoCu



