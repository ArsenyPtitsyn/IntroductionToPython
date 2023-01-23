import phonebook as p
import os

def write_to_file(filename):
    with open(filename, 'w', encoding="utf-8") as f:
        for key, value in p.phonebook.items():
            f.write(f'{key}:{value[0]}, {value[1]}, {value[2]}, {value[3]}\n')

def read_phonebook_from_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        if os.path.getsize('phonebook.txt') == 0:
            return {}
        else:
            lines = f.readlines()
            for line in lines:
                key = line.split(':')[0]
                value = line.split(':')[1][:-1].split(', ')
                p.phonebook[int(key)] = value
            return p.phonebook