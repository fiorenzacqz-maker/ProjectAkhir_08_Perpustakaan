import os
from datetime import datetime

buku_list = [
    {"judul": "bumi manusia", "penulis": "pramoedya ananta toer", "kategori": "sejarah / realisme sosial",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 7, "dipinjam_count": 45},
    {"judul": "laskar pelangi", "penulis": "andrea hirata", "kategori": "inspiratif / pendidikan",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 3, "dipinjam_count": 78},
    {"judul": "cantik itu luka", "penulis": "eka kurniawan", "kategori": "realisme magis",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 9, "dipinjam_count": 52},
    {"judul": "laut bercerita", "penulis": "leila s. chudori", "kategori": "sejarah / politik",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 5, "dipinjam_count": 61},
    {"judul": "saman", "penulis": "ayu utami", "kategori": "feminis / politik",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 2, "dipinjam_count": 33},
    {"judul": "ronggeng dukuh paruk", "penulis": "ahmad tohari", "kategori": "budaya / sosial",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 8, "dipinjam_count": 48},
    {"judul": "entrok", "penulis": "okky madasari", "kategori": "sosial / politik",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 4, "dipinjam_count": 29},
    {"judul": "sumur", "penulis": "eka kurniawan", "kategori": "realisme magis / romance gelap",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 6, "dipinjam_count": 21},
    {"judul": "ayat-ayat cinta", "penulis": "habiburrahman el shirazy", "kategori": "romance religi",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 1, "dipinjam_count": 76},
    {"judul": "hujan bulan juni", "penulis": "sapardi djoko damono", "kategori": "puisi / romance",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 10, "dipinjam_count": 15},
    {"judul": "supernova", "penulis": "dewi lestari", "kategori": "fiksi ilmiah / filosofis",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 7, "dipinjam_count": 55},
    {"judul": "cinta sepanjang amazon", "penulis": "mira w", "kategori": "romance drama",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 3, "dipinjam_count": 32},
    {"judul": "hujan", "penulis": "tere liye", "kategori": "distopia / sci-fi",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 9, "dipinjam_count": 49},
    {"judul": "perahu kertas", "penulis": "dewi lestari", "kategori": "romance / coming-of-age",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 5, "dipinjam_count": 60},
    {"judul": "negeri 5 menara", "penulis": "ahmad fuadi", "kategori": "inspiratif / pendidikan",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 2, "dipinjam_count": 70},
    {"judul": "amba", "penulis": "laksmi pamuntjak", "kategori": "sejarah / romance",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 8, "dipinjam_count": 25},
    {"judul": "orang-orang biasa", "penulis": "andrea hirata", "kategori": "komedi / petualangan",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 4, "dipinjam_count": 37},
    {"judul": "pulang", "penulis": "leila s. chudori", "kategori": "sejarah / diaspora",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 6, "dipinjam_count": 58},
    {"judul": "harry potter", "penulis": "j.k. rowling", "kategori": "fantasi",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 1, "dipinjam_count": 95},
    {"judul": "1984", "penulis": "george orwell", "kategori": "distopia",
     "status": "tersedia", "tanggal_pinjam": None, "peminjam": None, "stok": 10, "dipinjam_count": 84},
]

peminjam_data = {
    'dion': {
        'nim': '113', 
        'prodi': 'sistem informasi', 
        'buku_pinjam': [], 
        'denda': 0, 
        'pinjam_count': 5, 
        'riwayat': [
            {'judul': 'bumi manusia', 'tanggal_pinjam': '2025-10-01', 'tanggal_kembali': '2025-10-08', 'denda': 0},
            {'judul': 'laskar pelangi', 'tanggal_pinjam': '2025-09-15', 'tanggal_kembali': '2025-09-25', 'denda': 0},
            {'judul': 'cantik itu luka', 'tanggal_pinjam': '2025-08-20', 'tanggal_kembali': '2025-08-27', 'denda': 0},
            {'judul': 'ronggeng dukuh paruk', 'tanggal_pinjam': '2025-07-10', 'tanggal_kembali': '2025-07-18', 'denda': 0},
            {'judul': 'entrok', 'tanggal_pinjam': '2025-06-25', 'tanggal_kembali': '2025-07-02', 'denda': 0}
        ]
    },
    'riko': {
        'nim': '092', 
        'prodi': 'sistem informasi', 
        'buku_pinjam': [], 
        'denda': 0, 
        'pinjam_count': 7, 
        'riwayat': [
            {'judul': 'laut bercerita', 'tanggal_pinjam': '2025-11-01', 'tanggal_kembali': '2025-11-10', 'denda': 0},
            {'judul': 'saman', 'tanggal_pinjam': '2025-10-05', 'tanggal_kembali': '2025-10-12', 'denda': 0},
            {'judul': 'ronggeng dukuh paruk', 'tanggal_pinjam': '2025-09-10', 'tanggal_kembali': '2025-09-18', 'denda': 0},
            {'judul': 'entrok', 'tanggal_pinjam': '2025-08-25', 'tanggal_kembali': '2025-09-02', 'denda': 0},
            {'judul': 'sumur', 'tanggal_pinjam': '2025-07-20', 'tanggal_kembali': '2025-07-30', 'denda': 0},
            {'judul': 'ayat-ayat cinta', 'tanggal_pinjam': '2025-06-15', 'tanggal_kembali': '2025-06-22', 'denda': 0},
            {'judul': 'hujan bulan juni', 'tanggal_pinjam': '2025-05-10', 'tanggal_kembali': '2025-05-20', 'denda': 0}
        ]
    },
    'rian': {
        'nim': '045', 
        'prodi': 'teknik informatika', 
        'buku_pinjam': [], 
        'denda': 60000, 
        'pinjam_count': 3, 
        'riwayat': [
            {'judul': 'sumur', 'tanggal_pinjam': '2025-10-10', 'tanggal_kembali': '2025-10-20', 'denda': 30000},
            {'judul': 'ayat-ayat cinta', 'tanggal_pinjam': '2025-09-05', 'tanggal_kembali': '2025-09-12', 'denda': 0},
            {'judul': 'supernova', 'tanggal_pinjam': '2025-08-01', 'tanggal_kembali': '2025-08-11', 'denda': 30000}
        ]
    },
    'sari': {
        'nim': '112', 
        'prodi': 'manajemen', 
        'buku_pinjam': [], 
        'denda': 100000, 
        'pinjam_count': 9, 
        'riwayat': [
            {'judul': 'hujan bulan juni', 'tanggal_pinjam': '2025-11-05', 'tanggal_kembali': '2025-11-15', 'denda': 0},
            {'judul': 'supernova', 'tanggal_pinjam': '2025-10-15', 'tanggal_kembali': '2025-10-25', 'denda': 0},
            {'judul': 'cinta sepanjang amazon', 'tanggal_pinjam': '2025-09-20', 'tanggal_kembali': '2025-09-30', 'denda': 0},
            {'judul': 'hujan', 'tanggal_pinjam': '2025-08-30', 'tanggal_kembali': '2025-09-10', 'denda': 0},
            {'judul': 'perahu kertas', 'tanggal_pinjam': '2025-08-01', 'tanggal_kembali': '2025-08-12', 'denda': 30000},
            {'judul': 'negeri 5 menara', 'tanggal_pinjam': '2025-07-05', 'tanggal_kembali': '2025-07-15', 'denda': 20000},
            {'judul': 'amba', 'tanggal_pinjam': '2025-06-10', 'tanggal_kembali': '2025-06-20', 'denda': 10000},
            {'judul': 'orang-orang biasa', 'tanggal_pinjam': '2025-05-15', 'tanggal_kembali': '2025-05-25', 'denda': 10000},
            {'judul': 'pulang', 'tanggal_pinjam': '2025-04-20', 'tanggal_kembali': '2025-04-30', 'denda': 30000}
        ]
    },
    'budi': {
        'nim': '203', 
        'prodi': 'akuntansi', 
        'buku_pinjam': [], 
        'denda': 50000, 
        'pinjam_count': 2, 
        'riwayat': [
            {'judul': 'negeri 5 menara', 'tanggal_pinjam': '2025-10-20', 'tanggal_kembali': '2025-10-30', 'denda': 30000},
            {'judul': 'amba', 'tanggal_pinjam': '2025-09-25', 'tanggal_kembali': '2025-10-05', 'denda': 20000}
        ]
    }
}

