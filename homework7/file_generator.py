import view as v
import phonebook as p

def write_to_file(filename):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(str(p.phonebook))