import networkx as nx

# 1. Inisialisasi Graf Undirected
G_java = nx.Graph()

# 2. Menambahkan Edge (Sisi) dan Bobot (Jarak) berdasarkan Gambar b
# Data diambil sesuai angka yang tertera pada garis antar kota
edges_java = [
    ("Jakarta", "Cirebon", 327), ("Jakarta", "Bandung", 270),
    ("Bandung", "Cirebon", 120), ("Bandung", "Yogyakarta", 373),
    ("Cirebon", "Semarang", 305), ("Cirebon", "Yogyakarta", 210),
    ("Semarang", "Surakarta", 109), ("Semarang", "Surabaya", 369),
    ("Yogyakarta", "Surakarta", 60), ("Yogyakarta", "Magelang", 370), # Note: Di gambar tertulis 'Malang' namun posisinya di kanan
    ("Surakarta", "Surabaya", 97),
    ("Surabaya", "Malang", 94)
]

# Catatan: Pada gambar b, terdapat garis dari Yogyakarta ke arah kanan (Malang) 
# dengan bobot 370. Kita inputkan sesuai visualisasi tersebut.
G_java.add_weighted_edges_from(edges_java)

# 3. Mencari Semua Pasangan Shortest Path
all_paths_java = dict(nx.all_pairs_dijkstra_path(G_java, weight='weight'))
all_dist_java = dict(nx.all_pairs_dijkstra_path_length(G_java, weight='weight'))

# 4. Menampilkan Output (Contoh rute utama)
print(f"{'Asal':<12} | {'Tujuan':<12} | {'Jarak':<6} | {'Lintasan'}")
print("-" * 65)

# Menampilkan sampel hasil
sample_routes = [
    ("Jakarta", "Surabaya"),
    ("Jakarta", "Yogyakarta"),
    ("Bandung", "Surakarta"),
    ("Cirebon", "Malang")
]

for start, end in sample_routes:
    path = all_paths_java[start][end]
    dist = all_dist_java[start][end]
    print(f"{start:<12} | {end:<12} | {dist:<6} | {' -> '.join(path)}")
