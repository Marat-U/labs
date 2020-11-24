class Progression:
    def __init__(self, first, step):
        self.first = first
        self.step = step

    def set_strategy(self, strategy):
        self.strategy = strategy

    def compute_n_elem(self, n):
        print(self.strategy.compute_n_elem(n))

    def sum(self, n):
        print(self.strategy.sum(n))

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

progr = Progression(1, 2)

progr.set_strategy(ArithmeticProgression(1, 5))
progr.compute_n_elem(3)
progr.sum(4)

progr.set_strategy(GeometricProgression(1, 2))
progr.compute_n_elem(3)
progr.sum(4)
