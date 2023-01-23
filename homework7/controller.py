import phonebook as p
import view as v
import file_generator as fg

def add_contact():
    contact = []
    name = v.set_name()
    contact.append(name)
    surname = v.set_surname()
    contact.append(surname)
    phonenumber = v.set_phonenumber()
    contact.append(phonenumber)
    comment = v.set_comment()
    contact.append(comment)
    return contact

def add_entry():
    if not p.phonebook:
        key = 1
    else:
        key = max(p.phonebook.keys()) + 1
    p.phonebook[key] = add_contact()
    fg.write_to_file('phonebook.txt')

def delete_entry(id):
    del p.phonebook[id]
    fg.write_to_file('phonebook.txt')

def show_phonebook():
    v.show_phonebook(p.phonebook)

def show_contact(id):
    v.show_contact(str(p.phonebook[id]))

def show_contact_briefly(id):
    v.show_contact_briefly(f'{str(p.phonebook[id][0])}, {str(p.phonebook[id][1])}, {str(p.phonebook[id][2])}')

def print_phonebook_from_file(filename):
    print(fg.read_phonebook_from_file(filename))