class Hesap:
    def __init__(self, ad, soyad, id, bakiye=100):
        self._ad = ad
        self._soyad = soyad
        self._id = id
        self._bakiye = bakiye

    @property
    def ad(self):
        return self._ad

    @property
    def soyad(self):
        return self._soyad
    
    @property
    def id(self):
        return self._id

    @property
    def bakiye(self):
        return self._bakiye

    def para_yatir(self):
        print("Yatirmak istediğiniz miktari kapak altina yerlestiriniz")

    def para_cek(self):
        print("Cekmek istediginiz para tutarini $ türünden giriniz")
        
    