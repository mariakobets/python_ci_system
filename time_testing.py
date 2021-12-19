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
