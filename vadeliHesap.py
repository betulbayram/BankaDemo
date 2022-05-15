from hesap import Hesap
from decimal import Decimal

class VadeliHesap(Hesap):
    def __init__(self, ad, soyad, id, bakiye=100, faiz_orani=0.1):
        super().__init__(ad, soyad, id, bakiye)
        self._faiz_orani = faiz_orani

    @property#getter setter
    def faiz_orani(self):
        return self._faiz_orani

    @faiz_orani.setter
    def faiz_orani(self, f):

        if 0 < f < 1:
            self._faiz_orani = f
        else:
            raise ValueError("girdiginiz oran 0 ile 1 arasinda olmalidir")


    def faiz_hesapla(self):
        return Decimal(self._bakiye * self._faiz_orani)