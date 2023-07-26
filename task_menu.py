import print_text as pt
from typing import Tuple

def menu_task():
    print(pt.greeting_text())
    print(pt.menu_text())
    task_menu()
def task_menu():
    number = int(input('\033[32mВведите выбранный вариант: \033[0m'))
    if 1 <= number <= 3:
            match number:
                case 1:
                    print(pt.task1_text())
                    task1_start()
                    task_menu()
                case 2:
                    print(pt.task2_text())
                    task2_start()
                    task_menu()
                case 3:
                    print(pt.task3_text())
                    task3_start()
                    task_menu()
    elif number == 0:
            print(pt.menu_text())
            task_menu()
    elif number == 00:
            print(pt.exit_text())
            exit()
    else:
        print(pt.error_text())
        task_menu()


# Задача 1
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Имена файлов для отображения
FILE_1 = "d:\\path1\\sub_path1\\file_1.png"
FILE_2 = "d:\\path2\\sub_path2\\file_2.txt"
FILE_3 = "d:\\path3\\sub_path3\\file_3.docx"


def split_path(path: str) -> tuple[str, str, str]:
    """Парсинг абсолютного пути на каталог, имя и расширение файла"""
    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext


def task1_start():
    print(split_path(FILE_1))
    print(split_path(FILE_2))
    print(split_path(FILE_3))

# Задача 2
# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# Списки для проверки работы генератора
NAMES = ["Иван", "Петр", "Михаил", "Сергей"]
RATES = [10_000, 20_000, 15_000, 30_000]
PERCENTS = ["10.25%", "15.00%", "6.50%", "12.75%"]


def gen_dict(names: list[str], rates: list[int], percents: list[str]):
    """Генератор премий"""
    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(names, rates, map(lambda x: float(x[:-1]), percents))))}


def task2_start():
    print(NAMES)
    print(RATES)
    print(PERCENTS)
    print(*gen_dict(NAMES, RATES, PERCENTS))

# Задача 3
# Генератор чисел Фибоначчи
# Последовательность Фибоначчи - 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# Множество для проверки генерации рядов Фибоначчи
FIB_SET = (5, 8, 10, 15)


def fib_gen(n: int) -> list[int]:
    """Генератор чисел Фибоначчи"""
    fib_list = [0]
    fib1 = 0
    fib2 = 1
    for _ in range(n):
        fib_list.append(fib2)
        fib1, fib2 = fib2, fib2 + fib1
    yield fib_list


def task3_start():
    for n in FIB_SET:
        print(*fib_gen(n))