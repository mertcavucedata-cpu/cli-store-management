# 🛒 Konsol Tabanlı Mağaza & Sepet Yönetim Sistemi

Python öğrenme sürecimde temel veri yapıları, kullanıcı girdi yönetimi ve mantıksal akışları pekiştirmek amacıyla geliştirdiğim konsol tabanlı mağaza ve satış fişi simülasyonu.

## 🚀 Özellikler

* **Canlı Sepet Görünümü:** Kullanıcı ürün seçtikçe sepetin anlık durumunu ekranın üst kısmında dinamik olarak gösterme.
* **Dinamik Ürün Menüsü:** Sözlük (dictionary) yapısında tutulan ürünleri fiyatlarıyla birlikte düzenli bir menü olarak listeleme.
* **Hatalı Girdi Kontrolü:** Kullanıcının hatalı tuşlamalarını veya büyük/küçük harf durumlarını (`strip()`, `lower()`) yakalayarak uygulamanın çökmesini engelleme.
* **Otomatik Kargo & Fiş Dökümü:** Alışveriş bitiminde ürünlerin toplam tutarını hesaplama, belirlenen kargo barajına (300 TL) göre kargo ücretini otomatik ekleme/düşme ve detaylı fiş basma.

## 🛠️ Kullanılan Teknolojiler & Konseptler

* **Dil:** Python 3
* **Konseptler:** İç içe Veri Yapıları (Dictionary in List), `while` ve `for` döngüleri, Koşullu İfadeler (`if-elif-else`), Girdi Temizleme (Sanitization), CLI Menü Yönetimi

## 📚 Bu Projede Pekiştirdiğim Konular

* `dict.items()` ile sözlük üzerinde döngü kurma
* Liste içine sözlük ekleme ve veri çekme (`sepet.append()`)
* String metodları (`strip()`, `lower()`, `title()`)
* Toplam tutar ve kargo mantığı algoritması oluşturma
* Konsol üzerinde düzenli ve okunabilir çıktı tasarımı
