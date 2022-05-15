from hesap import Hesap

class VadesizHesap(Hesap):
    
    def __init__(self, ad, soyad, id, bakiye, islem_ucreti):
        super().__init__(ad, soyad, id, bakiye)
        self._islem_ucreti = islem_ucreti

    def para_cek(self):
        super().para_cek()
        print(f"Para cekme ucreti {self._islem_ucreti}dir")

    def para_yatir(self):
        super().para_yatir()
        print("vadesiz hesabiniza para yatirilmistir")