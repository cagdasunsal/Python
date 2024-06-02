## İkinci El Araç Yönetim Sistemi

Bu Python programı, ikinci el araçlar için bir yönetim sistemi sağlar. Kullanıcılar, araçları ekleyebilir, silebilir, belirli kriterlere göre arama yapabilir ve tüm mevcut araçları listeleyebilir.

### Gereksinimler

- Python 3.x

### Kurulum

1. Bu repository'i klonlayın veya kodu indirin.
2. Python'un sisteminizde kurulu olduğundan emin olun.

### Kullanım

Programı çalıştırmak için terminalde aşağıdaki komutu çalıştırın:
```python
python 2.ElArac.py

Fonksiyonlar ve Açıklamaları
1. MevcutAraclar()
Bu fonksiyon, sistemde mevcut olan araçları listeye ekler. Araçlar, markası, modeli, yılı, fiyatı ve özellikleri ile birlikte eklenir.

python
Kodu kopyala
def MevcutAraclar():
    Araclar = []
    Araclar.append(["Volkswagen", "Passat", "2014", "1200000",
                    """...""" ])
    ...
    for i in Araclar:
        aracBilgisi = {
            "Marka": i[0],
            "Model": i[1],
            "Yıl": i[2],
            "Fiyatı": i[3],
            "Özellikler": i[4]
        }
        ilanListe.append(aracBilgisi)
2. AracEkle()
Kullanıcıdan araç bilgilerini alarak yeni bir araç ekler.

python
Kodu kopyala
def AracEkle():
    ...
    ilanListe.append({
        "Marka": marka0,
        "Model": modeli0,
        "Yıl": yili0,
        "Fiyatı": fiyati0,
        "Özellikler": ozellikleri0
    })
3. AracSil()
Belirtilen araç kodunu kullanarak listeden bir aracı siler.

python
Kodu kopyala
def AracSil():
    ...
    del ilanListe[indeks]
4. MarkaAra()
Kullanıcıdan marka bilgisi alarak o markaya ait araçları listeler.

python
Kodu kopyala
def MarkaAra():
    ...
    for i in ilanListe:
        if ilanListe[i]["Marka"] == markasi0:
            print(ilanListe[i]["Model"], ilanListe[i]["Yıl"], ilanListe[i]["Fiyatı"], sep=" - ")
5. FiyatAra()
Kullanıcıdan fiyat aralığı bilgisi alarak belirtilen aralıkta araçları listeler.

python
Kodu kopyala
def FiyatAra():
    ...
    for i in ilanListe:
        if int(ilanListe[i]["Fiyatı"]) in range(int(fiyatMin0), int(fiyatMax0)):
            print(ilanListe[i]["Marka"], ilanListe[i]["Model"], ilanListe[i]["Yıl"], ilanListe[i]["Fiyatı"], sep=" - ")
6. Dokum()
Mevcut tüm araçları listeler.

python
Kodu kopyala
def Dokum():
    ...
    for i in ilanListe:
        print(i, ilanListe[i]["Marka"], ilanListe[i]["Model"], ilanListe[i]["Yıl"], ilanListe[i]["Fiyatı"], sep=" - ")
7. Menu()
Kullanıcıya işlem yapmak için bir menü sunar.

python
Kodu kopyala
def Menu():
    ...
    MenuSayac0 = input("Bir Menü Seçiniz:\t")
    ...
    if MenuSayac0 == "1":
        MarkaAra()
    elif MenuSayac0 == "2":
        FiyatAra()
    elif MenuSayac0 == "3":
        Dokum()
    elif MenuSayac0 == "8":
        AracSil()
    elif MenuSayac0 == "9":
        AracEkle()
    elif MenuSayac0 == "q":
        return
8. Calıstır()
Programı başlatır ve kullanıcıyı karşılar.

python
Kodu kopyala
def Calıstır():
    print("--------- Galerimize Hoş Geldiniz ---------")
    MevcutAraclar()
    Menu()
Örnek Kullanım
python
Kodu kopyala
# Programı başlatmak için
Calıstır()
Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
