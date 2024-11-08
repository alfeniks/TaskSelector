mass = float(input("Введите массу объекта в килограммах: "))
height = float(input("Введите высоту в метрах: "))
gravity = float(input("Введите ускорение свободного падения (м/с²): "))

# Вычисляем потенциальную энергию
potential_energy = mass * gravity * height

# Выводим результат
print(f"Потенциальная энергия: {potential_energy} джоулей")