from hesap import Hesap
from vadeliHesap import VadeliHesap
from vadesizHesap import VadesizHesap

x = VadesizHesap("betty", "bayram", 1, 100, 10).para_cek()
print(x)
y = VadeliHesap("betty", "bayram", 1, 100, 10).faiz_hesapla()

print(y)
z = Hesap("betty", "bayram", 1, 100).para_yatir()
print(z)

