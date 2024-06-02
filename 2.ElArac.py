#!/usr/bin/env python
# coding: utf-8

# In[ ]:



Araclar = []
ilanListe = {}


def MevcutAraclar():
    global Araclar, ilanListe, Markalar
    Araclar.append(["BMW", "3.20", "2015", "1450000",
                    "Heap up cama yansıtma \nCam tavan \n4 kapı vakum \nSunroof \n4 koltuk ısıtma \nM4 COMPETİTİON ELEKTİRİKLİ HAFIZALI adaptif koltuklar \nM4 COMPETİTİON JANT LASTİKLER önler 255/30/20\nArkalar 295/30/20\nM4 firen kaliperi ve diskleri \nElektirikli vakumlu arka bagaj \nGeri görüş kamerası \nPusulalı HAFIZALI ayna \nF1 ve smg m4 vites \nM4 gts bady KİT \nEmniyet Kemeri gerdirme\nHasar kaydı yoktur"])
    Araclar.append(["BMW", "3.20", "2015", "1254500",
                    "CAM TAVAN\n8 İLERİ TİPTRONİC VİTES\nŞERİT TAKİP\n8 AIRBAG\nABS-BAS\nDSC\nHAYALET GÖSTERGE\nELEKTRİKLİ BAGAJ\nDİJİTAL KLİMA\nÇOK FONKSİYONLU DERİ DİREKSİYON\nMP3-CD-RADYO\nBLUETOOTH TELEFON\nUSB-AUX GİRİŞİ\nÖN-ARKA ARA KOL DAYAMA\nANAHTARSIZ ÇALIŞTIRMA\nFAR SENSÖRÜ\nYAĞMUR SENSÖRÜ\nLASTİK BASINÇ SENSÖRÜ\nPARK MESAFE SENSÖRÜ\nGERİ GÖRÜŞ KAMERASI\nLEDLİ ÖN FARLAR\nELEKTRİKLİ KATLANIR AYNA\nSİS FARI\nYOL BİLGİSAYARI\nÇİZİKTEN KAYNAKLI 2 PARÇA LOKAL BOYA VARDIR\nEKSPERTİZ YAPILMIŞ\nTRAMERSİZ"])
    Araclar.append(["BMW", "3.20", "2016", "1380000", """2016 MODEL BMW 320D EDİTİON M SPORT İÇİ DIŞI ORJİNAL M SPORT\nARACIM HATASIZ BOYASIZDIR YEDEK ANAHTARI KİTAPÇIKLARI DURUYOR\n9500 TL SOL FAR DEĞİŞİMİNDEN TRAMER MEVCUTTUR\nTÜM BAKIMLARI YETKİLİ SERVİSTE YAPILMIŞTIR\nÖZEL PLAKA 777\nSİSLERDE BEYAZ LED\nKATLANIR AYNA\nACİL S.O.S BUTONU\nSİYAH TAVAN
    \nGERİ GÖRÜŞ KAMERASI\nÖN ARKA PARK SENSÖRÜ\nM DERİ DİREKSİYON\nHIZ SABİTLEYİCİ VE LİMİTLEYİCİ\nABS-ASR-DSC\nLED FAR\nLED STOP\nÇİFT BÖLGE DİJİTAL KLİMA\nBLUETOOTH – USB – AUX\nFOLLOW ME\nFAR VE YAĞMUR SENSÖRÜ\nYOL BİLGİSAYARI\nRECARO KOLTUK\nSUNROOF\nAKRAPOVİÇ EGZOZ VE UYUMLU DİFİZÖR\n4 FARKLI SÜRÜŞ MODU\nYOKUŞ KALKIŞ DESTEĞİ\nAMBİANS AYDINLATMA\nAUTO HOLD\nLED GÜNDÜZ FARLARI\nKARARTMALI DİKİZ AYNASI\nDETAYLI BİLGİ İÇİN ARAYINIZ"""])
    Araclar.append(["BMW", "3.20", "2016", "1289900",
                    """ARACIMIZ 2016 MODEL BMW 3.20 D XDRİVE\n(53) BİNDE ORJİNAL TECHNO PLUS PAKET \n2.0 DİZEL OTOMATİK 8 İLERİ 190 PS SİYAH İÇİ BEJ RENK.\nNOT: ARACIMIZA İÇ DIŞ SERAMİK KAPLAMA +\nKUAFÖR + PASTA CİLA UYGULANMIŞTIR.\nARACIMIZDA SADECE 1 PARÇA LOKAL BOYA VARDIR.\n(SAĞ ÖN ÇAMURLUK)\nHARİCİ KESİNLİKLE HATASIZDIR ORJİNALDİR.\nNOT: ARACIMIZDA SÖYLENİLEN DIŞINDA BİRŞEY ÇIKARSA EXPERTİZ ÜCRETİ\nVE TÜM MASRAFLARINIZ FİRMAMIZ TARAFINDAN KARŞILANMAKTADIR..\n- 4 ADET SÜRÜŞ MODLARI\n(SPORT SPORT+ COMFORT + ECO MOD)\n- SUNROOF (AÇILIR)\n- DİGİTAL KLİMA (ÇİFT BÖLGE)\n- ABS - ASR - ASC - ESP​\n- BEJ DERİ KOLTUKLAR - BI XENON FAR\n- FAR YIKAMA - LED FARLAR - XENON SİSLER\n- AHŞAP İÇ DEKOR - HIZ SABİTLEME​\n- MULTİ FONK DERİ DİREKSİYON​\n- BOARD COMPUTER (YOL BİLGİSAYARI)\n- RENKLİ CAMLAR - 18 İNÇ ÇELİK JANT\n- GERİ GÖRÜŞ KAMERASI - PARK MESAFE\n- KATLANIR & ISITMALI YAN AYNALAR\n- OTOMATİK FAR SENSÖRÜ - YAĞMUR SENSÖRÜ\n- BLUETOOTH - CD - MP3 - USB - AUX ÇALAR\n- MUAYENE BİTİŞ TARİHİ: 10 / 04 / 2023"""])
    Araclar.append(["BMW", "5.20", "2015", "1675000",
                    "ARACIMIZDA DEĞİŞEN YOK 2 PARÇA LOKAL BOYA VARDIR\nARACIMIZ BAKIMLARI YENI YAPILMIŞTIR\nMODELİNİN EN DOLUSUDUR \nARACIMIZIN DÖRT LASTIK CANTI SIFIRDIR \nÇALIŞMAYAN AKŞAMI YOKTUR MOTORU SANZIMANI HERSEYIYLE MAYERIDIR \nISTENILEN EXPERE USTAYA AÇIKTIR \nTREMER => 11.000 \nDEĞİŞEN => YOK \nBOYA => ıkı parça lokal \nARACIMIZ BMW 5,20D M SPOT \nARACIMIZDA VAKUMLU KAPILAR.ELEKTRİKLİ BAGAJ.NBT EKRAN.HAYALET GÖSTERGE.\nİÇ DIŞ M SPORT.ELEKTRİKLİ HAFIZALI ISITMALI KOLTUK.KATLANIR AYNA.\nVS.VS ÖZELLİKLER"])
    Araclar.append(["BMW", "5.20", "2015", "1470500",
                    """2015 MODEL BMW 5.20D PREMİUM PAKET \nARACIMIZDA DEĞİŞEN BOYA YOKTUR \nBORUSAN BAYİİ ÇIKIŞLI \nARACIMIZ TAMAMEN BORUSAN SERVİS BAKIMLIDIR \nHAYALET EKRAN \nVAKUM KAPILAR \nBEJ DERİ DÖŞEME \nDÖŞEMELERİNDE YANIK YIRTIK DEFORMA YOKTUR\n3 FARKLI SÜRÜŞ MODU \nSUNROOF \nDİJİTAL KLİMA \nISITMALI KOLTUKLAR \nELEKTRİKLİ AYNA \nGÜNDÜZ LEDLİ\nELEKTRİKLİ HAFIZALI SÜRÜCÜ KOLTUĞU\nELEKTRİKLİ YOLCU KOLTUĞU\nSTART&STOP\nGERİ GÖRÜŞ KAMERA \nYOKUŞ KALKIŞ DESTEĞİ\n4 LASTİĞİ YENİDİR \nVS VS…."""])
    Araclar.append(["BMW", "5.20", "2016", "1570000",
                    """HAYALET GÖSTERGE\nBÜYÜK EKRAN\nNAVİGASYON\nBEJ DERİ DÖŞEME\nGERİ GÖRÜŞ KAMERASI\nKÖR NOKTA UYARI SİSTEMİ\nŞERİT TAKİP SİSTEMİ\nÇARPIŞMA ÖNLEYİCİ\n3 FARKLI SÜRÜŞ MODU\nGÜNEŞ KORUMALI ARKA CAMLAR\nDİJİTAL GÖSTERGE\nFONKSİYONEL DERİ DİREKSİYON\nELEKTROKROM KATLANIR AYNALAR\nLED SİS FARLARI\nPARK ASİSTAN \nBMW ACİL DURUM ÇAĞRISI\nOTOMATİK KLİMA\nCD ÇALAR\nELEKTRİKLİ CAM TAVAN\nVELUR HALI PASPASLAR\nBLUETOOH\nUSB-MP3\nHIZ SABİTLEME\nYOKUŞ KALKIŞ DESTEĞİ\nYAĞMUR SENSÖRÜ\nFAR SENSÖRÜ\nÖN VE ARKA PARK SENSÖRÜ"""])
    Araclar.append(["BMW", "5.20", "2016", "1500000",
                    """Aracımızın tüm bakımları zamanında yapılmıştır.\nAracımız Borusan çıkışıdır.\nHatasız boyasızdır. \nEkspertiz resimlerde mevcuttur.\nTramer kaydı 12.300₺’dir parça parça halinde.\nAracımızın özellikleri aşağıda işaretlenmiştir.\nNOT:Araç Kahramanmaraş’tadır."""])

    Araclar.append(["Audi", "A3", "2015", "960000",
                    """Aracımda tramer boya yoktur \nhatasızdır \nkoltuk ısıtması vardır \nbalata disk filtre bakımları 1 ay önce yapılmıştır \naracın motorunda soft 1 yazılım vardır \n200hp arka ön tampon ve stop farlar s3 modifiyelidir \nyanında varex egzozuda veriyorum \ntek kusuru yolda ufak çakıl taşlarının sekmesinden dolayı çok gözükmeyecek şekilde ön camda ufak bir çatlak vardır \nharici hiçbir sorunu yoktur yeni sahibine şimdiden hayırlı olsun"""])
    Araclar.append(["Audi", "A3", "2015", "935000",
                    """ Aracımda tramer boya yoktur \nhatasızdır \nkoltuk ısıtması vardır \nbalata disk filtre bakımları 1 ay önce yapılmıştır \naracın motorunda soft 1 yazılım vardır \n200hp arka ön tampon ve stop farlar s3 modifiyelidir \nyanında varex egzozuda veriyorum \ntek kusuru yolda ufak çakıl taşlarının sekmesinden dolayı çok gözükmeyecek şekilde ön camda ufak bir çatlak vardır \nharici hiçbir sorunu yoktur yeni sahibine şimdiden hayırlı olsun"""])
    Araclar.append(["Audi", "A3", "2016", "995900",
                    """AUDI A3 CABRIO \n1.4 TFSI SPORT LINE S-TRONIC\n2016 MODEL\nDEĞİŞEN BOYA TRAMER KAYDI YOKTUR\nGERİ GÖRÜŞ KAMERASI\nISITMALI ÖN KOLTUKLAR\nKOLTUK BAŞI ENSE ISITMA\nANAHTARSIZ GİRİŞ VE ÇALIŞTIRMA\nFONKSİYONEL DERİ DİREKSİYON\nYARI DERİ, KUMAŞ KOLTUKLAR\nLED GÜNDÜZ FARLARI\nLED ARKA STOPLAR\nXENON PLUS FARLAR\nFAR YIKAMA\n19" ALAŞIMLI SPOR ÇELİK JANTLAR\nELEKTRİKLİ, ISITMALI, KATLANIR YAN AYNALAR\nOTOMATİK FAR YAĞMUR SENSÖRÜ\nKİLİTLENEBİLİR TORPİDO GÖZÜ\nÇİFT BÖLGE DİGİTAL KLİMA \nÖN, ARKA PARK SENSÖRÜ"""])
    Araclar.append(["Audi", "A3", "2016", "965000",
                    """Sahibinden kapalı garaj aracı. \n* Yeni nesil 1.4 TFSi Ultra 150 Hp Cabrio\n* Ense Üfleme (Air Scarf)\n* Drive Select\n* 3 Kol Sline Direksiyon\n* Ön Koltuklarda Isıtma\n* Arka Park Sensörü\n* Elektrikli Katlanır Aynalar\n* ABS+ASR+EBD+ESP\n* Led Matrix Far\n* Isıtmalı Aynalar\n* Soğutmalı Torpido\n* Çift Yönlü Dijital Klima\n* Elektrikli Park Freni\n* Auto Hold\n* Follow Me\n*Far sensörü\n*Yağmur sensörü"""])
    Araclar.append(["Audi", "A4", "2015", "1350000",
                    """A4 all road quattro 2.0 225 hp\nHatasız ve Full Yekili Servis Bakımlı\nAraçta ekstra olarak serviste hız sabitleme sistemi takılmıştır.\nYazlık ve kışlık lastikleri mevcut.\nAraç boya değişen yoktur\nLütfen Takas için aramayın…"""])
    Araclar.append(["Audi", "A4", "2015", "1325000",
                    """Hatasız. \n95.750 km \nKış lastikleri mevcut. \nHayalet ekran\nKahverengi deri koltuklar.\nMuayenesi yeni yapılmış.\nBakımları yeni yapılmış.\nMasrafsız!!!\nFatura kesilecektir.\nSADECE NAKİT SATILIKTIR!!!"""])
    Araclar.append(["Audi", "A4", "2016", "1545000",
                    """DIŞ RENK\nSİYAH\nİÇ RENK\nDERİ \nÖZELLİKLER\nBAYİ ÇIKIŞLI\nYETKİLİ SERVİS BAKIMLI\n2017 TRAFİĞE ÇIKIŞLI\nCAM TAVAN - SUNROOF\nF - 1 VİTES\nHAYALET EKRAN\nGENİŞ MENÜ EKRANI\nNAVİGASYON\nGERİ GÖRÜŞ KAMERASI\nELEKTİRİKLİ BAGAJ\nÖN - ARKA PARK SENSÖRÜ\nSTART - STOP\nHAFIZALI - ELEKTRİKLİ - ISITMALI - BEL DESTEKLİ ÖN KOLTUKLAR\nSÜRÜŞ MODLARI\nDİJİTAL GÖSTERGELİ KLİMA\nXENON FAR SİSTEMİ\nLED STOP LAMBALARI\nÖN - ARKA GÜNDÜZ LEDLERİ\nÖN - ARKA KOL DAYAMA\nBLUETOOTH - USB - TELEFON - AUX\nEXPERTİZ\nBOYA - DEĞİŞEN YOK\nTRAMER\nYOK"""])
    Araclar.append(["Audi", "A4", "2016", "1520000",
                    """SUNROOF\nRECORE KOLTUKLAR\nKOLTUK ISITMA\nKABLOSUZ TELEFON ŞARJI\nBÜYÜK AUDI MMI EKRAN\nHAYALET EKRAN GÖSTERGE\nKAYARLI SİNYAL LAMBALARI\nSTART STOP \nİÇ AMBİYANS AYDINLATMA\nELEKTRİKLİ DERİ KOLTUKLAR\nF1 VİTES\nÇOK FONKSİYONLU DERİ DİREKSİYON\nHIZ LİMİTÖRÜ\nCRUISE KONTROL\nSÜRÜŞ MOD SEÇİMİ\nÖN ARKA PARK SENSÖRÜ\nFAR SENSÖRÜ\nYAĞMUR SENSÖRÜ\nBLUETOOTH \nUSB"""])

    Araclar.append(["Seat", "Leon", "2015", "1450000",
                    """Araç BeMaps referanslıdır\n-Her 5bin km'de yağ bakımı yapılmıştır motul x-clean 5w30\n-Dsg ıslak tip olup bakım kapsamında 50bin km'de yağı yenilendi\n-Kronik olan devir daim ve termostat Seat Bursa yetkili servisinde yeni versiyon ile değişmiştir\n-Haziran ayında ön fren disk ve balataları 380mm Brembo olarak yurt dışından temin edilip yenilendi\n-Son yağ bakımı 66.000de yapıldı\n-Kasım ayında kavrama ve volan doğuştan alınarak değiştirildi\n-Muayene 2024 Mayıs"""])
    Araclar.append(["Seat", "Leon", "2015", "675000",
                    """2015 MODEL SEAT LEON 1.6TDI \nSTYLE OTOMATİK\nHATASIZ BOYASIZ \nTRAMERSİZ\nCAM TAVAN \nALCANTARA KOLTUK\nLED + XENON FAR\nBÜYÜK  EKRAN \nBLUETOOT MEDIA PLAYER\nKATLANIR AYNA\nDİJİTAL KLİMA\n17'' ÇELİK FR JANT \nELEKTRİKLİ KATLANIR YAN AYNALAR\nDÖNÜŞE DUYARLI SİS FARI\nÖN ARKA KOL DAYAMA\nİSOFİKS\nÖN ARKA PARK SENSÖRÜ\nYOKUŞ KALKIŞ DESTEĞİ\nOTOMATİK KARARAN İÇ DİKİZ AYNASI \nHIZ SABİTLEME\nYOL BİLGİSAYARI"""])
    Araclar.append(["Seat", "Leon", "2016", "1275000",
                    """2016 MODEL SEAT LEON CUPRA 290HP \nACC + KOLTUK ISITMA + SPOR KOLTUK + DCC\nSOL ÖN ÇAMURLUK VE SOL ÖN KAPI DEĞİŞMİŞTİR\nHARİCİ HATASIZ BOYASIZDIR\nARAÇ SİGORTA ŞİŞİRMESİNDEN DOLAYI AĞIR HASAR KAYITLIDIR"""])
    Araclar.append(["Seat", "Leon", "2016", "795000",
                    """ARACIN 2. SAHİBİYİM.\n-ARACI YAKLAŞIK 2,5 YILDIR KULLANMAKTAYIM.\n-ARACIM YETKİLİ SERVİS BAKIMLIDIR VE SÜREKLİ KAPALI GARAJDA DURMAKTADIR.\n-06/07/2016 YILINA AİT KTT-ÇARPMASI BULUNMAKTADIR VE BEDELSİZDİR.\n-ARACIMDA HATA,BOYA VE DEĞİŞEN KESİNLİKLE BULUNMAMAKTADIR.\n-ARACIMIN STANDART ÖZELLİKLERİ AŞAĞIDA DOĞRU ŞEKİLDE İŞARETLENMİŞTİR.\n-ARACIMDA STANDART FR MODELLERE GÖRE ÖZEL SİPARİŞ VERİLEREK ALINAN BİRKAÇ ÖZELLİKLER\n-18” JANTLAR\n-ORTA KISMI ALCANTARA OLAN KOLTUKLAR\n-MAT SİYAH TAVAN RAYLARI\n-SEAT SOUND MÜZİK SİSTEMİ (STEPNEDE SUBWOOFER)\n-ARACIMIN SERVİSTEKİ İYİ NİYET GARANTİSİ DEVAM ETMEKTEDİR.\n-ARACIMIN 16/11/2022 TARİHİNDE 90.000 KM BAKIMI YİNE YETKİLİ SERVİSTE YAPILMIŞTIR."""])
    Araclar.append(["Seat", "İbiza", "2015", "620000",
                    """TR DEKİ GERÇEK EN TEMİZ (SC) BİRİ\nKAZA YOK\nBOYA YOK\nDEĞİŞEN YOK\nHASAR KAYDI YOK\nEZİK ÇİZİK YOK\nORJİNAL 53.000 KM DE\nFULL SERVİS(DOĞUŞ OTO) BAKIMLI OLUP BAKIMLARI YAPILMIŞTIR\nLASTİKLER YENİ OLUP MİCHELİN PILOT SPORT 4 SERİSİDİR\nMUAYENE YENİ OLUP MTV Sİ ÖDENMİŞTİR\nEXTRALAR:\nÖZEL PLAKA\nSPARCO ORJINAL ANTEN\nORJINAL BODY KİT\nCUPRA DETAYLAR\nSON SUSTURUCU İPTALİ\nPİANO BLACK İÇ DETAYLAR\nEİBACH PRO YAYLAR\nRSA STAGE 1 YAZILIM\nFORGE SESLİ DUMP VALVE\nORJINAL İBİZA ZENEC MULTİMEDİA\n3M CAM FİLMİ\nXPEL PPF KAPUT, FAR VE KAPI İÇLERİ KAPLAMA\nDR DETAİLİNG İÇ VE DIŞ TEMİZLİK (POLİSHİNG VE CİLA)"""])
    Araclar.append(["Seat", "İbiza", "2015", "565000",
                    """2015 SEAT Ibiza Sport Coupe 1.4 TSI Cupra DSG boyasız değişensiz\nCam Tavan\nLed Bi-Xenon Farlar\nCruise Control \nPiano Black 17 Orijinal Jantlar"""])
    Araclar.append(["Seat", "İbiza", "2016", "989000",
                    """2017 MAYIS TRAFİK ÇIKIŞLI\n1.8 TSI 192 HP MOTOR\nÖZEL PLAKA\nÜST DÜZEY DONANIM VE ÖZELLİKLER\nELEKTRONİK KİLİTLİ DİFERANSİYEL ( XDS )\nSPORT MOD ( DİREKSİYON GAZ TEPKİME HIZI VE SÜSPANSİYON AYARI )\nPANORAMİK SUNROOF\nAPPLE CAR PLAY\nBİ XENON LED FAR SİSTEMİ\nLED GÜNDÜZ VE STOP FARLARI\nFAR YIKAMA\nSTATİK AYDINLATMA SİSTEMİ\nKATLANABİLİR AYNALAR\nYAĞMUR - FAR - PARK SENSÖRLERİ\nKARARAN DİKİZ AYNASI\n6 AİRBAG\nSPOR KOLTUKLAR\nVS\nKOLEKSİYON DEĞERİNDE BİBLO MİSALİ\nGÜÇ VE DİNAMİK BİR ARADA\nHATASIZ - BOYASIZ - ÇİZİK DAHİ YOK"""])
    Araclar.append(["Seat", "İbiza", "2016", "559000",
                    """Araç 85.500 km de hasar kaydı yoktur.\nİlk sahibinden temiz özenli kullanılmıştır.\nBakımları zamanında ve eksiksiz yapılmıştır.\nDaha çok şehir içinde kullanılmıştır.\nKitapçıkları yedek anahtarı mevcuttur.\nDetaylı temizliği yeni yapılmıştır.\nKaputta ppf film vardır.\nAraç fabrika çıkışlı sunrooflu ve xenon mercek farlıdır. \nKeyifle binilecek modelleri arasında nadir bulunan temiz araçtır."""])

    Araclar.append(["Volkswagen", "Golf", "2015", "1420000",
                    """ARAÇTAKİ EKSTRALAR;\nÖZEL R PLAKA (xx.xxx TL)\nSTAGE 3 YAZILIM (550 HP) (7.000 TL)\nTTH 550 BÜYÜK TURBO (550 HP'E KADAR UYUMLU) (3.700 EURO)\nİGNİTİON PROJECTS PERFORMANS TİPİ BOBİN SETİ (785 USD)\nKW ELEKTRONİK AYARLI (DCC UYUMLU) COİLOVER SET (3.525 EURO)\nOZ ULTRALEGGERA 18 JANT TAKIMI (30.000 TL)\nBREMBO S3 BÜYÜK FREN KİTİ (2.950 EURO)\nEVENTURİ FİLTRE KİTİ (1.150 EURO)\nKOMPLE FORGE HORTUM SETİ (500 USD)\nFORGE BLOW OFF / DUMP VALVE SET (305 USD)\nİNNOVATE MOTORSPORT 4’LÜ PERFORMANS SETİ VE GÖSTERGE KİTİ (405 USD)\nSNOW PERFORMANCE METHANOL KİTİ VE GÖSTERGESİ (770 EURO)\nLEDLİ VE EKRANLI KARBON DİREKSİYON (23.000 TL)\nKOMPLE MİLLTEK EGZOS SİSTEMİ (47.000 TL)"""])
    Araclar.append(["Volkswagen", "Golf", "2015", "1375000",
                    """Hayalet Ekran(EKSTRA)\nDiscovery Pro Mib II Multimedia Sistemi(EKSTRA)\nPark Mesafe Kontrol\nGeri Görüş kamerası\nAlcantara Direksiyon\nCarbon R koltuklar\nAuto Start-Stop\nEco-Comfort-Race-İndividual Sürüş Seçenekleri\nU Led Gündüz Farları\n4x4 Çekiş Kontrol Sistemi\nFar Asist\nAuto Far\nElektrokrom İç Ayna\nMulti Fonksiyonel Direksiyon\nElektirikli Isıtmalı Katlanır Yan Aynalar\nÇift Bölgeli Dijital Klima\nBluetooth-Usb-Cd-Mp3 Player\nElektrikli Park Freni\nDSG Şanzuman\nF1 Paddle Shift\nAdaptif Servotronik Direksiyon\nHard Drive Multimedya Hafıza\nCd Challenger\nDijital Klima\nUSB\nAUX\nYağmur Sensörü\nFar Sensörü\nUzun Far Asistanı\nAdaptif Xenon Farlar\nYol Bilgisayarı"""])
    Araclar.append(["Volkswagen", "Golf", "2016", "2250000",
                    """O.z Racing Ultraleggera Jant\nBucket Seat 6R Koltuk Orjinal\nForge 6 piston Frenler\nGoodridge Çelik Fren Hortumları\nKomple Valfi Milltek Exhaust\nÖzel Yalıtımlı DownPipe\nGarret G25-660 Yeni Nesil Turbo Kitt\nKW V3 Dcc Coilovers \nNS2R Semi Slinck 4 Adet Lastik \nApr Mavi Bobin 4 Adet\nBrisk Racing Yeni Nesil Buji 4 Adet \nRacingline Oil Catch can\nRacingline R600 İntake Yeni Nesil \nForge Marka Full Set Motor İçi  Hortumlar \nCts Turbo Throttle Pipe\nAuto Tech Ön Yakıt Pompası\nP3 Dijital Gösterge\nÖn Arka H&R Viraj Demirleri\nForge Dv \nCharge Pipe\nEcs Tuning Sway Bar Endlikleri \nHg Motorsport İntercoller \nLeyo Turbo Muffler Delete \nHf Series İnlet Pipe \nRevo Low Pressure Fuel Pump Low \n(Arka Yakıt Pompası)"""])
    Araclar.append(["Volkswagen", "Golf", "2016", "1425000",
                    """Park Mesafe Kontrol Geri Görüş\nAuto Start-Stop\nEco-Comfort-Race Sürüş Seçenekleri\nU Led Gündüz Farları\nn4x4 Haldex Çekiş Kontrol Sistemi\n​360 Park Mesafe Sensörü\nFar Asist\nAuto Far\nElektrokrom İç Ayna\nMulti Fonksiyonel Direksiyon\nElektirikli Isıtmalı Katlanır Yan Aynalar\nÇift Bölgeli Dijital Klima\nBluetooth-Usb-Cd-Mp3 Player\nElektrikli Park Freni\nDSG Şanzuman\nF1 Paddle Shift\nAdaptif Servotronik Direksiyon\nHard Drive Multimedya Hafıza\nCd Challenger\nDijital Klima\nUSB\nAUX\nYağmur Sensörü\nFar Sensörü\nUzun Far Asistanı\nR Koltuklar\nAdaptif Xenon Farlar\nElektrikli Katlanır Aynalar\nFonksiyonel Deri Direksiyon \nYol Bilgisayarı"""])
    Araclar.append(["Volkswagen", "Passat", "2015", "1420000",
                    """2015 MODEL HİGHLİNE FULL +FULL\nARAÇTA BAKIMLI \nMASRAFSIZ BİR ARAÇTIR \nİÇİ KREM DERİ DÖŞEME\nARAÇ MAKAM ARACIDIR\nAKPARTİ TUTKUNLARI İÇİN İDEAL \nARAÇTA TRAMER 34.000TL \nNOT:TAKAS OLUR \nS KASA MERCEDES \nAUDİ A8 LONG"""])
    Araclar.append(["Volkswagen", "Passat", "2015", "1375000",
                    """Tungsten gri\n- Cam tavan\n- Hayalet ekran\n- Discover pro" navigasyon sistemi\n- Isıtmalı direksiyon\n- Elektrikli arka perde ve manuel yan perdeler\n- Adaptif hız sabitleyici_ ACC (160 km), Front assist \n- Side assist, Liane assist \n- 19 Verona jantlar, yeni lastikler\n- Area view" çevre görüş sistemi\n- Ahşap iç dekor"""])
    Araclar.append(["Volkswagen", "Passat", "2016", "1740000",
                    """Spor Direksiyon\nSpor tam deri, hafıza ve masajlı ön koltuklar\nDynaudio Ses Sistemi\nSunroof\nHayalet Ekran\nDiscovery Pro Dahili Navigasyon ve CarPlay\nKoltuk Isıtma\nLine Assist ( Şerit Takip Asistanı )\nUzun Far Asistanı \nAdaptif Cruise Control \nFront Assist ( Ön Çarpışma Uyarısı )\nBlint Spot Detection ( Kör Nokta Uyarı )\nArka Klima Kontrolü\nElektrikli Bagaj\nAdaptif Şasi Kontrolü\nAnahtarsız Çalıştırma\nAnahtarsız Giriş\n360 Derece ve Arka Kamera \nFabrikasyon R-Line Ön Tampon ve Izgara\nR-Line Arka Tampon ve Marşpiyer\nOtomatik Katlanır Aynalar\n19 inç Orjinal Vw Verona Jant"""])
    Araclar.append(["Volkswagen", "Passat", "2016", "1550000",
                    """Dynaudio Ses Sistemi\nSunroof\nHayalet Ekran\nDiscovery Pro Dahili Navigasyon ve CarPlay\nKoltuk Isıtma\nLine Assist ( Şerit Takip Asistanı )\nUzun Far Asistanı \nAdaptif Cruise Control \nFront Assist ( Ön Çarpışma Uyarısı )\nBlint Spot Detection ( Kör Nokta Uyarı )\nArka Klima Kontrolü\nElektrikli Bagaj\nAdaptif Şasi Kontrolü\nAnahtarsız Çalıştırma\nAnahtarsız Giriş\n360 Derece ve Arka Kamera \nFabrikasyon R-Line Ön Tampon ve Izgara\nR-Line Arka Tampon ve Marşpiyer\nOtomatik Katlanır Aynalar\n19 inç Orjinal Vw Verona Jant\nÖzel Seramik Fren Disk + Balata\nİç Dizayna Uygun Kaplama Direksiyon\nBoya Koruma +Seramik \nAraç Full Şeffaf Kaplama"""])

    Araclar.append(["Renault", "Clio", "2015", "800000",
                    """ARACIMIZ\n2015 MODEL\n1.6 TURBO RS \n250 HP \nABS - ASR - ESP\nSTART - STOP\nF1 \nLED FAR\nANAHTARSIZ GİRİŞ\nANAHTARSIZ ÇALIŞTIRMA\nDİJİTAL KLİMA\nFONKSİYONEL DİREKSİYON​\nRENAULT SPORT SÜRÜŞ MODU \nKATLANIR AYNA\nRENAULT SPORT KOLTUK\nRENAULT SPORT DİREKSİYON \nRENAULT SPORT KONTROL EKRANI \nDOKUNMATİK EKRAN\nNAVİGASYON \nYAĞMUR FAR SENSÖRÜ\nAEM AFR SAATİ \nDOWNPİPE\nBÜYÜK İNTERCOOLER\nİSKENDER YAPIMI \nKROM DÜZ BORU \nSEDEFLİ SARI \nBLUETOOTH - TELEFON\nUSB - AUX \nORJİNAL 18'' RS JANT\nARACIMIZ GARAJ ARACIDIR \nEMSALSİZ'DİR \nMANTIKLI ARAÇLAR İLE TAKAS OLABİLİR\nKREDİ KARTINA 8 AY TAKSİT İMKANI  \nANLAŞMALI BANKALAR İLE HIZLI KREDİ İMKANI"""])
    Araclar.append(["Renault", "Clio", "2015", "480000",
                    """Orjinal RS ön tampon\nOrjinal İnitiale Paris farlar\nOrjinal RS direksiyon\nOrjinal RS koltuk takımı ( arkalar geldi önleri bekliyorum )\nOrjinal RS kadran\nOrjinal RS Drive tuş\nOrjinal RS vites topuzu \nOrjinal RS marşpiyel\nOrjinal RS difüzör\nOrjinal RS spoiler\nOrjinal RS smoke 3. Fren lambası\nOrjinal RS geri görüş kamerası\nOrjinal led stop\nOrjinal İnitiale Paris klima paneli\nOrjinal tavan barı\nOrjinal 2020 Carplay \nOrjinal Bose hoparlör ve twitter takımı\n18 Oz Ultraleggera jant 205/35/18 Nankang Lastik\nBaşaran Coilover\nDr.Ecu yazılım\nDownpipe"""])
    Araclar.append(["Renault", "Clio", "2016", "524000",
                    """ANAHTARSIZ GİRİŞ-ÇALIŞTIRMA\nNAVİGASYON\nBASS REFLEX SES SİSTEMİ\nBİ XENON LED FARLAR\nLED STOPLAR\nHIZ SABİTLEYİCİ VE LİMİTLEYİCİ\nELEKTRİKLİ ISITMALI AYNALAR\nOTOMATİK KATLANIR YAN AYNALAR\nYAĞMUR VE FAR SENSÖRÜ\nARKA PARK SENSÖRÜ\nLASTİK BASINÇ SENSÖRÜ\nDOKUNMATİK EKRAN\nYARI DERİ KOLTUK\nECO MODU\nSTART-STOP\nBLUETOOTH-USB-AUX\nÇELİK JANT\nSİS FARI\nKışlık lastikleri yanında verilecektir\nSürtmeden dolayı sağ ön çamurluk değişmiştir\n2184 tl hasar kaydı vardır"""])
    Araclar.append(["Renault", "Clio", "2016", "515000",
                    """NAVİGASYON\nARKA KAMERA\nBLUETOOTH\nYOKUŞ KALKIŞ DESTEĞİ\nECO MODU\nSERVİS BAKIMLI\nİÇ DÖŞEMELERİ TEMİZ\nYEDEK ANAHTARI VE KİTAPÇIKLARI MEVCUT"""])
    Araclar.append(["Renault", "Megane", "2015", "519000",
                    """2014 modellerden farklı olarak;\n​Lastik basınç sensörleri\nYarı deri koltuk yapısı\nKarartılmış stop lambaları\nR-Link kullanıcı deneyimi (yakıt, sürüş vb.)\nİyileştirilmiş yalıtımı (Bence en önemlisi)\nSınıfının üstünde konfor ve donanıma sahip bir araçtır.\n﻿Anahtarsız giriş-çıkış ve çalıştırma (5 kapı aktif)\nÖn ve arka park sensörü (R-Link sesli ve görsel destekli)\nAnahtar üzerinden sunroof ve camları kapatma\nElektrikli park freni (aracı stop ettiğinizde otomatik kendi aktif olur, gaza bastığınızda otomatik devreden çıkar)\n412 litre bagaj hacmi\n17" alaşımlı jantlar"""])
    Araclar.append(["Renault", "Megane", "2015", "480000",
                    """2015 model 1,6 Touch Plus aracımızın hiçbir kazası ve tramer kaydı bulunmamaktadır. Tramer No: 457373003\nİhlalli geçiş ve ceza kaydı bulunmamaktadır.  \nMuayenesi yapılmıştır 29.1.2024’e kadar muayenesi geçerlidir.\nAraca ait vergi borcu bulunmamaktadır.\nSigortası düzenli olarak yapılmıştır.\nGenel bakımları ve yağ bakımı her zaman düzenli olarak yapılmıştır.\nAraç çok temizdir, alacak kişiye şimdiden hayırlı olsun.."""])
    Araclar.append(["Renault", "Megane", "2016", "880000 ",
                    """Sağ arka kapı mini onarım sol arka çamurluk ve kapı boyasız göçük giderme hasar kaydı 1340tl\nResimleri mevcut teslim edilecek\nSıfır En Full Paketi 976bin dir. benim aracta daha fazla donanım mevcutur. Sıfırı şu diye yazmayın Lütfen \nAracın ilk sahibiyim Fatura benim adıma \nTüm bakımları Her Yıl Yetkili serviste Antalya Zamanlar veya Isparta otopetrol den yapıldı. \n2021 Bakımında Triger değişimi yapıldı\nAraç boş Paket değildir Satış tarihinde listelenen Tüm Opsiyonlardan sadece Full deri koltuklar Eksiktir.\nMasajlı Sürücü koltuğu mevcut Sonraki paketlerde kaldırılmıştı.﻿\nÖn camlarda Arkaya yakın llumar Cam Film mevcut bu sene yatırdım\nYedek anahtardan Siyah olan kullanıldı Beyaz sıfır duruyor"""])
    Araclar.append(["Renault", "Megane", "2016", "738000",
                    """SAHİBİNDEN KAZASIZ TRAMERSİZ DEĞİŞENSİZ MEGANE 4 İCON 1.5 DCİ\nMASAJLI KOLTUK\nELLER SERBEST BAGAJ AÇMA\nYORGUNLUK ALGILAMA\nANAHTARSIZ GİRİŞ/ÇIKIŞ/ÇALIŞTIRMA\nYOKUŞ KALKIŞ DESTEĞİ\nMULTİSENSE 5 FARKLI SÜRÜŞ MODU\nR-LİNK MULTİMEDYA\nSESLİ KOMUT ÖZELLİĞİ\nGERİ GÖRÜŞ KAMERASI VE SENSÖRLER\n5 FARKLI RENK İÇ AMBİYANS AYDINLATMA\nKARARTMA CAMLAR\nOTOMATİK KARARAN DİKİZ VE YAN AYNALAR\nBLUETOOTH TELEFON BAĞLAMA/ARAMA\nELEKTRONİK PARK FRENİ\nXZENON UZUN/KISA OTOMATİK LED FARLAR\nOTOMATİK GECE/TÜNEL ALGILAMA\nYAĞMUR SENSÖRÜ\nGECE/GÜNDÜZ LEDLERİ\nELEKTRONİK OTOMATİK KATLANAN AYNALAR\nCRUİSE CONTROL\nHIZ SABİTLEYİCİ/SINIRLAYICI\nSTART/STOP\nLASTİK BASINÇ KONTROL SİSTEMİ\nUSB GİRİŞLERİ\nİSOFİX\nİMMOBİLİZER\n4 ADET YAZLIK 205/50/R17 NOKİAN LASTİKLERİ YENİ ALDIM. AYRICA 4 ADET KIŞLIK LASTİKLERİ DE VERECEĞİM.\nTRİGER SETİ, FREN BALATALARI YENİ DEĞİŞTİ.\nARACIN TÜM BAKIMLARI DÜZENLİ OLARAK SERVİSTE YAPILDI"""])

    Araclar.append(["Mercedes", "A-serisi", "2015", "1685000 ",
                    """ARAÇ DONANIMI\nAÇILIR CAM TAVAN\nLED XENON FARLAR\nGERİ GÖRÜŞ KAMERASI\nSÜRÜŞ MODLARI\nF1 ŞANZUMAN\nÖN VE ARKA PARK SENSÖRÜ\nYAĞMUR SENSÖRÜ\nFAR SENSÖRÜ\nHIZ SABİTLEYİCİ\nELEKTRİKLİ KATLANIR AYNALAR\nÇİFT BÖLGELİ DİJİTAL KLİMA\nUSB-BLUETOOTH\nISOFİX…\nAraç Yetkili Servis Bakımlı Olup Kayıtları Mevcuttur.\nMichelin Pilot Sport 4 Lastikler Sifirdir \nBir Sonraki Bakim Ücretsizdir.."""])
    Araclar.append(["Mercedes", "A-serisi", "2015", "1660000",
                    """Yetkili servis bakımlı \nHatasız boyasız\nMichelin pilot4 performans lastikler\nÖzel GTR yan destekli koltuklar\nSağ ve sol hafızalı ısıtmalı koltuk\nAnahtarsız giriş çıkış ve çalıştırma\nEn çok tercih edilen özel mat gri\nVe daha birçok özellik \nAracın ikinci sahibiyim araç 2017 de trafiğe çıkmıştır bayi çıkışlı ve servis bakımlıdır oynanmış bir araç değildir sıfır araç kondisyonundadır garaj aracıdır"""])
    Araclar.append(["Mercedes", "A-serisi", "2016", "1875000",
                    """AÇILIR CAM TAVAN\nLED XENON FARLAR\nKÖR NOKTA UYARICI\nNAVİGASYON\nGERİ GÖRÜŞ KAMERASI\nSÜRÜŞ MODLARI\nF1 ŞANZUMAN\nÖN VE ARKA PARK SENSÖRÜ\nYAĞMUR SENSÖRÜ\nFAR SENSÖRÜ\nHIZ SABİTLEYİCİ\nELEKTRİKLİ KATLANIR AYNALAR\nÇİFT BÖLGELİ DİJİTAL KLİMA\nUSB-BLUETOOTH\nISOFİX..\nTRAMER \nBOYA : YOK \nDEĞİŞEN : YOK\nTRAMER : YOK"""])
    Araclar.append(["Mercedes", "A-serisi", "2016", "1725000",
                    """LCI Makyajlı Kasa\nAMG Body Kit\nAMG Styling Ön ve Arka Spoiler\nAMG Carbon Ayna Kapakları\nAMG Genisletilmis Camurluklar\nAMG 4 Piston Fren Sistemi\nAMG Deri Cockpit Paketi\nAMG Drive Paketi "Race Modu"\nAMG Sport Exhaust\nAMG Spor Suspansiyon\nAMG Işıklı Kapı Eşikleri\nAMG Gece Paketi\n18" AMG Spoke Jantlar\n4×4 Diffaransiyelli Aks\n7 İleri Çift Kavrama Şanzuman\nSpor Süspansiyon\nF1 Paddle Shift\nGeri Görüş Kamerası\nAktif Park Asistanı\nHafızalı Sürücü Koltuğu\nCam Tavan\nSD Card Navi\nTEMPOMAT \nSpor Süspansiyon\nOtomatik Katlanir Aynalar"""])

    Araclar.append(["Mercedes", "E-serisi", "2015", "2250000",
                    """PANORAMİK CAM TAVAN\nELEKTRİKLİ ARKA PERDE\nARKA MAKAM PERDELERİ\nPARK ASİSTANI\nLED GÜNDÜZ FARLARI\nSÜRÜŞE DUYARLI VİRAJ AYDINLATMA\n7G-TRONİC F-1 ŞANZIMAN\nECO MODE\nELEKTRİKLİ AYARLANIR ve KATLANIR YAN AYNALAR\nENTEGRE GÖSTERGELİ ve GENİŞ GÖRÜŞ AÇILI YAN AYNALAR\nOTOMATİK KARARAN YAN AYNALAR\nKOLTUKLAR BEJ DERİ DÖŞEME\nISITMALI ÖN KOLTUKLAR\n-ELEKTİRKLİ AYARLANABİLEN KOLTUKLAR\nSTART&STOP\nHIZ SABİTLEYİCİ&SINIRLAYICI\nANALOG SAAT\nLASTİK BASINÇ KONTROL SİSTEMİ\nHILL HOLDER(yokuş kalkış desteği)\nADAPTİF FREN SİSTEMİ"""])
    Araclar.append(["Mercedes", "E-serisi", "2015", "2000000",
                    """DONANIMLAR\nPanoramik Cam Tavan\n360 Derece 5 Bölge Kamera\nElektirikli Bağaj\nSağ-Sol Hafızalı Koltuklar\nSağ-Sol Isıtmalı Koltuklar​\nAnahtarsız Giriş-Çalıştırma​ Keyless Go\nElektirikli Çok Fonksiyonlu Direksiyon\nF1 Vites\nEco-Start-Stop\nYan Makam Perdeleri\nArka Elektrikli Perde\nÖzel Dikişli Bej Deri Döşeme\nBi-Xenon Farlar\nLed Stoplar \nGündüz Led\nÖn-Arka Park Sensörü​\nGeri Görüş Kamera\nAdaptif Süspansiyon Sistemi\nKrom Kaplama\nTorpido Soğutucu\nKatlanır Aynalar\nÖn-Arka Park Sensörleri\nFar - Yağmur Sensörü\nCd-Aux-Usb"""])
    Araclar.append(["Mercedes", "E-serisi", "2016", "3575000",
                    """KEYLESS-GO ANAHTARSIZ GİRİŞ-ÇIKIŞ VE ÇALIŞTIRMA\nELEKTRİKLİ BAGAJ\n360° KAMERA SİSTEMİ\nVAKUMLU KAPILAR\nELEKTRİKLİ AYARLANIR ÖN KOLTUKLAR\nHAFIZALI ÖN KOLTUKLAR\nISITMALI ÖN KOLTUKLAR\nARKA YAN VE ARKA PERDE\nGENİŞLETİLMİŞ MERKEZİ EKRAN VE DİJİTAL GÖSTERGE PANELİ\nAKTİF NAVİGASYON\nAKTİF ÇARPIŞMA ÖNLEME SİSTEMİ\nDİKKAT ASİSTANI\nAMBİYANS AYDINLATMA\nOTOMATİK FAR SENSÖRÜ\nOTOMATİK YAĞMUR SENSÖRÜ\nTOUCHPAD\nANALOG SAAT\nOTOMATİK İKİ BÖLGE KLİMA SİSTEMİ"""])
    Araclar.append(["Mercedes", "E-serisi", "2016", "3000000",
                    """Her şeyi ile nadir ve özel bir araçtır \nExstra 25.000 tl servis bakım paketi vardır önümüzde ki iki bakımı servis tarafından karşılanacaktır \nGerek gücüyle gerek konforuyla sürücüsüne zevk veren bir araçtır\n2017 trafiğe çıkışlıdır\nHATASIZ-BOYASIZ'dır \n2 adet ücretli trameri vardır toplam 12.000 tl far ve korna değişimindendir"""])

    ilanNo = 0
    for i in Araclar:
        ilanListe[str(ilanNo)] = {"ilan No": ilanNo, "Marka": i[0], "Model": i[1], "Yıl": i[2], "Fiyatı": i[3],
                                  "Özellikler": i[4]}
        ilanNo += 1


