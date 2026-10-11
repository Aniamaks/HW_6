seconds = int(input("Введіть кількість секунд: "))

days, seconds = divmod(seconds, 86400)
hours, seconds = divmod(seconds, 3600)
minutes, seconds = divmod(seconds, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in (2, 3, 4) and days % 100 not in (12, 13, 14):
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")