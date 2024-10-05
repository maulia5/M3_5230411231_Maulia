class Menu:
    def __init__(self):
        self.Makanan = []
        self.Minuman = []

    def tambahmakanan(self, Makanan, Harga):
        self.Makanan[Makanan] = Harga
        print(f"Makanan {Makanan} berhasil ditambahkan dengan harga {Harga} ")

    def tambahminuman(self, Minuman, Harga):
        self.Makanan[Minuman] = Harga
        print(f"Minuman {Minuman} berhasil ditambahkan dengan harga {Harga} ")
    
    def tampilkanmenumakan(self):
        print("="*10 +"Makanan"+ "="*10)
        print("Nasi Goreng -> Rp. 10.000")
        print("Mie Ayam    -> Rp. 15.000")
        print("Rendang     -> Rp. 13.000")
        print("Bakso       -> Rp. 15.000")
        print("Kapurung    -> Rp. 14.000")
        for m in self.Makanan:
            print(f'- {m}')

    def tampilkanmenuminuman(self):
        print("="*10 +"Minuman"+ "="*10)
        print("Es Jeruk    -> Rp. 5.000")
        print("Es Teh      -> Rp. 3.000")
        print("Air Mineral -> Rp. 4.000")
        print("Es Lemon    -> Rp. 5.000")
        print("Es Kelapa   -> Rp. 6.000")
        for m in self.Minuman:
            print(f'- {m}')


def tampilanmenu():
    while True:
        print("="*10 +"Menu"+ "="*10)
        print("1. Daftar Menu Makanan")
        print("2. Daftar Menu Minuman")
        print("3. Tambah Menu")
        print("4. Keluar")
        pilih  = input("Masukkan pilihan 1/2/3/4:")

        if pilih == '1':
            menu.tampilkanmenumakan()

        if pilih == '2':
            menu.tampilkanmenuminuman()

        if pilih == '3':
            while True:
                print("1. Tambah Makanan")
                print("2. Tambah Minuman")
                pilih = input("Masukkan pilihan 1/2:")

                if pilih == '1':
                    Makanan = input("Masukkan nama makanan: ")
                    Harga = input("Masukkan harga makanan (tanpa Rp): ")
                try:
                    Harga = int(Harga)
                    menu.tambahmakanan(Makanan, Harga)
                except ValueError:
                    print("Harga harus berupa angka.")

                if pilih == '2':
                    Minuman = input("Masukkan nama minuman: ")
                    Harga = input("Masukkan harga minuman (tanpa Rp): ")
                try:
                    Harga = int(Harga)
                    menu.tambahminuman(Minuman, Harga)
                except ValueError:
                    print("Harga harus berupa angka.")

        if pilih == '4':
           print("Terimakasi telah memakai program ini")

        else:
            print("\n")        

menu = Menu()
tampilanmenu()

