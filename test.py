import divisor_master
# Test1
# проверка нет ли в чисел кратных 2.
def test_function():
    list_f=divisor_master.denominators(43)
    print (list_f)
    for i in list_f:
        if i%2==0:
            return print("Wrong")
        else: return print ("It`s OK")
    return True
