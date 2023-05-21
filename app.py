def create_bad_character_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def search(pattern, text):
    m = len(pattern)
    n = len(text)
    table = create_bad_character_table(pattern)
    i = m - 1  # indeks karakter terakhir pada pola
    j = m - 1  # indeks karakter terakhir pada teks

    while i < n:
        if pattern[j] == text[i]:
            if j == 0:
                return i  # Pola ditemukan
            i -= 1
            j -= 1
        else:
            shift = table.get(text[i], -1)
            i = i + m - min(j, shift + 1)
            j = m - 1
    
    return -1  # Pola tidak ditemukan

# Membaca input dari pengguna
text = input("Masukkan teks: ")
pattern = input("Masukkan pola: ")

# Melakukan pencarian menggunakan algoritma Boyer-Moore
result = search(pattern, text)

# Menampilkan hasil
if result != -1:
    print("Pola ditemukan pada indeks", result)
else:
    print("Pola tidak ditemukan dalam teks")