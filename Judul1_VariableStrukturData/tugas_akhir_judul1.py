def menu():
    print("PROGRAM PENGOLAHAN DATA NILAI MAHASISWA TEKNIK INFORMATIKA")
    print("MENU")
    print("1. Input data mahasiswa")
    print("2. Lihat address data nilai")
    print("3. Lihat address tiap nilai mata kuliah")
    print("4. Input nilai mahasiswa")
    print("5. Tampilkan semua nilai")
    print("6. Cek nilai mata kuliah tertentu")
    print("7. Keluar")

def main():
    a = [0] * 10
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan MENU: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        
        if choice == 1:
            nama = input("Masukkan nama mahasiswa: ")
            npm = input("Masukkan NPM: ")

        elif choice == 2:
             print(f"address data nilai di sistem: {id(a)}")

        elif choice == 3:
            for i in range(10):
                print(f"address masing masing nilai mata kuliah[{i}]: {id(a[i])}")

        elif choice == 4:
            print("Masukkan 10 nilai mata kuliah:")
            for i in range(10):
                while True:
                    try:
                        a[i] = int(input(f"a[{i}] = "))
                        break
                    except ValueError:
                        print("Input tidak valid, silakan masukkan nilai!")

        elif choice == 5:
            print("HASIL NILAI MAHASISWA")
            print(f"Nama: {nama}")
            print(f"NPM: {npm}")
            print("DAFTAR NILAI:", a)
            print(f"Nilai tertinggi: {max(a)}")
            print(f"Nilai terendah: {min(a)}")
            print(f"Rata-rata: {sum(a)/len(a)}")

        elif choice == 6:
            index: int = int(input("Ingin mengecek nilai mata kuliah ke berapa? "))
            try:
                print (f"Nilai mata kuliah tersebut: {a[index]}")
            except ValueError:
                print("input harus berupa angka")

        elif choice == 7:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
