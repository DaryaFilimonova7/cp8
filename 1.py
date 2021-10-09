def bin1(a,answer):
    
    while True:
        if a // 1 != 0:
            
            if a % 2 == 0:
                answer.append(0)
                a = a // 2
            elif a % 2 != 0:
                answer.append(1)
                a = a // 2 
        else:
            answer.reverse()
            print ("Двоичное представление числа равно " + "".join(map(str, answer)))
            break

    
def oct1(a,answer):
    while True:
        if a // 1 != 0:
            if a % 8 == 0:
                answer.append(0)
                a = a // 8
                #print(a)
            elif a % 8 == 1:
                answer.append(1)
                a = a // 8 
            elif a % 8 == 2:
                answer.append(2)
                a = a // 8     
            elif a % 8 == 3:
                answer.append(3)
                a = a // 8    
            elif a % 8 == 4:
                answer.append(4)
                a = a // 8
            elif a % 8 == 5:
                answer.append(5)
                a = a // 8     
            elif a % 8 == 6:
                answer.append(6)
                a = a // 8 
            elif a % 8 == 7:
                answer.append(7)
                a = a // 8 
        else:
            answer.reverse()
            print ("Восьмеричное представление числа равно " + "".join(map(str, answer)))
            break




while True:
    try:
        a = int(input("Введите десятичное число: "))
        if a > 0:
            break
        else:
            print("Ошибка. Введите положительное число.")
            continue
    except:
        print("Ошибка.")
        continue


answer = []
while True:
    try:
        
        syst = int(input("Введите основание системы счисления для перевода десятичного числа: "))
        if syst == 2 or syst == 8:
            
            break
        
        else:
            print("Ошибка. Введите основание равное 2 или 8.")
            continue
    except:
        print("Ошибка.")
        continue

if syst == 2:
    bin1(a,answer)
else:
    oct1(a,answer)