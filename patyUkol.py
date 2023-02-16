teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

avarage_temperature = [[sum(day) / len(day)] for day in teploty]
print(avarage_temperature)

morning_temperature = [[day[0]] for day in teploty]
print(morning_temperature)

night_temperature = [[day[3]] for day in teploty]
print(night_temperature)

noon_night_temperature = [[day[1], day[3]] for day in teploty]
print(noon_night_temperature)