admin = {
    'fio': 'fio018',
    'naya': 'naya062',
}

BATAS_PINJAM_HARI = 7
BATAS_PINJAM_BUKU = 5
DENDA_PER_HARI = 10000

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_screen():
    visual = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                 SISTEM PERPUSTAKAAN DIGITAL                  ║
    ║                 Manajemen Buku & Peminjaman                  ║
    ║              Selamat Datang Admin Perpustakaan               ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(visual)

def cek_buku_duplikat(judul):
    for buku in buku_list:
        if buku['judul'].lower() == judul.lower():
            return True
    return False

def cek_peminjam_duplikat(nama):
    for peminjam in peminjam_data.keys():
        if peminjam.lower() == nama.lower():
            return True
    return False

def laporan_statistik():
    clear_screen()
    print("\n" + "="*80)
    print("LAPORAN STATISTIK PERPUSTAKAAN".center(80))
    print("="*80)
    
    total_buku = len(buku_list)
    total_stok = sum(b['stok'] for b in buku_list)
    total_dipinjam_count = sum(b['dipinjam_count'] for b in buku_list)
    buku_tersedia = len([b for b in buku_list if b['stok'] > 0])
    buku_habis = len([b for b in buku_list if b['stok'] == 0])
    
    print("\nSTATISTIK BUKU:")
    print(f"   • Total Judul Buku        : {total_buku}")
    print(f"   • Total Stok Tersedia     : {total_stok}")
    print(f"   • Buku Tersedia           : {buku_tersedia}")
    print(f"   • Buku Stok Habis         : {buku_habis}")
    print(f"   • Total Peminjaman (all)  : {total_dipinjam_count}")
    
    if buku_list:
        buku_populer = max(buku_list, key=lambda x: x['dipinjam_count'])
        print(f"   • Buku Terpopuler         : {buku_populer['judul'].title()} ({buku_populer['dipinjam_count']}x)")
    
    total_anggota = len(peminjam_data)
    total_denda = sum(p.get('denda', 0) for p in peminjam_data.values())
    sedang_pinjam = sum(len(p.get('buku_pinjam', [])) for p in peminjam_data.values())
    
    print("\nSTATISTIK ANGGOTA:")
    print(f"   • Total Anggota           : {total_anggota}")
    print(f"   • Buku Sedang Dipinjam    : {sedang_pinjam}")
    print(f"   • Total Denda Terkumpul   : Rp{total_denda:,}")
    
    if peminjam_data:
        anggota_aktif = max(peminjam_data.items(), key=lambda x: x[1].get('pinjam_count', 0))
        print(f"Anggota Teraktif        : {anggota_aktif[0].title()} ({anggota_aktif[1]['pinjam_count']}x)")
    
    kategori_count = {}
    for buku in buku_list:
        kat = buku['kategori'].split('/')[0].strip()
        kategori_count[kat] = kategori_count.get(kat, 0) + 1
    
    print("\nSTATISTIK KATEGORI:")
    for kat, count in sorted(kategori_count.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{kat.title():<25} : {count} buku")
    
    prodi_count = {}
    for info in peminjam_data.values():
        prodi = info.get('prodi', 'Unknown')
        prodi_count[prodi] = prodi_count.get(prodi, 0) + info.get('pinjam_count', 0)
    
    if prodi_count:
        print("\nPRODI TERBANYAK MEMINJAM:")
        for prodi, count in sorted(prodi_count.items(), key=lambda x: x[1], reverse=True)[:3]:
            print(f"{prodi.title():<25} : {count}x")
    
    print("\n" + "="*80)
    input("\nTekan Enter untuk kembali ke menu.")

def menu_buku():
    clear_screen()
    while True:
        print("\n=== Kelola Buku ===")
        print("1. Daftar Buku")
        print("2. Cari Buku")
        print("3. Tambah Buku")
        print("4. Hapus Buku")
        print("5. kembali")
        p = input("Pilih: ").strip()
        
        if not p:
            print("Input tidak boleh kosong.")
            continue

        try:
            if p == "1": daftar_buku()
            elif p == "2": cari_buku()
            elif p == "3": tambah_buku()
            elif p == "4": hapus_buku()
            elif p == "5": break
            else:
                print("Pilihan tidak valid. Masukkan angka 1-5.")
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")
        
def daftar_buku():
    clear_screen()
    print("\n--- Daftar Buku ---")
    print(f"\n {'No.':<5} {'Judul':<30} {'Penulis':<30} {'Kategori':<35} {'Stok':<5} {'Dipinjam':<15}")
    print("-" * 120) 

    for i, buku in enumerate(buku_list, start=1):
        print(f"{i:<5} {buku['judul'].title():<30} {buku['penulis'].title():<30} {buku['kategori'].title():<35} {buku['stok']:<5} {buku['dipinjam_count']:<15}")

    while True:
        print("\nPilih opsi berikut:")
        print("1. Buku dengan stok terbanyak")
        print("2. Buku dengan stok terdikit")
        print("3. Buku yang sering dipinjam")
        print("4. Buku yang tidak sering dipinjam")
        print("5. Kembali ke menu utama")
        pilihan = input("Masukkan pilihan (1-5): ").strip()
        
        if pilihan == '1':
            buku_sorted = sorted(buku_list, key=lambda x: x['stok'], reverse=True)
            print("\n--- Buku dengan Stok Terbanyak ---")
        elif pilihan == '2':
            buku_sorted = sorted(buku_list, key=lambda x: x['stok'])
            print("\n--- Buku dengan Stok Terdikit ---")
        elif pilihan == '3':
            buku_sorted = sorted(buku_list, key=lambda x: x['dipinjam_count'], reverse=True)
            print("\n--- Buku yang Sering Dipinjam ---")
        elif pilihan == '4':
            buku_sorted = sorted(buku_list, key=lambda x: x['dipinjam_count'])
            print("\n--- Buku yang Tidak Sering Dipinjam ---")
        elif pilihan == '5':
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")
            continue

        if pilihan in ['1', '2', '3', '4']:
            print(f"\n {'No.':<5} {'Judul':<30} {'Penulis':<30} {'Kategori':<35} {'Stok':<5} {'Dipinjam':<15}")
            print("-" * 120)
            for i, buku in enumerate(buku_sorted, start=1):
                print(f"{i:<5} {buku['judul'].title():<30} {buku['penulis'].title():<30} {buku['kategori'].title():<35} {buku['stok']:<5} {buku['dipinjam_count']:<15}")

def cari_buku():
    clear_screen()
    while True:
        print("\n=== Cari Buku ===")
        print("1. Pencarian Sederhana (judul/penulis/kategori)")
        print("2. Pencarian Lanjutan (multi-filter)")
        print("3. Kembali")
        pilihan = input("Pilih metode pencarian (1-3): ").strip()
            
        if not pilihan:
            print("Input tidak boleh kosong.")
            continue
            
        if pilihan == "1":
            clear_screen()
            print("\n--- Daftar Semua Buku ---")
            print(f"\n {'No.':<5} {'Judul':<30} {'Penulis':<30} {'Kategori':<35} {'Stok':<5} {'Dipinjam':<10} {'Status':<10}")
            print("-" * 130)
            for i, buku in enumerate(buku_list, start=1):
                status = "Tersedia" if buku['status'] == 'tersedia' else "Dipinjam"
                print(f"{i:<5} {buku['judul'].title():<30} {buku['penulis'].title():<30} {buku['kategori'].title():<35} {buku['stok']:<5} {buku['dipinjam_count']:<10} {status:<10}")
                
            while True:
                cari = input("\nMasukkan judul atau penulis atau kategori yang dicari: ").lower().strip()
                    
                if not cari:
                    print("Input tidak boleh kosong.")
                    continue
                    
                print("\n--- Hasil Pencarian ---")
                print(f"\n {'No.':<5} {'Judul':<30} {'Penulis':<30} {'Kategori':<35} {'Stok':<5} {'Dipinjam':<10} {'Status':<10}")
                print("-" * 130)
                found = False
                count = 1
                for buku in buku_list:
                    if cari in buku['judul'].lower() or cari in buku['penulis'].lower() or cari in buku['kategori'].lower():
                        status = "Tersedia" if buku['status'] == 'tersedia' else "Dipinjam"
                        print(f"{count:<5} {buku['judul'].title():<30} {buku['penulis'].title():<30} {buku['kategori'].title():<35} {buku['stok']:<5} {buku['dipinjam_count']:<10} {status:<10}")
                        count += 1
                        found = True
                if not found:
                    print("Buku tidak ditemukan.")
                    
                input("\nTekan Enter untuk kembali...")
                break
                
        elif pilihan == "2":
            clear_screen()
            print("\n--- Pencarian Filter ---")
            print("Kosongkan jika tidak ingin menggunakan filter tertentu.\n")
                
            kategori = input("Filter kategori (contoh: sejarah, romance, fantasi): ").lower().strip()
                
            min_stok = None
            while True:
                stok_input = input("Stok minimal (kosongkan untuk skip): ").strip()
                if not stok_input:
                    break
                if stok_input.isdigit():
                    min_stok = int(stok_input)
                    break
                else:
                    print("Masukkan angka yang valid atau kosongkan.")
                
            penulis = input("Filter penulis (contoh: andrea hirata): ").lower().strip()
                
            print("\nFilter status:")
            print("1. Tersedia")
            print("2. Dipinjam")
            print("3. Semua (skip filter)")
            status_pilihan = input("Pilih (1-3): ").strip()
            status_filter = None
            if status_pilihan == "1":
                status_filter = "tersedia"
            elif status_pilihan == "2":
                status_filter = "dipinjam"
                
            hasil = buku_list[:]
                
            if kategori:
                hasil = [b for b in hasil if kategori in b['kategori'].lower()]
                
            if min_stok is not None:
                hasil = [b for b in hasil if b['stok'] >= min_stok]
                
            if penulis:
                hasil = [b for b in hasil if penulis in b['penulis'].lower()]
                
            if status_filter:
                hasil = [b for b in hasil if b['status'] == status_filter]
                
            clear_screen()
            print("\n--- Hasil Pencarian Lanjutan ---")
            if not hasil:
                print("Tidak ada buku yang sesuai dengan kriteria pencarian.")
            else:
                print(f"\nDitemukan {len(hasil)} buku:")
                print(f"\n {'No.':<5} {'Judul':<30} {'Penulis':<30} {'Kategori':<35} {'Stok':<5} {'Dipinjam':<10} {'Status':<10}")
                print("-" * 130)
                for i, buku in enumerate(hasil, start=1):
                    status = "Tersedia" if buku['status'] == 'tersedia' else "Dipinjam"
                    print(f"{i:<5} {buku['judul'].title():<30} {buku['penulis'].title():<30} {buku['kategori'].title():<35} {buku['stok']:<5} {buku['dipinjam_count']:<10} {status:<10}")
                
            input("\nTekan Enter untuk kembali...")
            break
                
        elif pilihan == "3":
            print("Kembali ke menu sebelumnya.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-3.")  

def tambah_buku():
    clear_screen()
    while True:
        pilihan = input("ketik 'buku' untuk menambahkan buku baru atau 'stok' untuk menambahkan stok buku: ").lower().strip()
        
        if not pilihan:
            print("Input tidak boleh kosong.")
            continue
            
        if pilihan == 'buku':
            print("\n--- Tambah Buku Baru ---")
            while True:
                judul = input("Masukkan judul buku: ").lower().strip()
                
                if not judul:
                    print("Judul tidak boleh kosong.")
                    continue
                    
                if not judul.replace(" ", "").isalpha():
                    print("Judul harus berupa huruf saja.")
                    continue
                    
                if cek_buku_duplikat(judul):
                    print(f"Buku '{judul.title()}' sudah ada dalam sistem.")
                    continue
                    
                break
            
            while True:
                penulis = input("Masukkan penulis buku: ").lower().strip()
                
                if not penulis:
                    print("Penulis tidak boleh kosong.")
                    continue
                    
                if not penulis.replace(" ", "").isalpha():
                    print("Penulis harus berupa huruf saja.")
                    continue
                break
            
            while True:
                kategori = input("Masukkan kategori buku: ").lower().strip()
                
                if not kategori:
                    print("Kategori tidak boleh kosong.")
                    continue
                    
                if not kategori.replace(" ", "").isalpha():
                    print("Kategori harus berupa huruf saja.")
                    continue
                break
            
            while True:
                stok = input("Masukkan stok buku: ").strip()
                
                if not stok:
                    print("Stok tidak boleh kosong.")
                    continue
                    
                if not stok.isdigit() or int(stok) < 0:
                    print("Stok harus berupa angka positif.")
                    continue
                stok = int(stok)
                break
            
            buku_baru = {
                "judul": judul,
                "penulis": penulis,
                "kategori": kategori,
                "status": "tersedia",
                "tanggal_pinjam": None,
                "peminjam": None,
                "stok": stok,
                "dipinjam_count": 0
            }
            buku_list.append(buku_baru)
            print(f"Buku '{judul.title()}' berhasil ditambahkan.")
            break
    
        elif pilihan == 'stok':
            for i, buku in enumerate(buku_list, start=1):
                print(f"{i:<5} {buku['judul'].title():<30} {buku['penulis'].title():<30} {buku['kategori'].title():<35} {buku['stok']:<5} {buku['dipinjam_count']:<15}")
    
            while True:
                try:
                    nomor = int(input("Masukkan nomor buku yang ingin ditambahkan stoknya (atau 0 untuk batal): ").strip())
                    if nomor == 0:
                        print("Penambahan stok dibatalkan.")
                        return
                    if 1 <= nomor <= len(buku_list):
                        buku = buku_list[nomor - 1]  
                        while True:
                            tambahan = input(f"Masukkan jumlah stok yang ingin ditambahkan untuk '{buku['judul'].title()}': ").strip()
                            
                            if not tambahan:
                                print("Input tidak boleh kosong.")
                                continue
                                
                            if tambahan.isdigit() and int(tambahan) > 0:
                                tambahan = int(tambahan)
                                buku['stok'] += tambahan
                                print(f"Stok buku '{buku['judul'].title()}' berhasil ditambahkan. Stok sekarang: {buku['stok']}.")
                                return
                            else:
                                print("Masukkan angka positif yang valid.")
                    else:
                        print("Nomor tidak valid. Masukkan nomor antara 1 sampai", len(buku_list))
                except ValueError:
                    print("Masukkan nomor yang valid (angka).")
        else:
            print("Pilihan tidak valid. Silakan ketik 'buku' atau 'stok'.")
   
def hapus_buku():
    clear_screen()
    while True:
        pilihan = input("ketik 'buku' untuk menghapus buku atau 'stok' untuk mengurangi stok buku: ").lower().strip()
        
        if not pilihan:
            print("Input tidak boleh kosong.")
            continue
            
        if pilihan == 'buku':
            print("\n--- Daftar Buku ---")
            print(f"\n {'No.':<5} {'Judul':<30} {'Penulis':<30} {'Kategori':<35} {'Stok':<5} {'Dipinjam':<15}")
            print("-" * 120)  
            for i, buku in enumerate(buku_list, start=1):
                print(f"{i:<5} {buku['judul'].title():<30} {buku['penulis'].title():<30} {buku['kategori'].title():<35} {buku['stok']:<5} {buku['dipinjam_count']:<15}")
            
            while True:
                try:
                    nomor = int(input("Masukkan nomor buku yang ingin dihapus (atau 0 untuk batal): ").strip())
                    if nomor == 0:
                        print("Penghapusan dibatalkan.")
                        return
                    if 1 <= nomor <= len(buku_list):
                        buku = buku_list[nomor - 1]  
                        print(f"Yakin hapus buku '{buku['judul'].title()}'? (y/n): ", end="")
                        konfirmasi = input().lower().strip()
                        if konfirmasi == 'y' or konfirmasi == 'ya' or konfirmasi == 'iya' or konfirmasi == 'iy':
                            judul_dihapus = buku['judul']  
                            buku_list.remove(buku)
                            print(f"Buku '{judul_dihapus.title()}' berhasil dihapus.")
                            return
                        else:
                            print("Penghapusan dibatalkan.")
                            return
                    else:
                        print("Nomor tidak valid. Masukkan nomor antara 1 sampai", len(buku_list))
                except ValueError:
                    print("Masukkan nomor yang valid (angka).")
        
        elif pilihan == 'stok':
            print("\n--- Daftar Buku ---")
            print(f"\n {'No.':<5} {'Judul':<30} {'Penulis':<30} {'Kategori':<35} {'Stok':<5} {'Dipinjam':<15}")
            print("-" * 120)  
            for i, buku in enumerate(buku_list, start=1):
                print(f"{i:<5} {buku['judul'].title():<30} {buku['penulis'].title():<30} {buku['kategori'].title():<35} {buku['stok']:<5} {buku['dipinjam_count']:<15}")
            
            while True:
                try:
                    nomor = int(input("Masukkan nomor buku yang ingin dikurangi stoknya (atau 0 untuk batal): ").strip())
                    if nomor == 0:
                        print("Pengurangan stok dibatalkan.")
                        return
                    if 1 <= nomor <= len(buku_list):
                        buku = buku_list[nomor - 1]  
                        while True:
                            pengurangan = input(f"Masukkan jumlah stok yang ingin dikurangi untuk '{buku['judul'].title()}' (stok saat ini: {buku['stok']}): ").strip()
                            
                            if not pengurangan:
                                print("Input tidak boleh kosong.")
                                continue
                                
                            if pengurangan.isdigit() and int(pengurangan) > 0:
                                pengurangan = int(pengurangan)
                                if pengurangan > buku['stok']:
                                    print(f"Jumlah pengurangan ({pengurangan}) melebihi stok saat ini ({buku['stok']}).")
                                    continue
                                buku['stok'] -= pengurangan
                                print(f"Stok buku '{buku['judul'].title()}' berhasil dikurangi. Stok sekarang: {buku['stok']}.")
                                return
                            else:
                                print("Masukkan angka positif yang valid.")
                    else:
                        print("Nomor tidak valid. Masukkan nomor antara 1 sampai", len(buku_list))
                except ValueError:
                    print("Masukkan nomor yang valid (angka).")
        else:
            print("Pilihan tidak valid. Silakan ketik 'buku' atau 'stok'.")

def menu_anggota():
    clear_screen()
    while True:
        print("\n=== Kelola Data Peminjam ===")
        print("1. Daftar anggota")
        print("2. Cari anggota")
        print("3. Tambah anggota")
        print("4. Hapus anggota")
        print("5. Kembali")
        p = input("Pilih: ").strip()

        if not p:
            print("Input tidak boleh kosong.")
            continue

        try:    
            if p == "1": daftar_peminjam()
            elif p == "2": cari_peminjam()
            elif p == "3": tambah_peminjam()
            elif p == "4": hapus_peminjam()
            elif p == "5": break
            else:
                print("Pilihan tidak valid. Masukkan angka 1-5.")
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")           

def daftar_peminjam():
    clear_screen()
    print("\n--- Daftar Anggota Peminjam ---")
    if not peminjam_data:
        print("Belum ada anggota peminjam.")
        return
    print(f"\n {'No.':<5} {'Nama':<15} {'NIM':<15} {'Prodi':<25} {'Buku Dipinjam':<40} {'Denda':<10} {'Jumlah Pinjam':<15}")
    print("-" * 140)  
    for i, (nama, info) in enumerate(peminjam_data.items(), start=1):
        buku_dipinjam = info.get('buku_pinjam', [])
        buku_str = ', '.join(buku_dipinjam) if buku_dipinjam else 'None'
        nim_str = info.get('nim', 'None')
        prodi_str = info.get('prodi', 'None')
        denda_str = str(info.get('denda', 'None'))
        pinjam_count_str = str(info.get('pinjam_count', 'None'))
        print(f"{i:<5} {nama.title():<15} {nim_str:<15} {prodi_str:<25} {buku_str:<40} {denda_str:<10} {pinjam_count_str:<15}")
        
    total_denda = 0
    for info in peminjam_data.values():
        denda = info.get('denda', 0)
        if isinstance(denda, (int, float)):
            total_denda += denda
    print(f"\nTotal Denda: Rp.{total_denda}")
    
    while True:
        print("\nPilih opsi berikut:")
        print("1. Peminjam yang paling sering pinjam")
        print("2. Peminjam yang tidak sering pinjam")
        print("3. Kembali ke menu utama")
        pilihan = input("Masukkan pilihan (1-3): ").strip()
        
        if pilihan == '1':
            peminjam_sorted = sorted(peminjam_data.items(), key=lambda x: x[1]['pinjam_count'], reverse=True)
            print("\n--- Peminjam yang Paling Sering Pinjam ---")
        elif pilihan == '2':
            peminjam_sorted = sorted(peminjam_data.items(), key=lambda x: x[1]['pinjam_count'])
            print("\n--- Peminjam yang Tidak Sering Pinjam ---")
        elif pilihan == '3':
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-3.")
            continue
        
        if pilihan in ['1', '2']:
            print(f"\n {'No.':<5} {'Nama':<15} {'NIM':<15} {'Prodi':<25} {'Buku Dipinjam':<40} {'Denda':<10} {'Jumlah Pinjam':<15}")
            print("-" * 140)
            for i, (nama, info) in enumerate(peminjam_sorted, start=1):
                buku_dipinjam = info.get('buku_pinjam', [])
                buku_str = ', '.join(buku_dipinjam) if buku_dipinjam else 'None'
                nim_str = info.get('nim', 'None')
                prodi_str = info.get('prodi', 'None')
                denda_str = str(info.get('denda', 'None'))
                pinjam_count_str = str(info.get('pinjam_count', 'None'))
                print(f"{i:<5} {nama.title():<15} {nim_str:<15} {prodi_str:<25} {buku_str:<40} {denda_str:<10} {pinjam_count_str:<15}")
      
def cari_peminjam():
    clear_screen()
    print("\n--- Daftar Anggota Peminjam ---")
    for i, (nama, info) in enumerate(peminjam_data.items(), start=1):
        buku_dipinjam = info.get('buku_pinjam', [])
        buku_str = ', '.join(buku_dipinjam) if buku_dipinjam else 'None'
        print(f"{i:<5} {nama.title():<15} {info['nim']:<15} {info['prodi']:<25}")
    
    while True:
        cari = input("Masukkan nama atau NIM atau prodi yang dicari (atau 0 untuk kembali): ").lower().strip()
        
        if cari == '0':
            print("Kembali ke menu sebelumnya.")
            return  
        
        if not cari:
            print("Input tidak boleh kosong.")
            continue
        
        print("\n--- Hasil Pencarian Anggota ---")
        found = False
        for nama, info in peminjam_data.items():
            if cari in nama.lower() or cari in info['nim'].lower() or cari in info['prodi'].lower():
                buku_str = ', '.join(info.get('buku_pinjam', [])) if info.get('buku_pinjam') else 'None'
                denda_str = f"Rp{info.get('denda', 0)}"
                pinjam_count = info.get('pinjam_count', 0)
                print(f"Nama: {nama.title()} - NIM: {info['nim']} - Prodi: {info['prodi']} - Buku Dipinjam: {buku_str} - Total Pinjam: {pinjam_count} - Denda: {denda_str}")
                found = True
        if not found:
            print("Anggota tidak ditemukan.")
        
        input("\nTekan Enter untuk cari lagi...")
        
def tambah_peminjam():
    clear_screen()
    print("\n--- Tambah Anggota Peminjam ---")
    
    prodi_dict = {
        "1": "Teknik Informatika",
        "2": "Sistem Informasi",
        "3": "Teknik Elektro",
        "4": "Teknik Mesin",
        "5": "Teknik Sipil",
        "6": "Akuntansi",
        "7": "Manajemen",
        "8": "Psikologi",
        "9": "Hukum",
        "10": "Ilmu Komunikasi"    
    }
    
    while True:
        nama = input("Masukkan nama anggota: ").lower().strip()
        
        if not nama:
            print("Nama tidak boleh kosong.")
            continue
            
        if not nama.replace(" ", "").isalpha():
            print("Nama harus berupa huruf saja.")
            continue
            
        if cek_peminjam_duplikat(nama):
            print(f"Anggota '{nama.title()}' sudah terdaftar dalam sistem.")
            continue
            
        break
    
    while True:
        nim = input("Masukkan NIM anggota: ").strip()
        
        if not nim:
            print("NIM tidak boleh kosong.")
            continue
            
        if not nim.isdigit():
            print("NIM harus berupa angka saja.")
            continue
            
        if len(nim) < 3:
            print("NIM minimal 3 digit.")
            continue
            
        break
    
    while True:
        print("Silahkan pilih prodi anda:")
        print("1. Teknik Informatika")
        print("2. Sistem Informasi")
        print("3. Teknik Elektro")
        print("4. Teknik Mesin")
        print("5. Teknik Sipil")
        print("6. Akuntansi")
        print("7. Manajemen")
        print("8. Psikologi")
        print("9. Hukum")
        print("10. Ilmu Komunikasi")
        prodi_input = input("Masukkan prodi anggota (1-10): ").strip()
        
        if not prodi_input:
            print("Prodi tidak boleh kosong.")
            continue
            
        if not prodi_input.isdigit():
            print("Prodi harus berupa angka (1-10).")
            continue
            
        if prodi_input not in prodi_dict:
            print("Prodi harus antara 1-10.")
            continue
            
        prodi = prodi_dict[prodi_input]
        break
    
    peminjam_data[nama] = {
        "nim": nim,
        "prodi": prodi,  
        "buku_pinjam": [],
        "denda": 0,
        "pinjam_count": 0,
        "riwayat": []
    }
    print(f"Anggota '{nama.title()}' berhasil ditambahkan.")

def hapus_peminjam():
    clear_screen()
    print("\n--- Daftar Anggota Peminjam ---")
    for i, (nama, info) in enumerate(peminjam_data.items(), start=1):
        print(f"{i:<5} {nama.title():<15} {info['nim']:<15} {info['prodi']:<25}")
      
    while True:
        nama = input("Masukkan nama anggota yang ingin dihapus (atau ketik 'batal' untuk membatalkan): ").lower().strip()
        
        if not nama:
            print("Input tidak boleh kosong.")
            continue
            
        if nama == 'batal':
            print("Penghapusan dibatalkan.")
            return
        if nama in peminjam_data:
            print(f"Yakin hapus anggota '{nama.title()}'? (y/n): ", end="")
            konfirmasi = input().lower().strip()
            if konfirmasi == 'y' or konfirmasi == 'ya' or konfirmasi == 'iya' or konfirmasi == 'iy':
                del peminjam_data[nama]
                print(f"Anggota '{nama.title()}' berhasil dihapus.")
                return
            else:
                print("Penghapusan dibatalkan.")
                return
        else:
            print("Anggota tidak ditemukan. Silakan coba lagi.")

def menu_peminjaman():
    clear_screen()
    while True:
        print("\n=== Kelola Peminjaman ===")
        print("1. Pinjam Buku")
        print("2. Pengembalian Buku")
        print("3. Lihat Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Kembali")
        p = input("Pilih: ").strip()      
        
        if not p:
            print("Input tidak boleh kosong.")
            continue
        
        try:
            if p == "1": pinjam_buku()
            elif p == "2": kembalikan_buku()
            elif p == "3": lihat_peminjaman()
            elif p == "4": hapus_peminjaman()
            elif p == "5": break
            else:
                print("Pilihan tidak valid. Masukkan angka 1-5.")
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")
        
def pinjam_buku():
    clear_screen()
    if peminjam_data:
        print("Daftar Peminjam:")
        for i, (nama, info) in enumerate(peminjam_data.items(), start=1):
            buku_aktif = len(info.get('buku_pinjam', []))
            print(f"{i:<5} {nama.title():<15} (Sedang pinjam: {buku_aktif}/{BATAS_PINJAM_BUKU})")
    else:
        print("Belum ada peminjam terdaftar.")
    
    print("\n--- Pinjam Buku ---")
    while True:
        nama = input("Masukkan nama peminjam: ").lower().strip()
        
        if not nama:
            print("Nama tidak boleh kosong.")
            continue
            
        if not nama.replace(" ", "").isalpha():
            print("Nama harus berupa huruf saja.")
            continue
        if nama not in peminjam_data:
            print("Peminjam tidak ditemukan. Silakan tambah anggota terlebih dahulu.")
            while True:
                pilih = input("Apakah Anda ingin menambahkan anggota baru? (y/n): ").lower().strip()
                if pilih in ['y', 'ya', 'iya', 'iy']:
                    tambah_peminjam()
                    break  
                elif pilih in ['n', 'no', 'batal', 'enggak', 'gak']:
                    print("Baik, silakan kembali lagi.")
                    return
                else:
                    print("Jawaban tidak valid. Jawab dengan 'y' (ya/iya/iy) atau 'n' (no/batal/enggak/gak).")
            continue
        break   
    
    jumlah_pinjam_aktif = len(peminjam_data[nama].get('buku_pinjam', []))
    if jumlah_pinjam_aktif >= BATAS_PINJAM_BUKU:
        print(f"\nBATAS PEMINJAMAN TERCAPAI!")
        print(f"'{nama.title()}' sudah meminjam {jumlah_pinjam_aktif} buku.")
        print(f"Maksimal peminjaman adalah {BATAS_PINJAM_BUKU} buku sekaligus.")
        print("Silakan kembalikan buku terlebih dahulu.")
        input("\nTekan Enter untuk kembali...")
        return
    
    while True:
        print(f"\nBuku tersedia (Anda bisa pinjam {BATAS_PINJAM_BUKU - jumlah_pinjam_aktif} buku lagi):")
        buku_tersedia = [buku for buku in buku_list if buku['stok'] > 0]
        if not buku_tersedia:
            print("Tidak ada buku tersedia.")
            return
        for i, buku in enumerate(buku_tersedia, start=1):
            print(f"{i}. {buku['judul'].title()} - Stok: {buku['stok']}")
        
        try:
            nomor = int(input("Masukkan nomor buku yang ingin dipinjam: ").strip())
            if 1 <= nomor <= len(buku_tersedia):
                buku = buku_tersedia[nomor - 1]
                if buku['stok'] > 0:
                    buku['stok'] -= 1
                    buku['status'] = 'dipinjam'
                    buku['tanggal_pinjam'] = datetime.now()
                    buku['peminjam'] = nama
                    
                    if nama not in peminjam_data:
                        peminjam_data[nama] = {'buku_pinjam': [], 'riwayat': []}
                    if 'buku_pinjam' not in peminjam_data[nama]:
                        peminjam_data[nama]['buku_pinjam'] = []
                    if 'riwayat' not in peminjam_data[nama]:
                        peminjam_data[nama]['riwayat'] = []
                    
                    peminjam_data[nama]['buku_pinjam'].append(buku['judul'])
                    
                    peminjam_data[nama]['pinjam_count'] = len(peminjam_data[nama]['buku_pinjam'])
                    
                    if buku['dipinjam_count'] is None:
                        buku['dipinjam_count'] = 0
                    buku['dipinjam_count'] += 1
                    
                    print(f"Buku '{buku['judul'].title()}' berhasil dipinjam oleh '{nama.title()}'.")
                    print(f"Jumlah pinjam '{nama.title()}' sekarang: {peminjam_data[nama]['pinjam_count']}")
                    
                    jumlah_pinjam_aktif = len(peminjam_data[nama]['buku_pinjam'])
                    
                    if jumlah_pinjam_aktif >= BATAS_PINJAM_BUKU:
                        print(f"\nAnda sudah mencapai batas maksimal ({BATAS_PINJAM_BUKU} buku).")
                        print("Tidak bisa meminjam lagi sampai ada yang dikembalikan.")
                        input("\nTekan Enter untuk kembali...")
                        return
                    
                    while True:
                        lanjut = input(f"\nApakah Anda ingin meminjam buku lagi? (y/n): ").lower().strip()
                        if lanjut in ['y', 'ya', 'iya', 'iy']:
                            break
                        elif lanjut in ['n', 'no', 'batal', 'enggak', 'gak']:
                            print("Terima kasih telah meminjam buku.")
                            return
                        else:
                            print("Jawaban tidak valid. Jawab dengan 'y' (ya/iya/iy) atau 'n' (no/batal/enggak/gak).")
                else:
                    print("Stok buku habis.")
            else:
                print("Nomor buku tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

def kembalikan_buku():
    clear_screen()
    print("\n--- Daftar Anggota Peminjam ---")
    if peminjam_data:
        for i, (nama, info) in enumerate(peminjam_data.items(), start=1):
            buku_pinjam = info.get('buku_pinjam', [])
            print(f"{i:<5} {nama.title():<15} (Buku dipinjam: {len(buku_pinjam)})")
    else:
        print("Belum ada peminjam terdaftar.")
        return
    
    print("\n--- Pengembalian Buku ---")
    while True:
        nama = input("Masukkan nama peminjam: ").lower().strip()
        
        if not nama:
            print("Nama tidak boleh kosong.")
            continue
            
        if not nama.replace(" ", "").isalpha():
            print("Nama harus berupa huruf saja.")
            continue
        if nama not in peminjam_data:
            print("Peminjam tidak ditemukan.")
            continue
        if not peminjam_data[nama].get('buku_pinjam', []):
            print("Peminjam tidak memiliki buku yang dipinjam.")
            continue
        break
    
    print("Buku yang dipinjam:")
    for i, judul in enumerate(peminjam_data[nama]['buku_pinjam'], start=1):
        print(f"{i}. {judul.title()}")
    
    while True:
        nomor_input = input("Masukkan nomor buku yang ingin dikembalikan: ").strip()
        if not nomor_input:
            print("Input tidak boleh kosong. Masukkan nomor buku.")
            continue
        if not nomor_input.isdigit():
            print("Input harus berupa angka. Masukkan nomor buku yang valid.")
            continue
        nomor = int(nomor_input)
        if 1 <= nomor <= len(peminjam_data[nama]['buku_pinjam']):
            judul_kembali = peminjam_data[nama]['buku_pinjam'][nomor - 1]
            
            buku_ditemukan = None
            for buku in buku_list:
                if buku['judul'] == judul_kembali and buku['peminjam'] == nama:
                    buku_ditemukan = buku
                    break
            
            if not buku_ditemukan:
                print("Buku tidak ditemukan dalam daftar global atau tidak dipinjam oleh peminjam ini.")
                continue
            
            print(f"\nDetail buku yang dipilih: {judul_kembali.title()}")
            if buku_ditemukan['tanggal_pinjam']:
                print(f"Tanggal pinjam: {buku_ditemukan['tanggal_pinjam'].strftime('%Y-%m-%d')}")
            while True:
                konfirmasi = input("Apakah Anda yakin ingin mengembalikan buku ini? (y/n): ").strip().lower()
                if konfirmasi in ['y', 'ya', 'iya', 'iy']:
                    break  
                elif konfirmasi in ['n', 'no', 'batal', 'enggak', 'gak']:
                    print("Pengembalian dibatalkan.")
                    return
                else:
                    print("Jawaban tidak valid. Jawab dengan 'y' (ya/iya/iy) atau 'n' (no/batal/enggak/gak).")
            
            if not buku_ditemukan['tanggal_pinjam']:
                print("Data tanggal pinjam tidak ditemukan. Mengembalikan tanpa denda.")
                buku_ditemukan['stok'] += 1
                buku_ditemukan['status'] = 'tersedia'
                buku_ditemukan['peminjam'] = None
                buku_ditemukan['tanggal_pinjam'] = None
                peminjam_data[nama]['buku_pinjam'].pop(nomor - 1)
                break
            
            print("\nPilih metode input tanggal pengembalian:")
            print("1. Otomatis (tanggal hari ini)")
            print("2. Manual (format YYYY-MM-DD)")
            while True:
                metode = input("Pilih: ").strip()
                
                if not metode:
                    print("Input tidak boleh kosong.")
                    continue

                if metode == "1":
                    tanggal_kembali = datetime.now()
                elif metode == "2":
                    tgl_str = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ").strip()
                    try:
                        tanggal_kembali = datetime.strptime(tgl_str, "%Y-%m-%d")
                    except ValueError:
                        print("Format tanggal tidak valid. Gunakan YYYY-MM-DD.")
                        continue  
                else:
                    print("Pilihan tidak valid.") 
                    continue
                break

            if tanggal_kembali.date() < buku_ditemukan['tanggal_pinjam'].date():
                print("Tanggal pengembalian tidak boleh sebelum tanggal pinjam.")
                continue 

            tanggal_pinjam_dt = buku_ditemukan['tanggal_pinjam']

            hari_terlambat = (tanggal_kembali.date() - tanggal_pinjam_dt.date()).days
            denda = max(0, hari_terlambat - BATAS_PINJAM_HARI) * DENDA_PER_HARI

            buku_ditemukan['stok'] += 1
            buku_ditemukan['status'] = 'tersedia'
            buku_ditemukan['tanggal_pinjam'] = None
            buku_ditemukan['peminjam'] = None
            peminjam_data[nama]['buku_pinjam'].pop(nomor - 1)

            if 'riwayat' not in peminjam_data[nama]:
                peminjam_data[nama]['riwayat'] = []
            peminjam_data[nama]['riwayat'].append({
                'judul': judul_kembali,
                'tanggal_pinjam': tanggal_pinjam_dt.strftime('%Y-%m-%d'),
                'tanggal_kembali': tanggal_kembali.strftime('%Y-%m-%d'),
                'denda': denda
            })

            if denda > 0:
                peminjam_data[nama]['denda'] = peminjam_data[nama].get('denda', 0) + denda
                print(f"Buku dikembalikan dengan denda Rp{denda}.")
            else:
                print("Buku dikembalikan tanpa denda.")
            break
        else:
            print("Nomor tidak valid.")
            continue
  
def lihat_peminjaman():
    clear_screen()
    print("\n--- Daftar Anggota Peminjam ---")
    for i, (nama, info) in enumerate(peminjam_data.items(), start=1):
        print(f"{i:<5} {nama.title():<15} {info['nim']:<15} {info['prodi']:<25}")
        
    print("\n--- Lihat Peminjaman ---")
    while True:
        nama = input("Masukkan nama peminjam: ").lower().strip()
        
        if not nama:
            print("Input tidak boleh kosong.")
        if not nama.replace(" ", "").isalpha():
            print("Nama harus berupa huruf saja.")
            continue
        break
        
    if nama not in peminjam_data:
        print("Peminjam tidak ditemukan.")
        return
    info = peminjam_data[nama]
    print(f"Nama: {nama.title()}")
    print(f"NIM: {info['nim']}")
    print(f"Prodi: {info['prodi']}")
    print(f"Buku Dipinjam: {', '.join(info['buku_pinjam']) if info['buku_pinjam'] else 'None'}")
    print(f"Denda: Rp{info['denda']}")
    
def riwayat_peminjaman():
    clear_screen()
    print("\n=== Riwayat Peminjaman ===")
    
    if not peminjam_data:
        print("Belum ada data peminjam.")
        input("\nTekan Enter untuk kembali.")
        return
    
    print("\nDaftar Anggota:")
    for i, (nama, info) in enumerate(peminjam_data.items(), start=1):
        print(f"{i:<5} {nama.title():<15} {info['nim']:<15}")
    
    while True:
        nama = input("\nMasukkan nama peminjam (atau 'semua' untuk melihat semua riwayat, atau 0 untuk kembali): ").lower().strip()
        
        if nama == '0':
            print("Kembali ke menu sebelumnya.")
            return
        
        if not nama:
            print("Input tidak boleh kosong.")
            continue
        
        clear_screen()
        if nama == "semua":
            print("\n" + "="*100)
            print("RIWAYAT PEMINJAMAN SEMUA ANGGOTA".center(100))
            print("="*100)
            
            total_riwayat = 0
            for nama_peminjam, info in peminjam_data.items():
                riwayat = info.get('riwayat', [])
                if riwayat:
                    print(f"\n{nama_peminjam.title()} (NIM: {info['nim']})")
                    print(f"   {'No.':<5} {'Judul Buku':<30} {'Tgl Pinjam':<15} {'Tgl Kembali':<15} {'Denda':<15}")
                    print("   " + "-"*80)
                    for i, r in enumerate(riwayat, start=1):
                        print(f"   {i:<5} {r['judul'].title():<30} {r['tanggal_pinjam']:<15} {r['tanggal_kembali']:<15} Rp{r['denda']:<14,}")
                    total_riwayat += len(riwayat)
            
            if total_riwayat == 0:
                print("\nBelum ada riwayat peminjaman.")
            else:
                print(f"\n{'='*100}")
                print(f"Total Riwayat: {total_riwayat} transaksi")
            
        else:
            if nama not in peminjam_data:
                print("Peminjam tidak ditemukan.")
                input("\nTekan Enter untuk kembali.")
                continue
            
            info = peminjam_data[nama]
            riwayat = info.get('riwayat', [])
            
            print("\n" + "="*100)
            print(f"RIWAYAT PEMINJAMAN - {nama.title()}".center(100))
            print("="*100)
            print(f"\nNama  : {nama.title()}")
            print(f"NIM   : {info['nim']}")
            print(f"Prodi : {info['prodi']}")
            print(f"Total Peminjaman : {len(riwayat)}x")
            
            if not riwayat:
                print("\nBelum ada riwayat peminjaman.")
            else:
                print(f"\n{'No.':<5} {'Judul Buku':<35} {'Tgl Pinjam':<15} {'Tgl Kembali':<15} {'Denda':<15}")
                print("-"*85)
                total_denda_riwayat = 0
                for i, r in enumerate(riwayat, start=1):
                    print(f"{i:<5} {r['judul'].title():<35} {r['tanggal_pinjam']:<15} {r['tanggal_kembali']:<15} Rp{r['denda']:<14,}")
                    total_denda_riwayat += r['denda']
                print("-"*85)
                print(f"{'TOTAL DENDA DARI RIWAYAT':<70} Rp{total_denda_riwayat:,}")
        
        input("\nTekan Enter untuk kembali.")
        break 
   
def hapus_peminjaman():
    clear_screen()
    print("\n--- Daftar Anggota Peminjam ---")
    if peminjam_data:
        for i, (nama, info) in enumerate(peminjam_data.items(), start=1):
            nim_str = str(info.get('nim', 'None'))  
            prodi_str = str(info.get('prodi', 'None'))  
            print(f"{i:<5} {nama.title():<15} {nim_str:<15} {prodi_str:<25}")
    else:
        print("Belum ada peminjam terdaftar.")
        return
    
    print("\n--- Hapus Anggota Peminjam ---")
    while True:
        nama = input("Masukkan nama peminjam yang ingin dihapus: ").lower().strip()
        
        if not nama:
            print("Input tidak boleh kosong.")
        if not nama.replace(" ", "").isalpha():
            print("Nama harus berupa huruf saja.")
            continue
        break
            
    if nama not in peminjam_data:
        print("Peminjam tidak ditemukan.")
        return
    
    info = peminjam_data[nama]
    buku_pinjam = info.get('buku_pinjam', [])
    denda = info.get('denda', 0)
    nim = info.get('nim', 'None')
    prodi = info.get('prodi', 'None')
    print(f"Nama: {nama.title()}")
    print(f"NIM: {nim}")
    print(f"Prodi: {prodi}")
    print(f"Buku dipinjam: {', '.join(buku_pinjam) if buku_pinjam else 'None'}")
    print(f"Denda: Rp{denda}")
    
    while True:
        konfirmasi = input("Apakah Anda yakin ingin menghapus anggota ini? (y/n): ").strip().lower()
        if konfirmasi in ['y', 'ya', 'iya', 'iy']:
            break  
        elif konfirmasi in ['n', 'no', 'batal', 'enggak', 'gak']:
            print("Penghapusan dibatalkan.")
            return
        else:
            print("Jawaban tidak valid. Jawab dengan 'y' (ya/iya/iy) atau 'n' (no/batal/enggak/gak).")
    
    for judul in buku_pinjam:
        for buku in buku_list:  
            if buku['judul'] == judul and buku['peminjam'] == nama:
                buku['stok'] += 1
                buku['status'] = 'tersedia'
                buku['tanggal_pinjam'] = None
                buku['peminjam'] = None
                break
    
    del peminjam_data[nama]
    print(f"Anggota '{nama.title()}' berhasil dihapus, dan semua buku yang dipinjam telah dikembalikan.")

def menu():
    clear_screen()
    while True:
        print("\n=== Sistem Perpustakaan ===")
        print("1. Kelola Buku")
        print("2. Kelola Data Peminjam")
        print("3. Kelola Peminjaman")
        print("4. Riwayat Peminjaman")     
        print("5. Laporan Statistik")      
        print("6. Keluar")
        p = input("Pilih: ").strip()

        if not p:
            print("Input tidak boleh kosong.")
            continue

        if p == "1": menu_buku()
        elif p == "2": menu_anggota()
        elif p == "3": menu_peminjaman()
        elif p == "4": riwayat_peminjaman()    
        elif p == "5": laporan_statistik()     
        elif p == "6":
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-6.")

def login():
    clear_screen()
    tampilkan_screen()
    print("\n" + "="*80)
    print(f"LOGIN ADMIN".center(80))
    print("="*80)
    while True:
        username = input("Masukkan username: ").strip()

        if not username:
            print("Username tidak boleh kosong.")
            continue

        if username not in admin:
            print("username salah, silahkan coba lagi. ")
            continue
        if username in admin:
            print("Login berhasil.")
            break
    
    while True:
        password = input("Masukkan password: ").strip()
        
        if not password:
            print("Password tidak boleh kosong.")
            continue
        
        if admin[username] != password:
            print("password salah, silahkan coba lagi. ")
            continue
        if admin[username] == password:
            print("Login berhasil.")
            menu()
            break

login()   