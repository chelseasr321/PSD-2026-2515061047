A. Judul Program
“Implementasi Stack Array pada Riwayat Browser”
 
B. Deskripsi Program
Program ini dibuat untuk mengelola sistem antrean kasir menggunakan metode Binary Search Tree (BST). Setiap nomor antrean pelanggan yang masuk akan disimpan ke dalam pohon biner berdasarkan urutan nilainya. Sistem bekerja dengan konsep nilai yang lebih kecil disimpan di sebelah kiri node induk dan nilai yang lebih besar disimpan di sebelah kanan node induk. Pada program ini terdapat beberapa menu, seperti menambahkan nomor antrean pelanggan, menghapus nomor antrean pelanggan yang sudah dilayani, menampilkan seluruh antrean pelanggan menggunakan traversal level-order, melihat tinggi pohon BST, mencari pelanggan berikutnya (successor), mencari pelanggan sebelumnya (predecessor), serta menu keluar dari program. 

C. Source Code 
<img width="1665" height="849" alt="Screenshot 2026-05-24 124633" src="https://github.com/user-attachments/assets/bd9e0e71-0995-4ce7-bc96-0f48f283e3a2" />
<img width="1660" height="864" alt="Screenshot 2026-05-24 124653" src="https://github.com/user-attachments/assets/64dc160a-b909-4dd2-9251-18235868cc51" />
<img width="1662" height="860" alt="Screenshot 2026-05-24 124708" src="https://github.com/user-attachments/assets/2311897f-2dd6-49fd-9196-146a7f65ecb8" />
<img width="1663" height="858" alt="Screenshot 2026-05-24 124724" src="https://github.com/user-attachments/assets/49749df9-f000-4ad8-9ba3-4e3a582165c7" />
<img width="1654" height="862" alt="Screenshot 2026-05-24 124739" src="https://github.com/user-attachments/assets/2ab778f4-2393-4ec5-a29d-9b061bd7079a" />
<img width="1662" height="869" alt="Screenshot 2026-05-24 124757" src="https://github.com/user-attachments/assets/88dddfa6-d50e-42e5-9ecb-9e7f06d5c009" />
<img width="1659" height="485" alt="Screenshot 2026-05-24 124813" src="https://github.com/user-attachments/assets/663b3b45-b4c4-493a-b5e3-6184eac0287a" />
Penjelasan Perbaris
1. Fungsi untuk membuat class node
2. Fungsi untuk menyiapkan node baru 
3. Variabel key digunakan untuk menyimpan nilai data yang di masukkan pada node
4. Variabel left digunakan untuk menyimpan nilai di subpohon kiri, yang awalnya bernilai None
5. Variabel right digunakan untuk menyimpan nilai di subpohon kanan, yang awalnya bernilai None
6. -
7. -
8. Fungsi untuk membuat class BSTLanjut
9. Fungsi untuk menyiapkan Binary Search Tree
10. Fungsi yang berarti variabel root digunakan sebagai akar pohon BST, awalnya bernilai None karena pohon masih kosong 
11. -
12. Fungsi untuk menambahkan node baru kedalam BST, self untuk menggambarkan objek dari class BSTLanjut, root untuk menyimpan data baru yang sedang dibandingkan dengan node yang sedang diperiksa, key untuk menyimpan data yang akan dimasukkan ke BST 
13. Fungsi untuk mengecek apakah root kosong 
14. Jika root kosong maka membuat node baru 
15. Fungsi untuk mengecek apakah nilai key lebih kecil dari root
16. Jika lebih kecil maka data dimasukkan ke subpohon kiri 
17. Fungsi untuk mengecek apakah nilai key lebih besar dari root 
18. Jika lebih besar maka data dimasukkan ke subpohon kanan
19.  Fungsi untuk mengembalikan root setelah proses insert sel 
20. -
21. Fungsi untuk memanggil proses insert 
22. Variabel root BST diisi dengan hasil penambahan node baru dari fungsi insert_node
23. -
24. Fungsi untuk mencari node dengan nilai paling kecil pada BST 
25. Variabel current digunakan untuk menyimpan node yang sedang diperiksa
Nilai awal current diisi dengan node root
26. Perulangan dilakukan selama node masih ada dan masih memiliki anak kiri. Kondisi current is not None digunakan untuk memastikan node tidak kosong. Kondisi current.left is not None digunakan untuk mengecek apakah masih ada subtree kiri 
27. Posisi current dipindahkan ke anak kiri, Proses ini dilakukan terus sampai menemukan node paling kiri
28. Fungsi mengembalikan node dengan nilai terkecil yang ditemukan
29. -
30. Fungsi untuk menghapus node dari BST berdasarkan nilai tertentu. root untuk menyimpan node yang sedang diperiksa, key untuk menyimpan nilai yang akan dihapus.
31. Fungsi untuk mengecek apakah node kosong
32. Jika node kosong maka fungsi mengembalikan None karena data tidak ditemukan
33. Fungsi untuk mengecek apakah nilai key lebih kecil dari root.key 
34. Jika lebih kecil maka proses penghapusan dilanjutkan ke subtree kiri 
35. Fungsi untuk mengecek apakah nilai key lebih besar dari root.key 
36. Jika lebih besar maka proses penghapusan dilanjutkan ke subtree kanan 
37. Fungsi yang dijalankan jika kondisi sebelumnya tidak terpenuhi
38. Fungsi untuk mengecek apakah node tidak memiliki anak kiri dan anak kanan 
39. Jika node tidak memiliki anak maka node langsung dihapus dengan mengembalikan None 
40. Fungsi untuk mengecek apakah node tidak memiliki anak kiri
41. Jika benar maka node digantikan oleh anak kanan
42. Fungsi untuk mengecek apakah node tidak memiliki anak kanan
43. Jika benar maka node digantikan oleh anak kiri
44. Fungsi yang dijalankan ketika kondisi sebelumnya tidak terpenuhi, dijalankan ketika node yang akan dihapus memiliki dua anak
45. Variabel successor digunakan untuk menyimpan node pengganti, Fungsi self.find_min_node(root.right) digunakan untuk mencari node dengan nilai paling kecil pada subtree kanan
46. Digunakan untuk mengganti nilai node yang akan dihapus dengan nilai successor. 
47. Digunakan untuk menghapus node successor yang asli pada subtree kanan. 
48. Fungsi untuk memperbarui dengan hasil delete pada subtree kanan. 
49.  -
50. Fungsi untuk menjalankan proses penghapusan data pada BST berdasarkan nilai key yang diinputkan user 
51. Fungsi delete_node() dipanggil untuk menghapus node, lalu hasil penghapusan digunakan untuk memperbarui root BST. 
52. -
53. Fungsi untuk menghitung tinggi atau height pada BST
54. Fungsi untuk mengecek apakah node kosong
55. Jika node kosong maka fungsi mengembalikan nilai -1
56. Variabel height_left digunakan untuk menyimpan tinggi subtree kiri. Fungsi self.height(root.left) untuk menghitung tinggi anak kiri
57. Variabel height_right digunakan untuk menyimpan tinggi subtree kanan. Fungsi self.height(root.right) dipanggil untuk menghitung tinggi anak kanan
58. Fungsi untuk mencari tinggi terbesar antara subtree kiri dan kanan
59. -
60. Fungsi untuk menampilkan data BST menggunakan traversal level-order
61. Fungsi untuk mengecek apakah root kosong
62. Jika root kosong maka program menampilkan tulisan “(kosong)”
63. Fungsi untuk menghentikan proses karena BST tidak memiliki data
64. Membuat list kosong untuk menyimpan node sementara saat traversal berlangsung
65. Fungsi untuk memasukkan root pertama ke dalam queue
66. Fungsi perulangan dilakukan selama queue masih memiliki isi
67. Variabel current digunakan untuk mengambil node paling depan dari queue menggunakan pop(0)
68. Fungsi untuk menampilkan nilai node saat ini tanpa pindah baris
69. Fungsi untuk mengecek apakah node saat ini memiliki anak kiri
70. Jika anak kiri ada maka node anak kiri dimasukkan ke dalam queue
71. Fungsi untuk mengecek apakah node saat ini memiliki anak kanan
72. Jika anak kanan ada maka node anak kanan dimasukkan ke dalam queue
73. Fungsi untuk membuat baris baru agar output lebih rapi setelah traversal selesai
74. -
75. Fungsi untuk mencari successor dari suatu node 
76. Variabel current digunakan untuk menyimpan node yang sedang diperiksa
77. Variabel successor digunakan untuk menyimpan successor sementara
78. Perulangan dilakukan selama node current masih ada atau tidak kosong
79. Fungsi untuk mengecek apakah nilai key lebih kecil dari current.key. Jika key lebih kecil maka node saat ini dapat menjadi successor
80. Variabel successor diisi dengan node current saat ini
81. Posisi current dipindahkan ke subtree kiri untuk mencari successor yang lebih kecil lagi tetapi tetap lebih besar dari key
82. Fungsi untuk mengecek apakah nilai key lebih besar dari current.key
83. Jika key lebih besar maka posisi current dipindahkan ke subtree kanan
84. Fungsi yang dijalankan ketika jika kondisi sebelumnya tidak terpenuhi
85. Fungsi break digunakan untuk menghentikan perulangan
86. Fungsi untuk mengecek apakah node dengan nilai key tidak ditemukan pada BST
87. Jika node tidak ditemukan maka fungsi mengembalikan None dan False
88. Fungsi untuk mengecek apakah node memiliki subtree kanan
89. Jika subtree kanan ada maka successor dicari menggunakan node terkecil pada subtree kanan dengan fungsi
90. Fungsi untuk mengecek apakah successor tidak ditemukan
91. Jika successor ada maka fungsi mengembalikan nilai successor dan True, sedangkan jika tidak ada maka mengembalikan None dan False
92. Fungsi untuk mengembalikan nilai successor dan tanda bahwa successor berhasil ditemukan 
93. -
94. Fungsi untuk mencari predecessor dari suatu node pada BST berdasarkan nilai key
95. Variabel current digunakan untuk menyimpan node yang sedang diperiksa
96. Variabel predecessor digunakan untuk menyimpan node sebelum key sementara
97. Perulangan dilakukan selama node current masih ada atau tidak kosong
98. Fungsi untuk mengecek apakah nilai key lebih besar dari current.key, jika key lebih besar maka node saat ini dapat menjadi predecessor
99. Variabel predecessor diisi dengan node current saat ini
100. Posisi current dipindahkan ke subtree kanan untuk mencari nilai yang lebih besar tetapi tetap lebih kecil dari key
101. Fungsi untuk mengecek apakah nilai key lebih kecil dari current.key
102. Jika key lebih kecil maka posisi current dipindahkan ke subtree kiri
103. Fungsi yang dijalankan jika kondisi sebelumnya tidak terpenuhi 
104. Fungsi break digunakan untuk menghentikan perulangan
105. Fungsi untuk mengecek apakah node dengan nilai key tidak ditemukan pada BST
106. Jika node tidak ditemukan maka fungsi mengembalikan None dan False
107. Fungsi untuk mengecek apakah node memiliki subtree kiri
108. Variabel temp digunakan untuk menyimpan subtree kiri sementara
109. Fungsi perulangan dilakukan selama subtree kanan dari temp masih ada
110. Posisi temp dipindahkan ke subtree kanan untuk mencari nilai terbesar pada subtree kiri
111. Nilai temp disimpan ke variabel predecessor karena merupakan predecessor sebenarnya
112. Fungsi untuk mengecek apakah predecessor tidak ditemukan
113. Jika predecessor ada maka fungsi mengembalikan nilai predecessor dan True, sedangkan jika tidak ada maka mengembalikan None dan False
114. Fungsi untuk mengembalikan nilai predecessor dan tanda bahwa predecessor berhasil ditemukan. 
115. -
116. -
117. Fungsi main untuk menjalankan program
118. Membuat objek bst dari class BSTLanjut untuk menyimpan data antrean pelanggan 
119. Variabel pilih digunakan untuk menyimpan pilihan menu yang diinputkan user 
120. Fungsi perulangan yang digunakan untuk memilih menu lalu, =! digunakan agar menu terus ditampilkan sampai user memilih angka 7
121. Fungsi untuk menampilkan judul program
122. Fungsi untuk untuk menampilkan menu menambahkan nomor antrean pelanggan 
123. Fungsi untuk menampilkan menu menghapus nomor antrean pelanggan yang selesai dilayani 
124. Fungsi untuk menampilkan menu melihat seluruh antrean pelanggan 
125. Fungsi untuk menampilkan menu melihat tinggi BST antrean 
126. Fungsi untuk menampilkan menu mencari successor atau pelanggan setelah nomor tertentu 
127. Fungsi untuk menampilkan menu mencari predecessor atau pelanggan sebelum nomor tertentu 
128. Fungsi untuk menampilkan menu keluar dari program 
129. Fungsi untuk mencoba menjalankan program
130. Fungsi yang dibuat agar user bisa menginputkan pilihan menu
131. Fungsi untuk menangani jika yang diinputkan bukan berupa tipe data integer
132. Fungsi untuk menampilkan pesan input tidak valid jika yang diinputkan bukan berupa tipe data integer
133. Fungsi menghentikan proses yang sedang berjalan lalu kembali ke awal perulangan 
134. Fungsi jika pengguna menginputkan angka 1
135. Fungsi untuk  mencoba menjalankan program
136. Fungsi agar user bisa menginputkan nomor antrean ketika memilih angka 1 di fungsi sebelumnya
137. Fungsi untuk memanggil fungsi insert() agar data atau nomor antrean x dimasukkan ke dalam BST
138. Fungsi untuk menampilkan bahwa nilai x berhasil dimasukkan
139. Fungsi untuk menangani kesalahan jika program tidak mmenginputkan nilai integer sebelumnya
140. Program akan menampilkan input tidak valid jika yang diinputkan bukan berupa integer
141. Fungsi jika pengguna menginputkan menu 2
142. Fungsi untuk mencoba menjalankan program
143. Fungsi yang dibuat agar pengguna bisa memasukkan nomor antrean (x) yang telah selesai setelah pengguna menginputkan menu 2
144. Fungsi untuk menghapus nilai x yang sebelumnya diinputkan
145. Fungsi untuk menampilkan pesan nomor antrean x berhasil dihapus
146. Fungsi untuk menangani kesalahan jika program tidak mmenginputkan nilai integer sebelumnya
147. Program akan menampilkan input tidak valid jika yang diinputkan bukan berupa integer
148. Fungsi jika pengguna menginputkan menu 3
149. Fungsi untuk menampilkan daftar antrean kasir
150. Digunakan digunakan untuk menampilkan isi BST berdasarkan level/tingkatan node. 
151. Fungsi jika pengguna menginputkan menu 4
152. Fungsi untuk menampilkan tinggi antrean
153. Fungsi jika pengguna menginputkan menu 5
154. Fungsi untuk mencoba menjalankan program
155. Fungsi yang dibuat agar pengguna dapat menginputkan nomor pelanggan untuk mencari pelanggan setelah nomor tersebut
156. Digunakan untuk memanggil fungsi pencarian successor pada BST
157. Fungsi yang dijalankan jika nilai ditemukan
158. Maka program akan menampilkan pesan pelanggan berikutnya adalah nomor {ans} sesuai nilai yang disimpan pada variabel sebelumnya
159. Fungsi yang dijalankan ketika kondisi sebelumnya tidak terpenuhi
160. Program akan menampilkan pesan bahwa tidak ada pelanggan berikutnya
161. Fungsi untuk menangani kesalahan input jika yang diinput bukan berupa integer
162. Fungsi untuk menampilkan pesan input tidak valid jika yang diinputkan bukan berupa integer
163. Fungsi jika program menginputkan menu 6
164. Fungsi untuk mencoba menjalankan program
165. Fungsi yang dibuat agar pengguna dapat menginputkan nomor antrean untuk mencari pelanggan sebelum nomor tersebut
166. Digunakan untuk memanggil fungsi pencarian predecessor pada BST
167. Fungsi yang dijalankan jika nilai ditemukan
168. Maka program akan menampilkan pesan pelanggan sebelumnya adalah nomor {ans} sesuai nilai yang disimpan pada variabel sebelumnya
169. Fungsi yang dijalankan ketika kondisi sebelumnya tidak terpenuhi
170. Fungsi untuk menampilkan pesan bahwa tidak ada pelanggan sebelumnya
171. Fungsi untuk menangani kesalahan input jika yang diinputkan bukan berupa integer
172. Fungsi agar program menampilkan pesan input tidak valid
173. Fungsi jika pengguna menginputkan menu 7
174. Fungsi untuk menampilkan pesan program selesai
175. Fungsi yang dijalankan ketika kondisi sebelumnya tidak terpenuhi
176. Fungsi untuk menampilkan pesan pilihan tidak valid jika pengguna menginputkan menu selain yang disediakan
177. -
178. -
179. Fungsi untuk menjalankan program
180. Fungsi untuk memanggil variabel main

