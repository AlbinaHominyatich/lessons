def is_palindrome(str):
 # ''.join() - объединение в строку
 # str.split(' ') - преобразование строки в массив по разделителю (в данном случае - пробелу)
 # ''.join(str.split(' ')) - удаление пробелов из строки
 # casefold() - нечувствительность к регистру, приведение к нижнему регистру
 str = ''.join(str.split(' ')).casefold()
 # инверсия строки - изменение порядка следования букв на противоположный
 rev = reversed(str)
 # сравнение списков
 return list(str) == list(rev)

print(is_palindrome('Borrow or rob')) # True