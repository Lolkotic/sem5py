# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

def counting(path):
    res = dict()
    line_number = 0
    try:
        with open(path, 'r') as p:
            for line_number, o in enumerate(p, 1):
                res[line_number] = len(o.split())
    except ValueError as error:
        print(error)
    return line_number, res
if __name__ == '__main__':
    nums, counts = counting('task2.txt')
    print(f'Количество строк - {nums}')
    for o, p in counts.items():
        print(f'Слов в(о)  {o} строке: {p} ')
