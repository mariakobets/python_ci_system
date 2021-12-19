import main
import pytest

# тесты

def test_min():
    test=[1,2,3,4,5]
    assert main.minimum(test)==1


def test_max():
    test = [1, 2, 3, 4, 5]
    assert main.maximum(test) == 5


def test_sum():
    test = [1, 2, 3, 4, 5]
    assert main.sumnum(test)==15

def test_multi():
    test = [1, 2, 3, 4, 5]
    assert main.multinum(test)==120


def test_another():
   test = ['a', 'bb','ccc']
   assert main.multinum(test) =='Ошибка: программа не может выполнить умножение чисел'






