import csv
with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)     # будут выведены списка с "Tab" между индексами вместо ","
                        # кроме того числа - уже int или float параметром quoting=csv.QUOTE_NONNUMERIC
    print(type(line))
