print("PROGRAM MENCARI NAMA SISWA PADA DAFTAR ABSENSI")

def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = ["Adelia", "Davina", "Naila", "Arcel", "Atthariqia", "Chelsea", "Alin", "Oliv", "Riva", "Dzakya"]
    n = len(data)
    print(f"Daftar Siswa: {data}")
    while True:
        try:
            target = str(input("Masukkan Nama Siswa yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan Nama Siswa!")
    counter = sequential_search(data, n, target)
    if counter > 0:
        print(f"Siswa bernama {target} ditemukan sebanyak {counter} kali.")
    else:
        print(f"Siswa bernama {target} tidak ditemukan.")

if __name__ == "__main__":
    main()

while True:
        ulang = input("Ingin Mencari Nama Lain? (iya/tidak): ")

        if ulang == "iya":
            main()

        else:
            print("Program selesai.")
            break
