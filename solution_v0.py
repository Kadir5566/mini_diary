import sys
import os

def initialize():
    """Klasor ve bos gunluk dosyasi olusturur."""
    if os.path.exists(".minidiary"):
        return "Already initialized"
    
    os.mkdir(".minidiary")
    f = open(".minidiary/diary.dat", "w")
    f.close()
    return "Initialized empty diary in .minidiary/"

def write_entry(content):
    """Yeni bir gunluk yazisi ekler. ID'yi satir sayisina gore hesaplar."""
    if not os.path.exists(".minidiary"):
        return "Error: Initialize first using 'init'"
    
    # Mevcut icerigi oku
    f = open(".minidiary/diary.dat", "r")
    full_text = f.read()
    f.close()
    
    # ID hesabi: Kac tane yeni satir karakteri varsa o kadar yazi vardir
    entry_id = full_text.count("\n") + 1
    
    # Statik tarih (Baslangicta boyleydi)
    date_str = "2026-03-15" 
    
    # Veriyi dosyaya ekle (Append modu)
    f = open(".minidiary/diary.dat", "a")
    f.write(str(entry_id) + "|" + date_str + "|" + content + "\n")
    f.close()
    
    return "Entry saved with ID: " + str(entry_id)

def show_not_implemented(command_name):
    """Henuz hazir olmayan komutlar icin uyari mesaji verir."""
    return "Command '" + command_name + "' will be implemented in future weeks."

# --- Ana Program ---

if len(sys.argv) < 2:
    print("Usage: python diary.py <command> [args]")

elif sys.argv[1] == "init":
    print(initialize())

elif sys.argv[1] == "write":
    if len(sys.argv) < 3:
        print("Usage: python diary.py write \"Your message\"")
    else:
        print(write_entry(sys.argv[2]))

elif sys.argv[1] in ["list", "read", "delete"]:
    print(show_not_implemented(sys.argv[1]))

else:
    print("Unknown command: " + sys.argv[1])
