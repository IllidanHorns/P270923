def rectangle_area(width: int, height: int):
    if (width > 0) and (height > 0):
        S = width*height
        return S
    else:
        return None

a = int(input())
b = int(input())
print("Площадь = ", rectangle_area(a,b))

def is_even(number: int):
    if (number % 2) == 0:
        return True
    elif (number % 2) != 0:
        return False

a = int(input())
print(is_even(a))

def sum_digits(number: int):
    if number > 0:
        CountCh: int = 0
        while number > 0:
            CountCh += number % 10
            number = number // 10
        return CountCh
    else:
        return None
a = int(input())
print(sum_digits(a))