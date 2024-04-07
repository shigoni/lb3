import random
def number_1():
    N = int(input("Введите количество слов: "))
    str = ""
    for i in range(N):
        i += 1
        strvvod = input(f"Введите слово {i}: ")
        str += strvvod + " "
    print("Результат: ", str)
    
def number_2():
    str = ""
    while True:
        N = input("Введите слово или stop: ")
        if N == "stop":
            break
        else:
            str += N + " "
    print("Результат: ", str)

'''  
    str = ""
        while True:
            N = input("Введите слово: ")
            if N.lower() == "stop":
                break
            str += N + " "
        print("Результат: ", str)
'''
def number_3():
    while True:
        str = input("Введите слово или stop: ")
        if str == "stop":
            break
        else:
            for i in str:
                if i == "ф":
                    print("Ого! Это редкое слово!")
                    break
            else:
                print("Эх, это не очень редкое слово")

def rd():
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    return x, y
           
def number_4():
    tr = 0
    fl = 0
    while fl < 3:
        x, y = rd()
        resh = x + y
        otv = int(input(f"{x} + {y} = "))
        if otv == resh:
            tr += 1
            print("Правильно!")
        else:
            fl += 1
            print("Ответ неверный")
    print("Игра окончена. Правильных ответов: ", tr)         
            
while True:
    number = int(input("Введите номер задания: "))

    if number == 1:
        number_1()
    elif number == 2:
        number_2()
    elif number == 3:
        number_3()
    elif number == 4:
        number_4()
    else:
        print("Такого задания нет")
    



    

    