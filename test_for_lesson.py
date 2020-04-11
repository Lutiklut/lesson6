import divisor_master



# Test2
# проверка не кратно ли полученное число 2.
def test2():

    assert  int(divisor_master.big_simple_denominator(38))%2!=0

# Test3
 # проверка правильности получаемых результатов
def test3():

    assert  int(divisor_master.big_simple_denominator(38))==19

    # Test 4
    #проверка выводит ли  функция самый большой делитель (не обязательно простой) числа.
def test4():
     assert int(divisor_master.big_denominators(50)) == 50

   # Test 5
    #проверка выводит ли  функция самый большой делитель (не обязательно простой) числа.
def test4():
     assert int(divisor_master.big_denominators(50)) == 50