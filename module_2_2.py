first = int(input('ввести первое число: '))
second = int(input('ввести второе число: '))
third = int(input('ввести третье число: '))
if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)