def AracEkle():
    global Araclar, ilanListe
    print("-------------------------------------------")
    marka = input("Marka Adı Giriniz\t")
    modeli = input("Model Adı Giriniz\t")
    yili = input("Araç Yılı Giriniz\t")
    parasi = input("Araç Fiyatını Giriniz\t")
    ozellik = input("Araç Özelliklerini Giriniz\n")
    Araclar.append([marka, modeli, yili, parasi, ozellik])
    ilanNo = len(ilanListe)
    ilanListe[str(ilanNo)] = {"ilan No": ilanNo, "Marka": marka, "Model": modeli, "Yıl": yili, "Fiyat": parasi,
                              "Özellikler": ozellik}
    print("Araç Eklendi. Ana Menuye Döndürülüyorsunuz.")


def AracSil():
    global Araclar
    print("-------------------------------------------")
    Sayac = 0
    for i in Araclar:
        print(Sayac, i[0], i[1], i[2], i[3], sep=" - ")
        Sayac += 1
    ilanNo = input("Silmek İstediğiniz İlan Numarasını Secin\t")
    Araclar.remove(Araclar[int(ilanNo)])
    ilanListe.pop(ilanNo)
    print("İlan Silindi. Ana Menuye Döndürülüyorsunuz.")


def MarkaAra():
    print("-------------------------------------------")
    marka = set()
    for i in Araclar:
        marka.add(i[0])
    sayac = 0
    for i in marka:
        print(sayac, i, sep=" - ")
        sayac += 1
    marka = list(marka)
    indeks = "-1"
    while int(indeks) > len(marka) - 1 or int(indeks) < 0:
        try:
            indeks = input("Tercih Edilen Markayı Giriniz:\t")
        except(ValueError):
            pass
    marka0 = marka[int(indeks)]

    print("-------------------------------------------")

    model = set()
    for i in ilanListe:
        if ilanListe[i]["Marka"] == marka0:
            model.add(ilanListe[i]["Model"])
    sayac = 0
    for i in model:
        print(sayac, i, sep=" - ")
        sayac += 1
    model = list(model)
    indeks = "-1"
    while int(indeks) > len(model) - 1 or int(indeks) < 0:
        try:
            indeks = input("Tercih Edilen Modeli Giriniz:\t")
        except(ValueError):
            pass
    model0 = model[int(indeks)]

    print("-------------------------------------------")

    yili = set()
    for i in ilanListe:
        if ilanListe[i]["Model"] == model0:
            yili.add(ilanListe[i]["Yıl"])
    sayac = 0
    for i in yili:
        print(sayac, i, sep=" - ")
        sayac += 1
    yil = list(yili)
    indeks = "-1"
    while int(indeks) > len(yili) - 1 or int(indeks) < 0:
        try:
            indeks = input("Tercih Edilen Yılı Giriniz:\t")
        except(ValueError):
            pass
    yil0 = yil[int(indeks)]

    print("-------------------------------------------")

    Fiyatlari = set()
    for i in ilanListe:
        if ilanListe[i]["Model"] == model0:
            if ilanListe[i]["Yıl"] == yil0:
                Fiyatlari.add(ilanListe[i]["Fiyatı"])
    sayac = 0
    for i in Fiyatlari:
        print(sayac, " - ", int(i), "TL")
        sayac += 1
    Fiyatlari = list(Fiyatlari)
    indeks = "-1"
    while int(indeks) > len(Fiyatlari) - 1 or int(indeks) < 0:
        try:
            indeks = input("Tercih Edilen Fiyatı Giriniz:\t")
        except(ValueError):
            pass
    Fiyatlar0 = Fiyatlari[int(indeks)]

    print("-------------------------------------------")

    for i in ilanListe:
        if ilanListe[i]["Model"] == model0:
            if ilanListe[i]["Yıl"] == yil0:
                if ilanListe[i]["Fiyatı"] == Fiyatlar0:
                    print(ilanListe[i]["Özellikler"])


