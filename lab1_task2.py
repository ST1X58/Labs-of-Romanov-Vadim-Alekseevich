obembyte = 1.44 * 1024 * 1024
stranici = 100
stroki_in_stranici = 50
symvoly_in_stroki = 25
for_kod_in_1_symvol_byte = 4

all_in_book = 100*50*25*4



print("Количество книг, помещающихся на дискету:", int(obembyte // all_in_book))
