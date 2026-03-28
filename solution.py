"""
mini-diary v0 — Basitlestirilmis implementasyon
Ogrenci: [Ad Soyad] ([Numara])

Kapsam: Sadece init ve write komutlari.
Sinirlamalar: Dongu ve liste henuz kullanilmadi.
"""
import sys
import os

def initialize():
    """Klasor ve bos gunluk dosyasi olusturur."""
    if os.path.exists(".minidiary"):
        return "Already initialized"
    
    os.mkdir(".minidiary")
    # Bos bir dosya acip hemen kapatiyoruz
    f = open(".minidiary/diary.dat", "w")
    f.close()
    return "Initialized empty diary in .minidiary/"

def write_entry(content):
    """Yeni bir gunluk yazisi ekler. ID'yi dosya boyutuna gore hesaplar."""
    if not os.path.exists(".minidiary"):
        return "Error: Initialize first using 'init'"
    
    # Mevcut icerigi oku (Satir sayisini saymak icin)
    f = open(".minidiary/diary.dat", "r")
    full_text = f.read()
    f.close()
    
    # Basit ID hesabi: Kac tane yeni satir karakteri varsa o kadar yazi vardir
    # Hic yazi yoksa ID 1 olur, varsa satir sayisi + 1 olur
    entry_id = full_text.count("\n") + 1
    
    # Tarihi manuel ekliyoruz (Henuz datetime modulu karmaik gelebilir)
    date_str = "2026-03-15" 
    
    # Veriyi dosyaya ekle (Append modu)
    f = open(".minidiary/diary.dat", "a")
    f.write(str(entry_id) + "|" + date_str + "|" + content + "\n")
    f.close()
    
    return "Entry saved with ID: " + str(entry_id)

def show_not_implemented(command_name):
    """Henuz hazir olmayan komutlar icin uyari mesaji verir."""
    return "Command '" + command_name + "' will be implemented in future weeks."

# --- Ana Program (Arguman Yonetimi) ---

# Kullanici hicbir sey yazmazsa kullanim klavuzunu goster
if len(sys.argv) < 2:
    print("Usage: python diary.py <command> [args]")

elif sys.argv[1] == "init":
    print(initialize())

elif sys.argv[1] == "write":
    # write komutu icin mesaj girilip girilmedigini kontrol et
    if len(sys.argv) < 3:
        print("Usage: python diary.py write \"Your message\"")
    else:
        print(write_entry(sys.argv[2]))

elif sys.argv[1] == "list":
    print(show_not_implemented("list"))

elif sys.argv[1] == "read":
    print(show_not_implemented("read"))

elif sys.argv[1] == "delete":
    print(show_not_implemented("delete"))

else:
    print("Unknown command: " + sys.argv[1])