initial_speed = float(input("Введите начальную скорость в км/ч: "))
time = float(input("Введите время движения в секундах: "))
acceleration = float(input("Введите ускорение в м/с^2: "))

initial_speed_mps = initial_speed / 3.6

distance = initial_speed_mps * time + (acceleration * time ** 2) / 2

distance_km = distance / 1000

print("Расстояние до точки назначения: {:.2f} км".format(distance_km))
