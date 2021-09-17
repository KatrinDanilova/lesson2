# задание 1
age = input("Сколько вам лет? ")

#try:
#    age = int(age)
#except ValueError:
#    print("Введите числовое значение")
    
age = int(age)
  
if age < 7:
    print(f"Вы еще не пошли в школу")
elif age >=7 and age < 18:
    print(f"Вы школьник")
elif age >=18 and age < 24:  
    print(f"Вы студент")
else:
    print(f"Работай лошара!")

# задание 2
str1 = input("Строка 1: ")
str2 = input("Строка 2: ")

str1_len = len(str1)
str2_len = len(str2)

if str1_len == str2_len:
    print(f"1") 
elif str1_len != str2_len: 
    if str1_len > str2_len:
        print(f"2") 
    elif str2 == 'learn':
        print(f"3") 



