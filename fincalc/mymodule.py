class Bankomat:

    def __init__(self, start_sum=1, new_sum=1, final_sum=1):
        self.start_sum = float(start_sum)
        self.new_sum = float(new_sum)
        self.final_sum = float(final_sum)

    # Вывод данных на экран
    def __str__(self):
        return f"{self.start_sum, self.new_sum, self.final_sum}"

    # Сравнение сумм в банках
    def __lt__(self, other):
        return self.final_sum < other.final_sum

    def __gt__(self, other):
        return self.final_sum > other.final_sum

    def __le__(self, other):
        return self.final_sum <= other.final_sum

    def __ge__(self, other):
        return self.final_sum >= other.final_sum

    def __eq__(self, other):
        return self.final_sum == other.final_sum

    def __ne__(self, other):
        return self.final_sum != other.final_sum

    # Выполнения арифметических операций над суммами
    def __add__(self, other):
        return self.final_sum + other.final_sum

    def __sub__(self, other):
        if self.final_sum >= other.final_sum:
            return self.final_sum - other.final_sum
        else:
            return ValueError("Отрицательная сумма денег.")

    def __mul__(self, other):
        return self.final_sum * other.final_sum

    def __truediv__(self, other):
        return self.final_sum / other.final_sum
