# Soal 1: Class BankAccount
class BankAccount:
    def __init__(self, account_name, balance, pin):
        self.account_name = account_name  # public attribute
        self._balance = balance           # protected attribute
        self.__pin = pin                  # private attribute

    def get_balance(self):
        return self._balance

    def set_pin(self, new_pin):
        self.__pin = new_pin

# Implementasi class BankAccount
bank_account = BankAccount("Shinata Putra", 1000000, 1234)

# Demonstrasi akses terhadap atribut
print(f"Nama Pemilik Rekening: {bank_account.account_name}")  # public
print(f"Saldo Rekening: {bank_account.get_balance()}")        # protected melalui method

# Mengubah PIN (private)
bank_account.set_pin(5678)
print("PIN berhasil diubah.")

# Soal 2: Class Library
class Library:
    def __init__(self, book_name, author, price):
        self.book_name = book_name        # public attribute
        self._author = author            # protected attribute
        self.__price = price             # private attribute

    def get_price(self):
        return self.__price

    def update_price(self, new_price):
        self.__price = new_price

# Implementasi class Library
library = Library("Pemrograman Python", "Guido van Rossum", 150000)

# Demonstrasi membaca atribut
print(f"Nama Buku: {library.book_name}")       # public
print(f"Nama Pengarang: {library._author}")     # protected
print(f"Harga Buku: {library.get_price()}")    # private melalui method

# Mengubah harga buku
library.update_price(200000)
print(f"Harga Buku Setelah Diubah: {library.get_price()}")

# Penjelasan akses langsung terhadap atribut private (__price)
# Jika mencoba mengakses library.__price langsung, akan terjadi error seperti berikut:
# AttributeError: 'Library' object has no attribute '__price'
