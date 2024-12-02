from fileinput import input
import re


def parse_input(file_name = "") -> list:

    list = []

    if not file_name:
        file_name = './input.txt'


    for line in input(files=(file_name)):
        data = re.split(r'\s+', line.strip())

        for j in range(0, len(data)):
            data[j] = int(data[j])

        list.append(data)

    return list