def FiyatAra():
    print("-------------------------------------------")
    Fiyatlar = set()
    MusteriHedefi = int(input("Bütçenizi Belirtiniz\t"))

    for i in ilanListe:
        AracFiyati = int(ilanListe[i]["Fiyatı"])
        if MusteriHedefi > AracFiyati:
            Fiyatlar.add(AracFiyati)
    Fiyatlar = list(Fiyatlar)

    sayac = 0
    if len(Fiyatlar) < 1:
        print("Bütçeye Uygun Araç Bulunamamıştır.")
    else:
        print("Bütçe İçin Belirlenen Araçlar:")

        Aracliste0 = []
        for i in ilanListe:
            AracFiyati = int(ilanListe[i]["Fiyatı"])
            if AracFiyati in Fiyatlar:
                markasi0 = ilanListe[i]["Marka"]
                modeli0 = ilanListe[i]["Model"]
                yili0 = ilanListe[i]["Yıl"]
                fiyati0 = ilanListe[i]["Fiyatı"]
                Aracliste0.append([sayac, markasi0, modeli0, yili0, fiyati0])
                print(sayac, markasi0, modeli0, yili0, fiyati0, sep=" - ")
                sayac += 1

        indeks = "-1"
        while int(indeks) > len(Aracliste0) - 1 or int(indeks) < 0:
            try:
                indeks = input("Tercih Edilen Araç Kodunu Girin:\t")
            except(ValueError):
                pass

        indeks = int(indeks)
        markasi0 = Aracliste0[indeks][1]
        modeli0 = Aracliste0[indeks][2]
        yili0 = Aracliste0[indeks][3]
        fiyati0 = Aracliste0[indeks][4]

        print("-------------------------------------------")
        print(sayac, markasi0, modeli0, yili0, fiyati0, sep=" - ")
        print("Özelikleri:")

        for i in ilanListe:
            if ilanListe[i]["Model"] == modeli0:
                if ilanListe[i]["Yıl"] == yili0:
                    if ilanListe[i]["Fiyatı"] == fiyati0:
                        print(ilanListe[i]["Özellikler"])


