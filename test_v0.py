"""
mini-diary SPEC test senaryolari
Ogrenci: [Adin Soyadin] ([Numaran])
Proje: mini-diary
"""
import subprocess
import os
import shutil

# --- Yardimci Fonksiyon ---
def run_cmd(args):
    """Programi (solution.py) calistirir ve ciktisini dondurur."""
    # Dosya adin solution.py oldugu icin burada onu kullaniyoruz
    result = subprocess.run(
        ["python", "solution.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def setup_function():
    """Her testten once temiz bir baslangic yapmak icin klasoru siler."""
    if os.path.exists(".minidiary"):
        shutil.rmtree(".minidiary")

# --- 10 ADET TEST SENARYOSU ---

def test_init_creates_directory():
    """Test 1: Klasor olusuyor mu?"""
    run_cmd(["init"])
    assert os.path.exists(".minidiary"), ".minidiary dizini olusturulmali"

def test_init_already_exists():
    """Test 2: Zaten varsa uyari veriyor mu?"""
    run_cmd(["init"])
    output = run_cmd(["init"])
    assert "Already initialized" in output

def test_write_single_entry():
    """Test 3: Ilk yazi ID 1 ile kaydediliyor mu?"""
    run_cmd(["init"])
    output = run_cmd(["write", "Hello Diary"])
    assert "Entry saved with ID: 1" in output

def test_write_multiple_entries():
    """Test 4: Ikinci yazi ID 2 oluyor mu?"""
    run_cmd(["init"])
    run_cmd(["write", "First"])
    output = run_cmd(["write", "Second"])
    assert "ID: 2" in output

def test_list_not_implemented():
    """Test 5: list komutu v0'da uyari veriyor mu?"""
    run_cmd(["init"])
    output = run_cmd(["list"])
    assert "will be implemented" in output

def test_read_not_implemented():
    """Test 6: read komutu v0'da uyari veriyor mu?"""
    run_cmd(["init"])
    output = run_cmd(["read", "1"])
    assert "will be implemented" in output

def test_delete_not_implemented():
    """Test 7: delete komutu v0'da uyari veriyor mu?"""
    run_cmd(["init"])
    output = run_cmd(["delete", "1"])
    assert "will be implemented" in output

def test_error_no_init():
    """Test 8: init yapmadan write kullanilirsa hata veriyor mu?"""
    output = run_cmd(["write", "Test"])
    assert "Error: Initialize first" in output

def test_unknown_command():
    """Test 9: Gecersiz komut hatasi?"""
    run_cmd(["init"])
    output = run_cmd(["fly"])
    assert "Unknown command" in output

def test_usage_no_args():
    """Test 10: Hic arguman girilmezse yardim mesaji geliyor mu?"""
    output = run_cmd([])
    assert "Usage:" in output
