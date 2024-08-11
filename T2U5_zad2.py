# -*- coding: cp1251 -*-
stroka = str(input("Введите строку:"))
count_gl = 0
count_sgl = 0
#А, о, у, ы, э, е, ё, и, ю, я
#(a, o, e, i, u, y)
vowels = set("aeiouyаоуыэеёиюя")
for letter in stroka:
    if letter in vowels:
        count_gl += 1
    else:
        count_sgl += 1
print("Количество гласных равно:", count_gl)
print("Количество согласных равно:", count_sgl)
