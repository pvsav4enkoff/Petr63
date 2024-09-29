def is_prime(func):
  def wrapper(*args, **kwargs):
      n = func(*args, **kwargs)
      if n <= 1:
          print("Не простое")
          return n
      k = 0
      for j in range(2, n+1):
          if n % j == 0:
              k += 1
          if k == 2:
              print("Не простое")
              return n
      print("Простое")
      return n
  return wrapper

@is_prime
def sum_three(num1, num2, num3):
  return num1+num2+num3


result = sum_three(2, 3, 6)
print(result)
