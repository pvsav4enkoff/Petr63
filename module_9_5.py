class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start, stop,step=1):
        self.start = start
        self.stop = stop
        self.pointer = start
        if step != 0:
            self.step = step
        else:
            raise StepValueError
            return
    def __iter__(self):
        self.pointer = self.start
        return self
    def __next__(self):
        result = 0
        if self.step > 0 and self.stop > self.start:
            if self.pointer > self.stop:
                raise StopIteration
            result = self.pointer
            self.pointer += self.step
        if self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration
            result = self.pointer
            self.pointer += self.step
            pass
        if self.step > 0 and self.stop < self.start:
            if self.pointer < self.stop:
                raise StopIteration
            result = self.pointer
            self.pointer -= self.step
        return result


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()