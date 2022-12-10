# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32



with open('task3.txt', 'r', encoding='utf-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if int(float(value)) < 20000:
            print(f'{key}: оклад менее 20 тыс.')

h = open('task3.txt', 'r')
content = h.readlines()
sum = 0
for line in content:
    for i in line:
        if i.isdigit() == True:
            sum += float(i)
print("Средний оклад:", sum/10 ,"тысячи рублей")


