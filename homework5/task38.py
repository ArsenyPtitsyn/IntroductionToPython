# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Квлицэв Абыевабву прабца итудвлаб цабв у цву абв. Абыпова цваоу цвабв цвавх цэабвф.'

lst_of_words = text.split()

res_text = ' '.join(list(filter(lambda x: 'абв' not in x, lst_of_words)))

print(res_text)