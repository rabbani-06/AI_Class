# MUH. RAFI RABBANI_F55123038

def find_even_indices(x, y1):
    if y1 % 2 != 0:
        raise ValueError("Input y1 is not an even number. Please provide an even number.")
    
    indices = [i for i, value in enumerate(x) if value == y1]
    
    if not indices:
        raise ValueError(f"Bilangan {y1} tidak ditemukan dalam list.")
    
    return indices

x = [2, 7, 8, 9, 1, 1, 4, 4, 4, 9, 5, 7, 8, 6, 1, 4, 7, 8, 3, 2]

y1 = int(input("Masukkan bilangan genap yang ingin dicari: "))

try:
    indices = find_even_indices(x, y1)
    print(f"Bilangan {y1} ada di indeks {indices}")
except ValueError as e:
    print(e)
