import view as v
import phonebook as p

def write_to_file(filename):
    with open(filename, 'w', encoding="utf-8") as f:
        for key, value in p.phonebook.items():
            f.write(f'{key}, {value} \n')