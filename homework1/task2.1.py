# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

bool_list = [True, False]
print(f"x \t\t y \t\t z \t\t ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
for x in bool_list:
    for y in bool_list:
        for z in bool_list:
            bool1 = not(x or y or z)
            bool2 = not x and not y and not z
            print(f'{x} \t {y} \t {z} \t\t\t\t {bool1 == bool2}')

