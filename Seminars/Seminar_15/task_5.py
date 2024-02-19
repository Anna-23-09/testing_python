"""
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
"""
import datetime
import argparse

DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

parser = argparse.ArgumentParser(description='Find date')
parser.add_argument('-date', metavar='date', type=str, nargs='*', help='Enter a number of weekday in month')
parser.add_argument('-day', metavar='day', type=int, default=datetime.datetime.now().weekday(),
                    help='Enter a number of weekday in month')
parser.add_argument('-dow', metavar='dow', type=str, default=DAYS[datetime.datetime.now().weekday()],
                    help='Enter a name of weekday')
parser.add_argument('-mon', metavar='mon', type=str, default=datetime.datetime.now().month, help='Enter a month name')
args = parser.parse_args()

print(args.day, args.dow, args.mon)


def _is_leap_year(year):
    return bool(not year % 4 and year % 100 or not year % 400)


def convert_string_to_date(day_number, day_name, month_name):
    current_year = datetime.datetime.now().year
    weekday_names = ['понедельник', 'вторник', 'среда', 'четверг',
                     'пятница', 'суббота', 'воскресенье']
    # month_names = {('апр', 'июн', 'сен', 'ноя') : 30,
    #                ('янв', 'мар', 'май', 'июл', 'авг', 'окт', 'дек'): 31,
    #                ('фев',): 29 if _is_leap_year(current_year) else 28
    #                }

    month_names = {(4, 5, 9, 11): 30,
                   (1, 3, 5, 7, 8, 10, 12): 31,
                   (2,): 29 if _is_leap_year(current_year) else 28
                   }

    try:
        # parts = text.split()
        # day_number = int(''.join([i for i in parts[0] if i.isdigit()]))
        # day_name = parts[1]
        # month_name = parts[2]

        first_day = datetime.datetime.strptime(f'1 {month_name} {current_year}', "%d %m %Y").weekday()
    except:
        raise ValueError

    count = 0
    weekday_names = weekday_names[first_day:] + weekday_names[:first_day]
    current_month = month_names[[month for month in month_names if month_name in month][0]]
    print(current_month)

    while count < month_names[month_name[:3]][0]:
        if day_name == weekday_names[count % 7]:
            day_number -= 1
            if not day_number:
                break
        count += 1
    else:
        raise ValueError

    return count + 1

convert_string_to_date(args.day, args.dow, args.mon)
