import math

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c  # محاسبه دلتا
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"دو ریشه حقیقی: x1 = {x1}, x2 = {x2}"
    
    elif delta == 0:
        x = -b / (2*a)
        return f"یک ریشه مضاعف: x = {x}"
    
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(delta)) / (2*a)
        return f"دو ریشه مختلط: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i"

# دریافت ورودی از کاربر
a = float(input("مقدار a: "))
b = float(input("مقدار b: "))
c = float(input("مقدار c: "))

# حل معادله و نمایش جواب
print(solve_quadratic(a, b, c))
