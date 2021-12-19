
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





