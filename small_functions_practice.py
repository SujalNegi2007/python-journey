#20 small exercise of functions

def number_square(a):
    return a*a
print(number_square(5))

def number_sum(a,b):
    return a+b
print(number_sum(5,4))

def even_odd(a):
    if a%2 == 0:
        return True
    elif a%2 == 1:
        return False
print(even_odd(5))

def cel_to_fah(a):
    return (a*9)/5 + 32
print(cel_to_fah(5))

def num_greater_than_zero(a):
    if a > 0:
        return True
    else:
        return False
print(num_greater_than_zero(5))

def larger_num(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "both are of same length"
print(larger_num(5,4))

def reversed_words(a):
    b = a.split()
    c = []
    for i in range(len(b)-1,-1,-1):
        c.append(b[i])
    return " ".join(c)
c = input(": ")
print(reversed_words(c))

def name(a):
    return print(f"Hello, {a}!")
a = input(":")
name(a)

def is_same(a):
    b = []
    c = list(a)
    for i in range(len(c)-1,-1,-1):
        b.append(c[i])
    d = "".join(b)
    a = "".join(a)
    if a == d:
        return "same"
    else:
        return "not same"
e = input("Enter to check if same or not: ")
print(is_same(e))

def is_vovel(a):
    vovel = ["A","E","0","I","U"]
    if a in vovel:
        print("It is a vovel!")
    else:
        print("It's not a vovel")
    return
a = input("Enter the letter: ").upper()
print(is_vovel(a))

def con_upper(a):
    return a.upper()
a = input("Enter the number: ")
print(con_upper(a))

import string
def con_specific(a):
    b = []
    d = []
    d.append(a)
    c = 0
    for i in range(0,len(b)):
        if b[i] in d:
            c += 1
        else:
            continue
    return c
a = input("Enter the letter you want to check how much special characters: ")
print(con_specific(a))

def first_letter(a):
    return a[0]
a = [1,2,3,4,5]
print(first_letter(a))

def last_letter(a):
    return a[-1]
a = [1,2,3,4,5]
print(last_letter(a))

def total_items(a):
    return len(a)
a = [1,2,3,4,5,6]
print(total_items(a))

def total_sum(a):
    c = 0
    for i in range(0,len(a)):
        c += a[i]
    return c
a = [1,2,3,4,5,6]
print(total_sum(a))

def low_num(a):
    return min(a)
a = [1,2,3,4,5]
low_num(a)

def leap_year(a):
    if a%4 == 0:
        if a%100 == 0:
            if a%400 == 0:
                return "Its a leap year!")
            else:
                return "It's not a leap year!"
        else:
            return "It's a leap year!")
    else:
        return "It's not a leap year!"
a = int(input("Enter the number: "))
leap_year(a)

def empty(item):
    if len(item) == 0:
        return True
    else:
        return False

def counting():
    a = int(input("Enter the positive number: ")
    for i in range (a,0,-1):
        print(i)
    return
