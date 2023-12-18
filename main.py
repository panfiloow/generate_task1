import random
import numpy
import tkinter as tk


def find_min(task):
    first = [task[0], task[1], task[2]]
    second = [task[3], task[4], task[5]]
    third = [task[6], task[7], task[8]]
    target = [task[9], task[10]]


def generateLine(i, j):
    point_y = [0, j]
    point_x = [i, 0]
    k = (point_x[1] - point_y[1]) / (point_x[0] - point_y[0])
    b = point_y[1] - k * point_y[0]
    return [-(k), 1, b]


def generateThird(first, second):
    first_y_cross = first[2] / first[1]
    second_y_cross = second[2] / second[1]
    if first_y_cross < second_y_cross:
        lower = first
        upper = second
        upper_y_cross = second[2] / second[1]
    else:
        lower = second
        upper = first
        upper_y_cross = first[2] / first[1]
    first_second_cross = find_cross(first, second)
    i = first_second_cross[0] + 1
    lim_i = upper[2] / upper[0]
    lim_j = upper_y_cross + 50
    while i < lim_i:
        j = upper_y_cross + 1
        while j < lim_j:
            line = generateLine(i, j)
            flag = is_normal(line, upper)
            cross = find_cross(line, lower)
            flag2 = cross[1] < first_second_cross[1] and cross[0] > first_second_cross[0] and cross[0] != \
                    first_second_cross[0]
            flag3 = line[0].is_integer()
            if flag and flag2 and flag3:
                rand1 = random.randint(3, 10)
                if upper[0] - rand1 > 0:
                    return [line[0] * 10, line[1] * 10, line[2] * 10, upper[0] - rand1, upper[1] - rand1]
                else:
                    return [line[0] * 10, line[1] * 10, line[2] * 10, upper[0] + rand1, upper[1] + rand1]
            j = j + 1
        i = i + 1
    return -1


def find_cross(first, second):
    try:
        m1 = numpy.array([[first[0], first[1]], [second[0], second[1]]])
        v1 = numpy.array([first[2], second[2]])
        answer = numpy.linalg.solve(m1, v1)
        return answer
    except numpy.linalg.LinAlgError:
        return False


def is_normal(first, second):
    try:
        m1 = numpy.array([[first[0], first[1]], [second[0], second[1]]])
        v1 = numpy.array([first[2], second[2]])
        answer = numpy.linalg.solve(m1, v1)
        x_cross = answer[0]
        y_cross = answer[1]
        flag1 = x_cross.is_integer()
        flag2 = y_cross.is_integer()
        flag3 = max(first[0], second[0]) % min(first[0], second[0])
        flag4 = max(first[1], second[1]) % min(first[1], second[1])
        flag5 = max(first[2], second[2]) % min(first[2], second[2])
        flag6 = (flag3 == 0 and flag4 == 0 and flag5 == 0)
        if flag1 and flag2 and not flag6 and x_cross > 0 and y_cross > 0:
            return True
        else:
            return False
    except numpy.linalg.LinAlgError:
        return False


def generateFirstAndSecond():
    x1 = random.randint(1, 50)
    y1 = random.randint(1, 50)
    firstLine = [x1, y1, x1 * y1 * random.randint(1, 3)]
    x2 = random.randint(1, 50)
    y2 = random.randint(1, 50)
    secondLine = [x2, y2, x2 * y2 * random.randint(1, 3)]
    return [firstLine, secondLine]


def generateTask():
    firstsAndSecond = generateFirstAndSecond()
    first = firstsAndSecond[0]
    second = firstsAndSecond[1]
    answer = is_normal(first, second)
    while not answer:
        firstsAndSecond = generateFirstAndSecond()
        first = firstsAndSecond[0]
        second = firstsAndSecond[1]
        answer = is_normal(first, second)
        if answer:
            line = generateThird(first, second)
            if line == -1:
                generateTask()
            else:
                return [first[0], first[1], first[2], second[0], second[1], second[2], int(line[0]), line[1],
                        int(line[2]), line[3], line[4]]


def print_tex(a1, b1, a2, b2, c2, a3, b3, c3, a4, b4, c4, year, var):
    tex_title = r'\begin{center}' + '\n\t' + r'Методы оптимизации -- ' + f'{year}' + '.' + '\n\t' + r'\textbf{Выполнил ........................................................... группа ..........' + '\n' + r'Задание по теме <<Графический метод решения задачи ЛП>>, ' 'вариант ' + f'{var}' + r'}' + '\n' + r'\end{center}' + '\n\n'
    MO.write(tex_title)
    tex_body = r'\begin{flushleft}' + '\n\t' + r'\textit{    Привести к каноническому виду, построить двойственную задачу следующей задачи линейного программирования $(x_1,x_2 \geq 0)$. Угловым точкам $D$ сопоставить базисные множества.}' + '\n' + r'\end{flushleft}' + '\n\n'
    MO.write(tex_body)
    tex_task = r'\begin{displaymath}' + '\n\t' + f'{a1}' + 'x_1' + '+' + f'{b1}' + r'x_2 \rightarrow min' + '\n' + r'\end{displaymath}' + '\n' + r'\begin{displaymath}' + '\n\t' + f'{a2}' + 'x_1' + '+' + f'{b2}' + r'x_2 \leq' f'{c2}' + '\n' + r'\end{displaymath}' + '\n' + r'\begin{displaymath}' + '\n\t' + f'{a3}' + 'x_1' + '+' + f'{b3}' + r'x_2 \leq' f'{c3}' + '\n' + r'\end{displaymath}' + '\n' + r'\begin{displaymath}' + '\n\t' + f'{a4}' + 'x_1' + '+' + f'{b4}' + r'x_2 \leq' f'{c4}' + '\n' + r'\end{displaymath}' + '\n'
    MO.write(tex_task)
    MO.write(r"\vspace{55}" + '\n')

