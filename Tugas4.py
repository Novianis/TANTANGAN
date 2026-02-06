import json

nama = input("Nama: ")
email = input("Email: ")
kelas1 = input("Kelas 1: ")
kelas2 = input("Kelas 2: ")

data = {
    "siswa1": {"nama": nama, "email": email},
    "kelas": [kelas1, kelas2]
}

json.dump(data, open("Tugas4.json", "w"), indent=4)
print("Data4 disimpan.")

# Dict dan list dalam dict