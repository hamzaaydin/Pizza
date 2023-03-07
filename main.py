import csv, os
from datetime import datetime

filename = 'Orders_Database.csv'
header = ['isim', 'tc_kimlik_no', 'kredi_karti_no', 'aciklama', 'siparis_zamani', 'kredi_karti_sifresi']

# Create file if it doesn't exist
if not os.path.exists(filename):
    with open(filename, 'w', newline='', encoding="utf-8")  as f:
        writer = csv.writer(f)
        writer.writerow(header)


class Pizza:
    def __init__(self, cost):
        self.cost = cost
    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description


class Klasik(Pizza):
    def __init__(self, cost):
        super().__init__(cost)
        self.description = "Klasik Pizza"
        self.cost = 10.99

class Margarita(Pizza):
    def __init__(self, cost):
        super().__init__(cost)
        self.description = "Margarita Pizza"
        self.cost = 11.99

class Turk(Pizza):
    def __init__(self, cost):
        super().__init__(cost)
        self.description = "Türk Pizza"
        self.cost = 12.99

class Sade(Pizza):
    def __init__(self, cost):
        super().__init__(cost)
        self.description = "Sade Pizza"
        self.cost = 13.99


class Zeytinli:
    def __init__(self, pizza):
        self.pizza = pizza
        self.price = 1.50
    def get_description(self):
        return self.pizza.get_description() + ", Ekstra Zeytinli"
    def get_cost(self):
        return self.pizza.get_cost() + self.price

class Mantarli:
    def __init__(self, pizza):
        self.pizza = pizza
        self.price = 2
    def get_description(self):
        return self.pizza.get_description() + ", Ekstra Mantarlı"
    def get_cost(self):
        return self.pizza.get_cost() + self.price

class KeciPeynirli:
    def __init__(self, pizza):
        self.pizza = pizza
        self.price = 2.50
    def get_description(self):
        return self.pizza.get_description() + ", Ekstra Keçi Peynirli"
    def get_cost(self):
        return self.pizza.get_cost() + self.price

class Etli:
    def __init__(self, pizza):
        self.pizza = pizza
        self.price = 3
    def get_description(self):
        return self.pizza.get_description() + ", Ekstra Etli"
    def get_cost(self):
        return self.pizza.get_cost() + self.price

class Soganli:
    def __init__(self, pizza):
        self.pizza = pizza
        self.price = 3.50
    def get_description(self):
        return self.pizza.get_description() + ", Ekstra Soğanlı"
    def get_cost(self):
        return self.pizza.get_cost() + self.price

class Misirli:
    def __init__(self, pizza):
        self.pizza = pizza
        self.price = 4
    def get_description(self):
        return self.pizza.get_description() + ", Ekstra Mısırlı"
    def get_cost(self):
        return self.pizza.get_cost() + self.price

taban_dict = {1: Klasik(Pizza),
              2: Margarita(Pizza),
              3: Turk(Pizza),
              4: Sade(Pizza)}
sos_dict = {11: Zeytinli,
            12: Misirli,
            13: KeciPeynirli,
            14: Etli,
            15: Soganli,
            16: Misirli}

#pizza = Klasik(3)
#zeytinli_klasikpizza = Zeytinli(pizza)
def main():
    with open("Menu.txt", encoding="utf-8") as file:
        print(file.read())
        print("-"*50)
    taban_id = int(input("Pizza Tabanı Seçiniz: "))
    if taban_id in taban_dict:
        taban = taban_dict[taban_id]
        sos_id = int(input("Sos seçiniz: "))
        if sos_id in sos_dict:
            soslu_pizza = sos_dict[sos_id](taban)
            print(f"Seçilen kombinasyon ---> {soslu_pizza.get_description()}")
            print(f"Toplam fiyat: {soslu_pizza.get_cost()}")
            isim = input("isim: ")
            tc_kimlik_no = input("TC Kimlik No: ")
            kredi_karti_no = input("Kredi Kart No:")
            aciklama = input("Açıklama: ")
            siparis_zamani = str(datetime.now())
            kredi_karti_sifresi = input("Kredi Kartı Şifresi: ")

            with open(filename, 'a', newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                list_to_write = [isim, tc_kimlik_no, kredi_karti_no, aciklama, siparis_zamani, kredi_karti_sifresi]
                writer.writerow(list_to_write)
            print("Kullanıcı bilgileri başarıyla kaydedildi")
        else:
            print("Tanımsız sos seçildi. Program sonlandırıldı")

    else:
        print("Tanımsız pizza tabanı seçildi. Program sonlandırıldı")

main()



