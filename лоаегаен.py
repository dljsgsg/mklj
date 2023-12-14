#1
print("time")
user_time = int(input("введите время в секундах от 0 до 86400:"))
user_choise = input("выберите eдиницу времени\n if in hours - h\n if in minuets - m\n if in seconds - s: ")
if user_choise == "s":
    print(f"time in seconds until midnight = {86400 - user_time}")
elif user_choise == "m":
    print(f"time in minuets until midnight = {86400 - user_time // 60}")
elif user_choise == "h":
    print(f"time in hours until moonlight = {86400 - user_time // 3600}")
    #2
calculate = input('список опций: \n "+" - периметр: \n "*" - площадь:')
a = float(input("first:"))
b = float(input("second:"))
if calculate == '+':
        print(f"результат вычисления: {a + b}")
elif calculate == '*':
        print(f"результат вычисления: {a * b}")
        #3
a = int(input("Введите ценy прситавки:"))
b = int(input("кол-во приставок:"))
c = int(input("процент скидки:"))
print(f'итого: {a * b // c}')
    #4
a = int(input("размер файла:"))
b = int(input("скорость интернета в битах/с:"))
print(f'за какое время скачается(ч): {a // b}')

#5
user_choise = input("\n if 0-7 - n\n if in 7-13 - m\n if in 13-17 - d \n id in 17-0 - nn:")
if user_choise == "n":
    print("good night")
elif user_choise == "m":
    print("good morning")
elif user_choise == "d":
    print("good evening")
elif user_choise == "nn":
    print("good night")



