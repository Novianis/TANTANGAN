class Orang:
    def __init__(self):
        self.nama_depan='Shytai'
        self.nama_belakang='ydh'

orang1 = Orang()
print(f'instance object: (person1)')
print(f'type: (type(person1))')

orang1 = Orang()
orang2 = Orang()
orang3 = Orang()

class Teman:
    def __init__(self):
        self.nama='Asep'
        
namateman = Teman()
print(namateman.nama)
