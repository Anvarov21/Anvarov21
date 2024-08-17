#def get_season(number):
    #if number < 4:
        #return "Весна"
    #elif number < 7:
        #return "Лето"
    #elif number < 10:
        #return "Осень"
    #elif number < 13:
        #return "Зима"
    #else:
        #return "Ошибка"
#number = int(input("Введите число: "))
#print(get_season(number))   

#import math
#kvadrat koren
#number = 25
#koren = math.sqrt(number)
#print(f"Kvadrat koren iz {number} raven {koren}")

#import math
#b = 2
#e = 3
#overall = math.pow(b,e)
#print(f"{b} v stepeni {e} ravno {overall}")

#import math
#katet1 = 3
#katet2 = 4
#gipotenuza = math.sqrt(katet1**2 + katet2**2)
#print(f"Dlina  gepotenuzi ravna {gipotenuza}")

#import math
#radius = 7
#dlina = 2*math.pi*radius
#print(f"dlina okrujnosti raven {dlina}")

#import math
#x=math.pi//4
#sin = math.sin(56 * x)
#cos = math.cos(2 * x)
#print(f"ravno {sin}")
#print(f"ravno {cos}")

# try:
#     result = int(input("please type random number"))
#     print(f"Your number is {result}")
# except ValueError:
#     print("Sorry men")
# except Exception as e:
#     print("you are lose")

# try:
#     file_text = input("Write your essay")
#     if file_text:
#         with open('example.txt', 'w') as file:
#             content = file.write(file_text)
#             if (content):
#                 print("You file is creted now")
#             else:
#                 print("Something is wrong")
#     else:
#         print("one more time")
#         file= str(input("Write your essay"))
# except FileNotFoundError:
#     print("Sorry man")
# except IOError:
#     print("Error: error")
# finally:
#     print("this is finaly tags")


# try: #Задания номер 1
#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))
#     result = num1 / num2
#     print(f"Результат деления {num1} на {num2} равен {result}")  
# except ValueError:
#     print("Ошибка: Введите числа. Пожалуйста, попробуйте снова.")
# except ZeroDivisionError:
#     print("Ошибка: Деление на ноль недопустимо. Пожалуйста, введите другое значение для второго числа.")
# except Exception as e:
#     print(f"Произошла непредвиденная ошибка: {e}")


# filename = "example.txt"      #Задания номер 2
# try:
#     with open(filename, 'r') as file:
#         content = file.read()
#         print("Содержимое файла:")
#         print(content)
# except FileNotFoundError:
#     print(f"Ошибка: Файл '{filename}' не найден.")


# try:    #Задание номер 3
#     number= int(input("Give me random number"))
#     result= 100/number
#     print(f"Результат деление на сто {result}")
# except ZeroDivisionError:
#     print("Ошибка деление на ноль нельзя")
# except ValueError:
#     print("Вы неправильно вели попробуйте снова")


# filename = "example.txt"   #Задание номер 4
# try:
#     with open(filename,'w') as file:
#         file.write("Hello world")
#         print("Данные успешно записаны")
# except IOError:
#     print("Ошибка")
# except Exception:
#     print("Прости повтори занова")

   
# try:    #Задание номер 5
#     stroka = input("Give me random number")
#     result=int(stroka)
#     print(f"Преобразованный результат {result}")
#     if result>=0:
#        print("Хорошо")
#     else:
#        print("Отличная работа")
# except ValueError:
#   print("Ошибка")
# finally:
#    print("Удачи")


# try:       #Задание номер 1
#     number = int(input("Give me random number"))
#     if number % 2 ==0:
#         print("Четное")
#     else:
#         print("Нечетное")
# except ValueError:
#     print("Попытайся снова")

# A = []       #Задание номер 2
# for _ in range(5):
#    a = int(input('Give me random number'))
# A.append(int(a))
# m_min = A[0]
# for i in A:
#     if m_min > i:
#        m_min = i
#     print( f'Минимальное: {m_min}' )

