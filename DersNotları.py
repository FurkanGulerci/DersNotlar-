
import sqlite3

vt = sqlite3.connect("/Users/furkangulerci/Documents/VsCode/Ders Notları/Dersnotları.db")
imlec = vt.cursor()

#Tablo Oluşturma
def tablo_olustur():
	imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciler(Ad_Soyad TEXT, Fizik İNT, Kimya İNT, Ortalama İNT)")
	vt.commit()
tablo_olustur()
def Ogrenciler (Ad_soyad, Fizik, Kimya, Ortalama):
	imlec.execute("INSERT INTO ogrenciler VALUES(?,?,?,?)"(Ad_soyad, Fizik, Kimya, Ortalama))
	vt.commit()
def ogrenci_guncelle():
	ad_soyad = input("Öğrenci Adı Soyadı Nedir?")
	secim = int(input("1-Adı Soyadı 2- Fizik 3- Kimya Güncellemek İstediğiniz Nedir?:"))
	if secim == 1:
		yeni_isim = str(input("Ad Soyad:"))
		imlec.execute("UPDATE Ogrenciler SET ad_soyad = ? WHERE ad_soyad = ?", (yeni_isim, ad_soyad))
	if secim == 2:
		yeni_fizik = int(input("Fizik:"))
		imlec.execute("UPDATE Ogrenciler SET fizik = ? WHERE ad_soyad = ?", (yeni_fizik, ad_soyad))
	if secim == 3:
		yeni_kimya = int(input("Kimya:"))
		imlec.execute("UPDATE Ogrenciler SET kimya = ? WHERE ad_soyad = ?", (yeni_kimya, ad_soyad))
	vt.commit()
def ogrenci_sil():
    silmek = input("Silmek İstediğiniz Ögrencinin Adı Soyadı Nedir ?")
    imlec.execute("DELETE FROM Ogrenciler WHERE ad_soyad = ?", (silmek))
    
while True:
	print("\n \n \n1)Öğretmen misiniz:")
	print("2)Öğrenci misiniz:")
	giris = int(input("Kullanıcı:"))
	
#Öğretmen Girişi
	if giris == 1:
		print("\n \n \nHoşgeldiniz!")
		print("1-Öğrencileri Listele")
		print("2-Öğrenci Ekle")
		print("3-Öğrenci Bilgileri Düzenle")
		print("4-Öğrenci Sil")
		print("5-Ana Sayfa")
		admin_menu = int(input("Seçimizin:"))
  
#Öğrencileri Listele
		if admin_menu == 1:
			imlec.execute("SELECT * From ogrenciler")
			liste = imlec.fetchall()
			for i in liste:
				print(i)
    
#Öğrenci Ekle
		elif admin_menu == 2:
			print("\n \n \nÖğrenci Ekleme")
			ad_soyad = str(input("Adı Soyadı:"))
			fizik = int(input("Fizik:"))
			kimya = int(input("Kimya:"))
			ortalama = (fizik+kimya)/2
			imlec.execute("INSERT INTO Ogrenciler(Ad_soyad, Fizik, Kimya, Ortalama) VALUES (?,?,?,?)",(ad_soyad,fizik,kimya,ortalama))
			vt.commit()
			str(input("Üst menüye dönmek için herhangi bir tuşa basınız:"))
#Öğrenci Bilgileri Güncelleme
		elif admin_menu == 3 :
			ogrenci_guncelle()
			vt.commit()
#Öğrenci Kaydı Sil
		elif admin_menu == 4 :
			ogrenci_sil()
			vt.commit()
		else :
			break
		
#Ögrenci Giriş
	if giris == 2:
		arama = str(input("\n \n \nAdınız Soyadınız ?:"))
		imlec.execute("SELECT * FROM Ogrenciler WHERE ad_soyad = ?", (arama,))
		sonuc = imlec.fetchall()
		if sonuc:
			for s in sonuc:
				print(s)
				print("Ortalamanız",ortalama)
		


		