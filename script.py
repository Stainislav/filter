'''
Требования:

1. В файл filtered.txt записывается список отфильтрованных файлов.

2. Выводится принтом словарь, в котором ключами являются имена файлов,
а значениями - папки назначения.

3. При обнаружении строки, сигнализирующей об ошибке, создается файл warning.txt,
в первой строке которого пишется количество ошибок, а в последующих строках выводится список ошибок.


Алгоритм:

1. Читаем данные из файла applog.log.
2. Ищем строки с ошибками и добавляем их в список ошибок.
3. Ищем строки с именами файлов и добавляем их в список файлов.
4. Ищем строки с именами папок и добавляем их в список папок.
5. Если есть ошибки, записываем их в файл warning.txt.
6. Список с именами файлов записываем в файл filtered.txt.
7. Создаём словарь на основе списка файлов и списка папок.
8. Выводим словарь в консоль.

Запуск:

Для работы скрипта необходим модуль re из стандартной библиотеки Python.
Для запуска скрипта вводим в консоли: python3 script.py

'''

import re

log_list = []

with open('applog.log', 'r') as f:
    for line in f:
        log_list.append(line)

error_list = []

# Ищем строки с ошибками.
for line in log_list:
    match = re.search('(error)', line, flags=re.IGNORECASE)
    if match:
        error_list.append(line)

tmp_list = []

# Делим строки с ошибками на два фрагмента.
for line in error_list:
    error = 'error' + ' '
    new_line = re.split(error, line, flags=re.IGNORECASE)
    tmp_list.append(new_line)

error_list.clear()

error_counter = 0

# Сохраняем в список фрагменты строк с описаниями ошибок.
for line in tmp_list:
    error_list.append(line[1])
    error_counter += 1

if error_list:
    with open('warning.txt', 'w') as f:
        errors = str(error_counter) + ' errors'
        f.write(errors + '\n')

        for line in error_list:
            f.write(line)

file_list = []

# Создаём список именами файлов.
for line in log_list:
    match = re.search('(file)+.+(csv)', line)
    if match:
        csv_file = match.group()
        file_list.append(csv_file)

with open('filtered.txt', 'w') as f:
    for line in file_list:
        f.write(line + '\n')


folder_list = []

# Создаём список с именами папок.
for line in log_list:
    match = re.search('(folder)+\d', line)
    if match:
        folder = match.group()
        folder_list.append(folder)

d = {}

# Заполняем словарь данными из двух списков.
for item, folder in zip(file_list, folder_list):
    d[item] = folder

# Печатаем словарь.
for key, val in d.items():
    print(f'{key} = {val}')

