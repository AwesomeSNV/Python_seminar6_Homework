# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text_str = 'Напишите програбвмму, удабвляющую из текста абвсе слова, содержабвщие ""абв"".'
print(text_str)
print(" ".join(list(filter(lambda x: 'абв' not in x, text_str.split(" ")))))