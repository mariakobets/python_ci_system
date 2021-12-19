# Бейдж с результатами тестов

[![Build Status - GitHub](https://github.com/mariakobets/python_ci_system/workflows/pytesting/badge.svg)](https://github.com/mariakobets/python_ci_system/actions/workflows/pythonapp.yml)

# Коды Программы и Тестов

## Код программы
```Python

# функции

def minimum(array):
    min=array[0]
    for i in array:
        if i<min:
            min=i
            print(min)
    return min


def maximum(array):
    max=array[0]
    for i in array:
        if i>max:
            max=i
    return max


def sumnum(array):
    sum =0
    for i in array:
        sum+=i
    return sum


def multinum(array):

    try:
        multi = 1
        for i in array:
            try:
                multi*=i

            except OverflowError:
                print("Ошибка переполнения")
        return multi
    except:
        return "Ошибка: программа не может выполнить умножение чисел"


# работа с файлом
array=[]
try:
    with open("file.txt") as file:
        for i in file:
            array.extend([int(x) for x in i.split()])

    # результат
    min=minimum(array)
    print("Минимальное:",min)
    max=maximum(array)
    print("Максимальное:",max)
    sum = sumnum(array)
    print("Сумма:",sum)
    multi=multinum(array)
    print("Произведение:",multi)
except IOError:
        print("Невозмонжо открыть или прочитать файл")
```

## Код тестов
```Python
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
```

## Код тестов времени работы

```Python
import main
import time
#работа программы с маленьким файлом
time1=time.time()
array_little=[]
with open("file.txt") as file:
    for i in file:
        array_little.extend([int(x) for x in i.split()])

min=main.minimum(array_little)
max=main.maximum(array_little)
sum = main.sumnum(array_little)
multi= main.multinum(array_little)
total_test_time1=time.time()-time1

# работа программы с большим файлом
time2=time.time()
array_big=[]
with open("file2.txt") as file:
    for i in file:
        array_big.extend([int(x) for x in i.split()])

min=main.minimum(array_big)
max=main.maximum(array_big)
sum = main.sumnum(array_big)
multi= main.multinum(array_big)
total_test_time2=time.time()-time2

print(f'Время работы с файлом file.txt -  {total_test_time1}')
print(f'Время работы с файлом file2.txt -  {total_test_time1}')
difference=total_test_time2-total_test_time1
print(f'Разница времени работы с файлами - {difference}')
```
## Вывод в консоль тестов
```console
platform win32 -- Python 3.9.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\Вадим\Downloads\Архив
plugins: anyio-3.1.0, markdown-1.0.2, telegram-1.2.0
collected 5 items

test_main.py .....                                                                                               [100%]

================================================== 5 passed in 0.05s ==================================================

```