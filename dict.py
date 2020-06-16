#Belajar Tipe Data Dictionary

customer = {"name":"eko", "age":30, "address":"subang"}

name = customer["name"]
age = customer["age"]
address = customer["address"]

#tambah data dalam dictionary
customer["company"] = "X"

#ubah data pada dictionary
customer["name"] = "Eko Kurniawan"

#menghapus data pada dictionary
del customer["address"]

for key, value in customer.items():
    print(f"{key}:{value}")

