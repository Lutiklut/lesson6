
import math
#Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000. Модуль содержит функции:
#1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
def simple(n):
    if n < 2:
        return True
    elif n == 2:
        return False
    i = 2
    limit = int(math.sqrt(n))

    while i <= limit:
        if n % i == 0:
            return False
        i += 1

    return True


def denominators(n):
      lst = []
      for i in range(1, n + 1):
          if n % i == 0:
                lst.append(i)
      return lst



#3) выводит самый большой простой делитель числа.
def big_simple_denominator(n):
    list_din = []
    lst = []
    list_wifh_den=[]
    for i in range(1, n + 1):
        if n % i == 0:
            list_din.append(i)


    for a in list_din:

        c = 2
        j = 0
        while c ** 2 <= a and j != 1:
            if a % c == 0:
                j = 1
            c += 1
        if j == 0:


            lst.append(a)


    return print (lst[-1])


#4) функция выводит каноническое разложение числа на простые множители;

def simle_dev (n):

        i = 2
        list_simple= []
        while i * i <= n:
            while n % i == 0:
                list_simple.append(i)
                n = n / i
            i = i + 1
        if n > 1:
            list_simple.append(n)
        return print(list_simple)




 # 5) функция выводит самый большой делитель (не обязательно простой) числа.

def big_denominators(n):
      lst = []
      for i in range(1, n + 1):
          if n % i == 0:
                lst.append(i)
      return print(lst[-1])