import pandas as pd
import numpy as np

#Наш датасет (в виде словаря)
data = {
    "Название": [
        "Attack on Titan", "Death Note", "Fullmetal Alchemist", 
        "One Punch Man", "Naruto", "Steins;Gate", 
        "My Hero Academia", "Tokyo Ghoul", "Sword Art Online", "Demon Slayer"
    ],
    "Год": [2013, 2006, 2009, 2015, 2002, 2011, 2016, 2014, 2012, 2019],
    "Жанр": [
        "Экшен", "Триллер", "Приключения", 
        "Экшен", "Экшен", "Фантастика", 
        "Экшен", "Ужасы", "Фэнтези", "Экшен"
    ],
    "Рейтинг": [9.0, 8.9, 9.1, 8.7, 8.3, 9.0, 8.2, 7.8, 7.2, 8.6],
    "Эпизоды": [87, 37, 64, 12, 220, 24, 113, 12, 25, 26]
}

df = pd.DataFrame(data)

print("--- Наш датасет по аниме ---")
print(df)

print ("\n---Информация о таблице---")
print(df.info())

print("\n---Статистика---")
print(df.describe())

#cамое длинное аниме
longest_anime = df.sort_values(by="Эпизоды", ascending=False).head(1)
print("\n---Самые длинные аниме---")
print(longest_anime[["Название", "Эпизоды"]])

#Аниме с самым высоким рейтингом
top_rated = df.sort_values(by="Рейтинг", ascending=False).head(1)
print("\n---Аниме с самым высоким рейтингом---")
print(top_rated)

#Поиск среднего значения эпизодов из категории Экшен
action_avg = df[df["Жанр"] =="Экшен"]["Эпизоды"].mean()
print(f"\nСреднее количество эпизодов у жанра экшен: {action_avg:.1f}")

# Добавим колонку Длительностb 1 эпизод +- 24 минуты
df["Минут_всего"] = df["Эпизоды"] * 24

# Сохраняем в новый файл
df.to_csv("anime_report.csv", index=False)
print("\n✅ Отчет успешно сохранен в файл 'anime_report.csv'!")