def Dokum():
    print("-------------------------------------------")
    for i in ilanListe:
        markasi0 = ilanListe[i]["Marka"]
        modeli0 = ilanListe[i]["Model"]
        yili0 = ilanListe[i]["Yıl"]
        fiyati0 = ilanListe[i]["Fiyatı"]
        print(i, markasi0, modeli0, yili0, fiyati0, sep=" - ")

        indeks = "-1"
    while int(indeks) > len(ilanListe) - 1 or int(indeks) < 0:
        try:
            indeks = input("Tercih Edilen Araç Kodunu Girin:\t")
        except(ValueError, KeyError):
            pass
    markasi0 = ilanListe[indeks]["Marka"]
    modeli0 = ilanListe[indeks]["Model"]
    yili0 = ilanListe[indeks]["Yıl"]
    fiyati0 = ilanListe[indeks]["Fiyatı"]
    print("-------------------------------------------")
    print(markasi0, modeli0, yili0, fiyati0, sep=" - ")
    print(ilanListe[indeks]["Özellikler"])


def Menu():
    print("-------------------------------------------")
    print("Yapmak İstediğiniz Arama Biçimini Seçin")
    print("1-Markaya Göre Arama")
    print("2-Fiyata Göre Arama")
    print("3-Tüm İlanların Dökümü")
    print("8-Araç Silme")
    print("9-Araç Ekleme")
    print("q-Çıkış")

    MenuSayac0 = "0"
    while MenuSayac0 == "0":
        MenuSayac0 = input("Bir Menü Seçiniz:\t")

        if MenuSayac0 == "1":
            MarkaAra()
        elif MenuSayac0 == "2":
            FiyatAra()
        elif MenuSayac0 == "3":
            Dokum()
        elif MenuSayac0 == "8":
            AracSil()
            Menu()
        elif MenuSayac0 == "9":
            AracEkle()
            Menu()
        elif MenuSayac0 == "q":
            return
        else:
            MenuSayac0 = "0"


def Calıstır():
    print("--------- Galerimize Hoş Geldiniz ---------")
    MevcutAraclar()
    Menu()


Calıstır()



# In[ ]:




