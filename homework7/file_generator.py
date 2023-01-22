import phonebook as p


def write_to_file(filename):
    with open(filename, 'w', encoding="utf-8") as f:
        for key, value in p.phonebook.items():
            f.write(f'{key}: {value} \n')


def read_phonebook_from_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        if not f.readline():
            return {}
        else:
            lines = f.readlines()
            for line in lines:
                key, *value = line.split(':')
                p.phonebook[key] = value
            return p.phonebook
