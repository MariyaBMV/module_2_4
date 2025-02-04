"""DZ. Stil for. Elementi spiska.
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:
Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значен
ия переменной is_prime после проверки (True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль)."""


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # список чисел.
_prime = list() # создали пустые списки
not_prime = list() #также пустой список
for i in numbers: #перебрали каждое число в списке.

    if i > 1: #установили проверку, чтобы число было > 1
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                not_prime.append(i)
                is_prime = False
                break
        if is_prime:
                _prime.append(i)

print("Простые числа из списка:", _prime)
print("Простые числа из списка:", not_prime)