D. Output Program
<img width="1644" height="878" alt="Screenshot 2026-05-23 223430" src="https://github.com/user-attachments/assets/25add09f-35ef-4b87-ab45-e96af1735aec" />
<img width="1652" height="866" alt="Screenshot 2026-05-23 223449" src="https://github.com/user-attachments/assets/a7bae01f-cad9-4a9d-a48e-ba1670dfabb8" />
<img width="1650" height="831" alt="Screenshot 2026-05-23 223504" src="https://github.com/user-attachments/assets/d4821d62-e1fa-4231-9f29-69571386b3e0" />
<img width="1659" height="850" alt="Screenshot 2026-05-23 223606" src="https://github.com/user-attachments/assets/d1338271-6384-4fc4-8f98-d83f50ccfae0" />
<img width="1655" height="598" alt="Screenshot 2026-05-23 223622" src="https://github.com/user-attachments/assets/910363fc-0a7b-4b64-86d9-a51df6590e5a" />
Penjelasan Output:
Program diawali dengan menampilkan judul “=== SISTEM ANTREAN KASIR ===”. Setelah itu, program menampilkan tujuh pilihan menu kepada pengguna, yaitu: 1. Tambah Nomor Antrean, 2. Hapus Nomor Antrean, 3. Tampilkan Antrean, 4. Tinggi Antrean, 5. Pelanggan Berikutnya, 6. Pelanggan Sebelumnya, dan 7. Keluar. Kemudian, pengguna memilih menu 1 beberapa kali untuk menambahkan nomor antrean ke dalam sistem. Pertama, pengguna memasukkan nomor antrean 5 dan program menampilkan pesan bahwa nomor antrean 5 berhasil dimasukkan. Proses yang sama dilakukan kembali untuk nomor antrean 10, 15, 8, 20, 25 dan 3. Kemudian, pengguna memilih menu 3 untuk menampilkan seluruh daftar antrean yang ada. Program menampilkan nomor antrean secara berurutan, yaitu 5, 3, 10, 8, 15,  20,  25. Setelah melihat daftar antrean, pengguna memilih menu 2 untuk menghapus nomor antrean yang telah selesai dilayani. Pengguna memasukkan nomor antrean 3 dan program memberikan pesan bahwa nomor antrean 3 berhasil dihapus dari daftar antrean. Lalu pengguna memilih menu 4 untuk melihat tinggi atau jumlah antrean yang masih tersisa. Program menampilkan informasi “Tinggi antrean: 4”. Selanjutnya, pengguna memilih menu 5 sebanyak dua kali untuk mencari pelanggan berikutnya. Pertama, pengguna memasukkan nomor 5 dan program menampilkan bahwa pelanggan berikutnya adalah nomor 8. Kemudian pengguna kembali mencari pelanggan berikutnya dari nomor 8 dan program menampilkan nomor 10 sebagai pelanggan selanjutnya. Terakhir, pengguna memilih menu 7 untuk keluar dari program. Program kemudian menampilkan pesan “Program selesai.”
E. Link Youtube

