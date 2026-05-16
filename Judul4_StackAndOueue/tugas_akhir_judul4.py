class StackArray:
    def __init__(self, max_size=5):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Halaman gagal ditambahkan")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Halaman {x} berhasil dibuka")

    def pop(self):
        if self.is_empty():
            print("Tidak ada riwayat pencarian")
            return
        print(f"Halaman {self.st[self.top_idx]} berhasil dihapus")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Tidak ada riwayat pencarian")
            return
        print(f"Halaman teratas adalah: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Tidak ada riwayat pencarian")
            return
        print("Riwayat Pencarian: ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=", " if i != 0 else "")

        print()


def main():
    stack = StackArray()
    pilih = 0
    while pilih != 5:
        print("\nImplementasi Stack Array pada Riwayat Browser")
        print("1. Masuk ke halaman")
        print("2. Hapus halaman")
        print("3. Tampilkan halaman pertama")
        print("4. Tampilkan halaman")
        print("5. Keluar dari browser")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                val = str(input("Buka Halaman: "))
                stack.push(val)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            print("Riwayat pencarian ditutup.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
