class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\nIsi Hash Table (Separate Chaining):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key},{current.value}) -> ", end="")
                current = current.next
            print("NULL")


def main():
    mahasiswa = HashMapSeparateChaining()
    mahasiswa.insert(2217051001, "Andi")
    mahasiswa.insert(2217051011, "Budi")
    mahasiswa.insert(2217051021, "Citra")
    mahasiswa.insert(2217051002, "Dina")

    mahasiswa.display()

    hasil = mahasiswa.search(2217051011)
    if hasil is not None:
        print(f"\nMahasiswa Ditemukan = {hasil.value}")
    else:
        print("\nMahasiswa tidak ditemukan")

    mahasiswa.remove_key(2217051011)
    print("\nSetelah data budi dihapus:")
    mahasiswa.display()


if __name__ == "__main__":
    main()
