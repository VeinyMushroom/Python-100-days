# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
# print(data)

import csv

with open("/Users/eleanorextence/Desktop/100 Days Files/Day Files/day-25-start/weather_data.csv") as data_file:
    data = list(csv.reader(data_file))
    temperatures = []
    for row in data[1:]:
        temperatures.append(int(row[1]))
    print(temperatures)
