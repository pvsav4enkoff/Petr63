def tracer(func, *pargs, **kargs):  # Принимает произвольные аргументы
  print('calling:', func.__name__)
  return func(*pargs, **kargs)       # Передает все полученные аргументы
def func(a, b, c, d):
    return a + b + c + d
print(tracer(func, 1, 2, c=3, d=4))