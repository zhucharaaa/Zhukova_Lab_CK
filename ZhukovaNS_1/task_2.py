# TODO Найдите количество книг, которое можно разместить на дискете
byte = 1.44 * 1024 * 1024
one_book = 4 * 25 * 50 * 100
n_book = int(byte//one_book)
print("Количество книг, помещающихся на дискету:", n_book)
