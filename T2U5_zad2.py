# -*- coding: cp1251 -*-
stroka = str(input("������� ������:"))
count_gl = 0
count_sgl = 0
#�, �, �, �, �, �, �, �, �, �
#(a, o, e, i, u, y)
vowels = set("aeiouy���������")
for letter in stroka:
    if letter in vowels:
        count_gl += 1
    else:
        count_sgl += 1
print("���������� ������� �����:", count_gl)
print("���������� ��������� �����:", count_sgl)
