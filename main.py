urunler = {"1":{"ürün":"Çelik Yüzük","fiyat":75},
           "2":{"ürün":"Deri Bileklik","fiyat":120},
           "3":{"ürün":"Gümüş Küpe","fiyat":180},
           "4":{"ürün":"Doğaltaş Kolye","fiyat":240},
           "5":{"ürün":"Güneş Gözlüğü","fiyat":320},
           "6":{"ürün":"Minimalist Saat","fiyat":450},
           "7":{"ürün":"Bez Çanta","fiyat":90},
           "8":{"ürün":"Fular/Eşarp","fiyat":110},
           "9":{"ürün":"Kravat İğnesi","fiyat":150},
           "10":{"ürün":"Şapka/Bere","fiyat":210},
}
sepet = []
while True:
    print("\n--- SEPETİNİZ ---")
    if len(sepet) == 0:
        print("(Sepetiniz boş.)")
    else:
        for item in sepet:
            print(f"\u2605 {item["ürün"]} - {item["fiyat"]} ₺")
    print("------------------------------")
    
    print("\n--- ÜRÜN MENÜSÜ ---")
    for no, detay in urunler.items():
        print(f"{no} -> {detay["ürün"]} : {detay["fiyat"]} ₺")
    
    alisveris = (input(f"Almak istediğiniz ürün numarasını yazın:(satın al = q): ")).strip().lower()
 
    if alisveris == "q":
        break
    elif alisveris in urunler:
        sepet.append(urunler[alisveris])
        print(f"\u2605 {urunler[alisveris]["ürün"]} sepete eklendi.")
    else:   
        print("Geçersiz seçim yaptınız!! Lütfen listedeki numaralardan birini seçin.")    

toplam_tutar = 0
kargo_tutarı = 30 
for u in sepet:
    urun = u["ürün"]
    fiyat = u["fiyat"]
    toplam_tutar += fiyat 
        
if len(sepet) == 0:
    print("Sepetiniz boş olduğu için fiş oluşturulmadı.")
else:
    print("=" * 40)
    print("       SATIŞ FİŞİ / ÖZET       ")
    print("=" * 40)
    
    for i in sepet:
        print(f"\u2605 {i["ürün"].title()} - {i["fiyat"]} ₺")
    print("-" * 40)
    print(f"Ürünler Toplamı : {toplam_tutar} ₺")
    if toplam_tutar < 300:
        kargo = 30
        genel_toplam = toplam_tutar + kargo
        print("Kargo Bilgisi   : 300 ₺ altı siparişlerde 30 ₺ kargo ücreti uygulanır.")
        print("-" * 40)
        print(f"ÖDEMENİZ GEREKEN TUTAR (Kargo Dahil): {genel_toplam} ₺")
    else:
        print("Kargo Bilgisi   : 300 ₺ üzeri alışverişinizden dolayı kargo ÜCRETSİZDİR!")
        print("-" * 40)
        print(f"ÖDEMENİZ GEREKEN TUTAR: {toplam_tutar} ₺")
        
    print("=" * 40)