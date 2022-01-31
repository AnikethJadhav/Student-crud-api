from math import floor


def add_numbers(num1, num2: float):
  if (num1 > 0 and num2 > 0) and (num1 < 10e6 and num2 < 10e6) and (len(str(num1).split('.')[1])<9 and len(str(num2).split('.')[1])<9):
    sum = num1 + num2
    print("SUM:", sum)
    return floor(sum)
  else:
    return "a, b needs to be as follows: 0.1 < a,b < 10e6"


num1 = 41.00121222
num2 = 111.12222328
print(add_numbers(num1, num2))