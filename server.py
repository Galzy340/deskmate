import os
import urllib.request
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000
IMG_DIR = "img"

# Daftar gambar placeholder otomatis
IMAGES = {
    "deskmat-hero.jpg": "https://images.unsplash.com/photo-1616588589676-63b3dd983446?w=1000&q=80",
    "produk1.jpg": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=600&q=80",
    "produk2.jpg": "https://images.unsplash.com/photo-1541140590914-579f21a6a13f?w=600&q=80",
    "produk3.jpg": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600&q=80",
    "about.jpg": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80"
}

def prepare_environment():
    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)
        print(f"[+] Folder '{IMG_DIR}/' berhasil dibuat.")

    print("[*] Memeriksa dan mengunduh gambar sampel jika belum ada...")
    for file_name, url in IMAGES.items():
        file_path = os.path.join(IMG_DIR, file_name)
        if not os.path.exists(file_path):
            try:
                print(f" -> Mengunduh {file_name}...")
                urllib.request.urlretrieve(url, file_path)
            except Exception as e:
                print(f" [!] Gagal mengunduh {file_name}: {e}")
        else:
            print(f" [✓] {file_name} sudah ada.")

def run_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    url = f"http://localhost:{PORT}"
    
    print(f"\n[+] Server berjalan di {url}")
    print("[+] Tekan Ctrl+C di terminal untuk menghentikan server.")
    
    webbrowser.open(url)
    httpd.serve_forever()

if __name__ == "__main__":
    prepare_environment()
    run_server()