import random

def boyer_moore_shuffle(word):
    # Mengonversi kata menjadi list karakter
    characters = list(word)
    length = len(characters)
    
    # Mengacak urutan karakter menggunakan algoritma Fisher-Yates
    for i in range(length-1, 0, -1):
        j = random.randint(0, i)
        characters[i], characters[j] = characters[j], characters[i]
    
    # Menggabungkan karakter yang sudah diacak menjadi kata baru
    shuffled_word = ''.join(characters)
    
    return shuffled_word

# Contoh penggunaan
word = input("Masukkan kata: ")
shuffled_word = boyer_moore_shuffle(word)
print("Kata yang diacak: ", shuffled_word)
