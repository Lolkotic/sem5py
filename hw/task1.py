# 1) Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_func = open('task1.txt', 'w')
line = input("Введите Ваш текст: ")
while line:
    my_func.writelines(line)
    line = input("Введите Ваш текст: ")
    if not line:
        break
my_func = open('task1.txt', 'r')
my_text = my_func.readlines(line)
print(my_text)
my_func.close()

