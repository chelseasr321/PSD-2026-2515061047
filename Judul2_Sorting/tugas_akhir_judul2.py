def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def exchange_sort(arr, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                tukar(arr, i, j)

print("Program Pengurutan Daftar Mata Kuliah Mahasiswa Teknik Informatika")

def main():
    try:
        n = int(input("Masukkan Jumlah Mata Kuliah: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan Nama Mata Kuliah:")
    for i in range(n):
        while True:
            try:
                a = str(input(f"Mata Kuliah ke-{i+1}: "))
                arr.append(a)
                break
            except ValueError:
                print("Input tidak valid, silahkan masukkan ulang!")
    print(f"Daftar Mata Kuliah sebelum diurutkan: {arr}")
    exchange_sort(arr, n)
    print("Daftar setelah diurutkan :", end=" ")
    for i in range(n):
        if i < n - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    main()
