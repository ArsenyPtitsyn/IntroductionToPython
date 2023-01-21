ids = []
contacts = []
phonebook = {}

def init(ids_list, contacts_list):
    global ids
    global contacts
    global phonebook
    ids = ids_list
    contacts = contacts_list
    phonebook = dict(zip(ids, contacts))