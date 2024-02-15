import argparse

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

r"""
Примеры запуска в терминале:
python .\task_argparse_1.py 42 3.14 73
python .\task_argparse_1.py --help
python .\task_argparse_1.py Hello world!
"""