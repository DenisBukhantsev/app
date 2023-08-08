from fractions import Fraction

a = int(input("a ")) 
b = int(input("b "))
c = int(input("c ")) 
d = int(input("d "))
action = input("действие ")
if action == "+":
    if b == d:
        print(f"{a + c}/{d}")
    else:
        print(f"{(a * d) + (c * b)}/{b * d}")
    print("проверка функцией Fraction", Fraction(a, b) + Fraction(c, d))
elif action == "*":
    a_c = a * c
    b_d = b * d 
    
    for i in range(min(a_c, b_d), 1, -1):
        if a_c % i == 0 and b_d % i == 0:
            print(f"{int(a_c / i)}/{int(b_d / i)}")
            break
    print("проверка функцией Fraction", Fraction(a, b) * Fraction(c, d))
