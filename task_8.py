mass = float(input("Введите массу в килограммах: "))
specific_heat_capacity = float(input("Введите удельную теплоёмкость (Дж/кг·°C): "))
temperature_change = float(input("Введите изменение температуры в градусах Цельсия: "))

# Вычисляем количество теплоты
heat = mass * specific_heat_capacity * temperature_change

# Выводим результат
print(f"Количество теплоты: {heat} Джоулей")