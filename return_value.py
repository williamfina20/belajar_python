# Belajar Method Return value

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka, total)

list_angka, total = jumlahkan(5, 5, 5, 5)
print(f"{list_angka} - Total nilai {total}")