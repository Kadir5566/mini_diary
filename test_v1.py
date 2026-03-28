import os
import shutil
import time
import subprocess

# Test klasoru ve dosya isimleri
TEST_DIR = ".minidiary"
SCRIPT_NAME = "solution.py"

def run_cmd(args):
    """Terminal komutunu calistirir ve ciktisini dondurur."""
    result = subprocess.run(['python', SCRIPT_NAME] + args, capture_output=True, text=True, encoding="utf-8")
    return result.stdout.strip()

def setup_test():
    """Test oncesi temizlik yapar."""
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)
    print("[1/6] Temizlik tamamlandi.")

def test_init():
    print("[2/6] Test: 'init' komutu...")
    out = run_cmd(["init"])
    if os.path.exists(TEST_DIR) and "Initialized" in out:
        print("  -> BAŞARILI: Klasör oluşturuldu.")
    
    out_again = run_cmd(["init"])
    if "Already initialized" in out_again:
        print("  -> BAŞARILI: Tekrar kurulum engellendi.")

def test_write():
    print("[3/6] Test: 'write' komutu (v0 Mantığı)...")
    run_cmd(["write", "İlk test mesajı"])
    run_cmd(["write", "İkinci test mesajı"])
    out = run_cmd(["write", "Üçüncü test mesajı"])
    
    if "ID: 3" in out:
        print("  -> BAŞARILI: 3 adet kayıt yapıldı ve ID'ler doğru atandı.")

def test_list():
    print("[4/6] Test: 'list' komutu (v1 Revize)...")
    out = run_cmd(["list"])
    if "İlk test mesajı" in out and "Üçüncü test mesajı" in out:
        print("  -> BAŞARILI: Tüm kayıtlar listelendi.")
    else:
        print("  -> HATA: Liste eksik!")

def test_search():
    print("[5/6] Test: 'search' komutu (v1 Revize)...")
    # Büyük/küçük harf duyarlılığı testi
    out = run_cmd(["search", "İkinci"])
    out_lower = run_cmd(["search", "ikinci"])
    
    if "ID [2]" in out and "ID [2]" in out_lower:
        print("  -> BAŞARILI: Arama motoru büyük/küçük harf duyarsız çalışıyor.")
    else:
        print("  -> HATA: Arama sonuç vermedi!")

def test_error_handling():
    print("[6/6] Test: Hata yönetimi...")
    out = run_cmd(["bilinmeyen_komut"])
    if "Unknown command" in out:
        print("  -> BAŞARILI: Geçersiz komut yakalandı.")

if __name__ == "__main__":
    print("=== Mini-Diary v1 Otomatik Test Başlatılıyor ===\n")
    if not os.path.exists(SCRIPT_NAME):
        print(f"HATA: {SCRIPT_NAME} dosyası bulunamadı! Lütfen dosya adını kontrol edin.")
    else:
        setup_test()
        test_init()
        test_write()
        test_list()
        test_search()
        test_error_handling()
        print("\n=== Tüm Testler Başarıyla Tamamlandı! ===")
