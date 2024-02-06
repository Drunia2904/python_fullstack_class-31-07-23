title = input("Введите название компании ")
title_len = len(title) // 2
new_title = title[title_len:] + title[:title_len]
print(f"Новое название: {new_title}")