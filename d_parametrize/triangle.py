# Validity of Triangle given sides

# Function definition to check validity
def is_valid_triangle(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False


def type_of_triangle(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "不是三角形"
    if (a == b) and (b == c):
        return "等邊三角形"
    elif (a == b) or (b == c) or (a == c):
        return "等腰三角形"
    elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
        return "直角三角形"
    else:
        return "一般三角形"