# for x in range(101):     #Задание номер 4
#     pass
# summa = x*(x+1)/2
# print(summa)

# numbers = [5,6,2,4,88,62,100]        #Задание номер 6
# numbers.sort()
# print(numbers)


# a = int(input("Give me random number1"))     #Задание номер 7
# b = int(input("Give me random number2"))
# print("Все простые числа") 
# for number in range(a,b+ 1): 
#     if number > 1: 
#         for i in range(2, number): 
#             if(number % i) == 0: 
#                 break 
#         else: 
#             print(number) 


# a = input("Write your essay")     #Задание номер 1
# print(len(a))


# list = [5,6,35,78,9,45,61,100]    #Задание номер 2
# list.reverse()
# print(list)


# set1 = {"apple", "banana", "cherry"}      #Задание номер 5
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}     #Задание номер 6
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)


# number = int(input("Give me random number"))    #Задание номер 1
# i = 1
# while i < number :
#     print(i)
#     i+=1


# x = 100     #Задание номер 2
# i = 0
# while i <= x :
#     print(i)
#     i+=1 
#     break
# summa = x*(x+1)/2
# print(summa)


# a = ""      #Задание номер 6
# while a != "password123":
#     a = input("Ведите пароль")
# print("Добро пожаловать")


# A = []       #Задание номер 7
# for _ in range(5):
#    a = int(input('Give me random number'))
# A.append(int(a))
# m_max = A[0]
# for i in A:
#     if m_max < i:
#        m_max = i
#     print( f'Максимальное: {m_max}' )


# a = [1,1,2,3,5,8,13,21,34,55,89]    #Задание номер 1
# newlist = [x for x in a if x<5]
# print(newlist)


# a = [1,1,2,3,5,8,13,21,34,55,89]     #Задание номер 2
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
# y = set(a)
# z = set(b)
# set3 = y & z
# print(set3)


# list = ["banana","cherry","apple","orange","kiwi"]   #Задание номер 3
# list.sort()
# print(list)


# my_dict = {'a':500, 'b':5874, 'c':560, 'd':400, 'e':5874, 'f':20}   #Задание номер 5
# print(sorted(my_dict.values())[-3:])


# a = "Hello world"    #Задание номер 18
# print(len(a))


# a = 12     #Задание калькулятор
# b = 6
# result = a + b
# print(f"Сложенный результат {result}")
# result1 = a - b
# print(f"Минусный результат {result1}")
# result2 = a * b 
# print(f"Умноженный результат {result2}")
# result3 = a / b
# print(f"Деленный результат {result3}")


# number = int(input("Give me random number"))   #Задание проверка на четность
# if number % 2 ==0:
#     print("Четное")
# else:
#     print("Нечетное")


# list = [45,2356,654,52,42,1541,2,154,14]  #Задание номер 7
# print(sum(list))


# son = 2    #Задание номер 1
# while True:
#     a = int(input("Угадай число"))
#     if a == son:
#         print("Good job")
#     elif a > son:
#         print("Твое число больше")
#     else:
#         print("Твое число меньше")


# filename = "projects.txt"      #Калькулятор
# def math(a,b,c) :
#         with open(filename,'w') as file :
#           file.write(f"First number is {a},second number is {b} result is {c}")
# try:
#     a = float(input("Give me random number1"))
#     z = input("Какую операцию нужно сделать ?")
#     b = float(input("Give me random number2"))
#     c = 0
#     if z== '+' :
#         c = a + b
#         math(a,b,c)
#     elif z=='-':
#         c = a - b
#         math(a,b,c)
#     elif z=='*':
#         c = a * b
#         math(a,b,c)
#     elif z=='/':
#         c = a / b
#         math(a,b,c)
#     elif z=='**':
#         c = a ** b
#         math(a,b,c)
#     else:
#         print("Ошибка")
# except ZeroDivisionError:
#     print("Деление на ноль нельзя")
# except ValueError:
#     print("Повтори еще")

