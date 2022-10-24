# Homework 1 : Muhammad Atho'illah

# Parent Class
class Hewan():
    
    # Class Attribute
    nama_latin = 'Panthera Leo'
    
    # Instance Attribute
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    # Instance Method
    def bangun(self):
        print("Nama hewan ini adalah {} \nUmur hewan ini adalah {}".format(
            self.nama, 
            self.umur))
        return None
    
    # Class Method
    def change_nama_latin(self):
        return "Nama Latin diubah menjadi {}".format(self.nama_latin_ganti)
        

# Child Class
class Kucing(Hewan):

    # Nama latin dirubah menggunakan Class Method
    def change_nama_latin(self):
        return super().change_nama_latin()

    # Override method bangun
    def __init__(self, nama, umur, ras, asal, kecepatan, latin):
        super().__init__(nama, umur)
        self.ras                    = ras
        self.asal                   = asal
        self.nama_latin_ganti       = latin
        self.kecepatan              = kecepatan
    
    def bangun(self):
        super().bangun()
        print("Ras hewan ini adalah {} \nAsal hewan ini adalah {}".format(
            self.ras, 
            self.asal))
        return None

    # Method Lari
    def lari(self):
        if self.kecepatan > 10 :
            print('Dia Berlari Cepat Sekali')
        else:
            print('Dia Lambat')

# Instantiate Hewan (Parent Class)
print('\n--- Instantiate Parent Class ---')
Singa = Hewan('John', 21)
print(Singa.bangun())


# Instantiate Kucing (Child Class)
print('\n--- Instantiate Child Class ---')
Meng = Kucing('Asep', 21, 'Anggora', 'Ciamis', 12, 'Felis Catus')
print(Meng.bangun())
print(Meng.change_nama_latin())
print(Meng.lari())