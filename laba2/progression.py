class Progression:
  def __init__(self, first, step):
    self.first = first
    self.step = step

  def compute_n_elem(self, n):
    pass

  def sum(self, n):
    pass

class ArithmeticProgression(Progression):
  def __init__(self, first, step):
    super().__init__(first, step)

  def compute_n_elem(self, n):
    a_n = self.first
    for i in range(n - 1):
      a_n += self.step
    return a_n

  def sum(self, n):
    summ = 0
    for i in range(1, n + 1):
      a_n = self.first + self.step * (i - 1)
      summ += a_n
    return summ

class GeometricProgression(Progression):
  def __init__(self, first, step):
    super().__init__(first, step)

  def compute_n_elem(self, n):
    a_n = self.first
    for i in range(n - 1):
      a_n *= self.step
    return a_n

  def sum(self, n):
    summ = 0
    for i in range(1, n + 1):
      a_n = self.first * self.step ** (i - 1)
      summ += a_n
    return summ

'''
obj1 = ArithmeticProgression(1, 10)
print(obj1.compute_n_elem(10))
print(obj1.sum(10))

obj1 = GeometricProgression(1, 10)
print(obj1.compute_n_elem(10))
print(obj1.sum(10))
'''
choose = input()
first, step = list(map(int, input().split()))
count = int(input())
if (choose == 'arithmetic'):
    obj1 = ArithmeticProgression(first, step)
    print(obj1.compute_n_elem(count))
    print(obj1.sum(count))
elif (choose == 'geometric'):
    obj1 = GeometricProgression(first, step)
    print(obj1.compute_n_elem(count))
    print(obj1.sum(count))
else:
    print('Cant create this progression')
