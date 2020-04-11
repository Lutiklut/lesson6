import divisor_master

#транспонирование
from pprint import pprint

matrix = [[0.5,   0,   0,   0,   0],
          [  1, 0.5,   0,   0,   0],
          [  1,   1, 0.5,   0,   0],
          [  1,   1,   1, 0.5,   0],
          [  1,   1,   1,   1, 0.5]]

matrix_t = list(zip(*matrix))



result=  [[0.5,   1,   1,   1,   1],
          [  0, 0.5,   1,   1,   1],
          [  0,   0, 0.5,   1,   1],
          [  0,   0,   0, 0.5,   1],
          [  0,   0,   0,   0, 0.5]]

#Test1
# проверка транспонирования
def test1_function():
        if matrix_t != result:
            return print("Wrong")
        else:
                     return print("It`s OK")
        return True

test1_function()

# Test 5
# проверка нет ли в чисел кратных 2.
def test5_function():
    list_f = divisor_master.denominators(43)
    print(list_f)
    for i in list_f:
        if int(i) % 2 == 0:
            return print("Wrong")
        else:
            return print("It`s OK")
    return True


test5_function()
