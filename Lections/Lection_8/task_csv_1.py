import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)  # выводится в виде маленького списка: ['Quin', 'M', '29', '71', '176']
    print(type(line))
