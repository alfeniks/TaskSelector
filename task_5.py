mass = float(input("Введите массу объекта в килограммах: "))
velocity = float(input("Введите скорость объекта в метрах в секунду: "))

# Вычисляем кинетическую энергию
kinetic_energy = 0.5 * mass * velocity ** 2

# Выводим результат
print(f"Кинетическая энергия: {kinetic_energy} джоулей")