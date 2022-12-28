# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def get_polynom_from_fie(filename):
    with open(filename, 'r') as f1:
        s = f1.readline()
        members_of_polygon = s.split(' + ')
    return members_of_polygon

def create_list_of_indicators_of_polynom(members_of_polygon):
    indicators_of_monomials = []
    for i in members_of_polygon:
        if '^' in i:
            parts1, parts2 = i.split('^')
            indicators_of_monomials.append(parts2)
        elif 'x' in i:
            indicators_of_monomials.append('1')
        else:
            indicators_of_monomials.append('0')
    return indicators_of_monomials

members_of_polygon1 = get_polynom_from_fie('file1.txt')
print(members_of_polygon1)
indicators_of_monomials = create_list_of_indicators_of_polynom(members_of_polygon1)
print(indicators_of_monomials)
