import csv


# словарь символов для hash
alf = sorted('ёЁйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
d = {alf[i]: i + 1 for i in range(66)}

# функция задаёт строке свой уникальный хэш
# s - входная строка, возвращает уникальный хэш этой строки
def hash(s):
    s = s.replace(' ', '')
    p = 67
    m = 10 ** 9 + 9
    hash_value = 0
    i = 0
    for c in s:
        hash_value += d[c] * p ** i
        i += 1
    return hash_value % m

# for i in range(len(s)):
#     c = s[i]
#     hash_value += d[c] * p ** i

with open('students.csv', encoding='utf-8') as file, open('students_with_hash.csv', 'w', encoding='utf-8') as new_file:
    data = list(csv.reader(file, delimiter=','))
    res = csv.writer(new_file, delimiter=',')

    res.writerow(data[0])
    for stroka in data[1:]:
        fio = stroka[1]
        h = hash(fio)
        stroka[0] = h
        res.writerow(stroka)


