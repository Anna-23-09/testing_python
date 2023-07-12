"""zip(function, iterable)"""
names = ["Иван", "Николай", "Петр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99] # 4-е значение будет проигнорировано
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary: 2f} денег и премию {salary * award:.2f}')