def printAnswer_tex(a1, b1, a2, b2, c2, a3, b3, c3, a4, b4, c4, year, var, min):
    tex_title = r'\begin{center}' + '\n\t' + r'Методы оптимизации -- ' + f'{year}' + '.' + '\n\t' + r'\textbf{Выполнил ........................................................... группа ..........' + '\n' + r'Задание по теме <<Графический метод решения задачи ЛП>>, ' 'вариант ' + f'{var}' + r'}' + '\n' + r'\end{center}' + '\n\n'
    MO1.write(tex_title)
    tex_body = r'\begin{flushleft}' + '\n\t' + r'\textit{    Привести к каноническому виду, построить двойственную задачу следующей задачи линейного программирования $(x_1,x_2 \geq 0)$. Угловым точкам $D$ сопоставить базисные множества.}' + '\n' + r'\end{flushleft}' + '\n\n'
    MO1.write(tex_body)
    tex_task = r'\begin{displaymath}' + '\n\t' + f'{a1}'+'x_1' + '+' + f'{b1}'+ r'x_2 \rightarrow' + f'{min}'  + '\n' + r'\end{displaymath}' + '\n' + r'\begin{displaymath}' + '\n\t' + f'{a2}' + 'x_1' + '+' + f'{b2}' + r'x_2 \leq' f'{c2}' + '\n' + r'\end{displaymath}' + '\n' + r'\begin{displaymath}' + '\n\t' + f'{a3}' + 'x_1' + '+' + f'{b3}' + r'x_2 \leq' f'{c3}' + '\n' + r'\end{displaymath}' + '\n' + r'\begin{displaymath}' + '\n\t' + f'{a4}' + 'x_1' + '+' + f'{b4}' + r'x_2 \leq' f'{c4}' + '\n' + r'\end{displaymath}' + '\n '
    MO1.write(tex_task)
    MO1.write(r"\vspace{55}" + '\n')


def main():
    i = 0
    year = 2023
    while i < int(var_entry.get()):
        task = generateTask()
        if task is None:
            i = i - 1
        else:
            min = find_min(task)
            print_tex(task[9], task[10], task[0], task[1], task[2], task[3], task[4], task[5], task[6], task[7],
                      task[8], year, i + 1)
            printAnswer_tex(task[9], task[10], task[0], task[1], task[2], task[3], task[4], task[5], task[6], task[7],
                      task[8], year, i + 1, min)
        i = i + 1
    MO.write(tex_end)
    MO.close()
    MO1.write(tex_end)
    MO1.close()

MO = open("file.tex", "w+", encoding='utf-8')
tex_start = r'\documentclass{article}' + '\n' + r'\usepackage[utf8]{inputenc}' + '\n' + r'\documentclass{article}' + '\n' + r'\usepackage[utf8]{inputenc}' + '\n' + r'\usepackage[english, russian]{babel}' + '\n' + r'\usepackage{mathtools}' + '\n' + r'\usepackage{stackrel}' + '\n' + r'\topmargin=0pt' + '\n' + r'\leftmargin=0pt' + '\n' + r'\oddsidemargin=0pt' + '\n' + r'\usepackage{natbib}' + '\n' + r'\usepackage{fancyhdr}' + '\n' + r'\usepackage{graphics}' + '\n' + r'\usepackage[left=2cm,right=2cm, top=2cm,bottom=2cm,bindingoffset=0cm]{geometry}' + '\n' + '\n' + r'\title{MO}' + '\n' + '\n' + r'\begin{document}' + '\n' + '\n'
tex_end = r'\end{document}'
tex_main = r'\begin{center}'
MO.write(tex_start)
MO1 = open("answer.tex", "w+", encoding='utf-8')
MO1.write(tex_start)

root = tk.Tk()
root.geometry("500x500+200+200")
root.title("Генератор задач для графического метода")
label = tk.Label(root, text="Введите кол-во вариантов: ", font="Arial 18")
label.place(x=10, y=100)
var_entry = tk.Entry(root)
var_entry.place(x=342, y=108)
button = tk.Button(root, text="Cгенерировать файл .tex", command=main)
button.place(x=150, y=150)

root.mainloop()
