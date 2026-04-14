import networkx as nx

# 1. Inisialisasi Graf Undirected
G_europe = nx.Graph()

# 2. Menambahkan Edge (Sisi) dan Bobot (Jarak) berdasarkan Gambar a
# Format: (Kota A, Kota B, Jarak)
edges = [
    ("Oradea", "Zerind", 71), ("Oradea", "Sibiu", 151),
    ("Zerind", "Arad", 75),
    ("Arad", "Sibiu", 140), ("Arad", "Timisoara", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75),
    ("Drobeta", "Craiova", 120),
    ("Sibiu", "Fagaras", 99), ("Sibiu", "Rimnicu Vilcea", 80),
    ("Rimnicu Vilcea", "Craiova", 146), ("Rimnicu Vilcea", "Pitesti", 97),
    ("Craiova", "Pitesti", 138),
    ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Giurgiu", 90), ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Vaslui", 142), ("Urziceni", "Hirsova", 98),
    ("Neamt", "Iasi", 87),
    ("Iasi", "Vaslui", 92),
    ("Hirsova", "Eforie", 86)
]

G_europe.add_weighted_edges_from(edges)

# 3. Mencari Semua Pasangan Shortest Path (All-Pairs Shortest Path)
# Menggunakan algoritma Dijkstra untuk graf berbobot
all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G_europe, weight='weight'))
all_shortest_distances = dict(nx.all_pairs_dijkstra_path_length(G_europe, weight='weight'))

# 4. Menampilkan Output (Contoh beberapa rute)
print(f"{'Asal':<15} | {'Tujuan':<15} | {'Jarak':<8} | {'Lintasan'}")
print("-" * 70)

# Menampilkan 10 sampel hasil agar tidak terlalu panjang
count = 0
for start_node, destinations in all_shortest_paths.items():
    for end_node, path in destinations.items():
        if start_node != end_node:
            distance = all_shortest_distances[start_node][end_node]
            print(f"{start_node:<15} | {end_node:<15} | {distance:<8} | {' -> '.join(path)}")
            count += 1
        if count >= 15: break # Limit output untuk display
    if count >= 15: break
