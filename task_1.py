# Запрашиваем у пользователя расстояние и время
distance = float(input("Введите расстояние в километрах: "))
time = float(input("Введите время в часах: "))

# Проверяем, что время не равно нулю, чтобы избежать деления на ноль
if time != 0:
    # Рассчитываем скорость
    speed = distance / time
    print(f"Скорость: {speed} км/ч")
else:
    print("Ошибка: время не может быть равно нулю.")