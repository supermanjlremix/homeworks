import functools

class FactorialCalculator:
    @functools.lru_cache(maxsize=None)
    def calculate_factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)

calculator = FactorialCalculator()
print(calculator.calculate_factorial(5))  # Вычисляет факториал числа 5
print(calculator.calculate_factorial(5))  # Возвращает закэшированный результат для числа 5
