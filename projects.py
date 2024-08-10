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


try:
    stroka = input("Give me random number")
    result=int(stroka)
    print(f"Преобразованный результат {result}")
    if result>=0:
       print("Хорошо")
    else:
       print("Отличная работа")
except ValueError:
  print("Ошибка")
finally:
   print("Удачи")