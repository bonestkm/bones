import time
import os

# Анимация бегущего человечка
frames = [
    "  o  \n /|\\ \n / \\ ",
    " \\o/ \n  |  \n / \\ ",
    "  |  \n /o\\ \n / \\ ",
    " \\ / \n  o  \n /|\\ ",
]

# Выводим анимацию
for i in range(8):  # Вращается 8 раз
    os.system("clear")  # Очистка экрана
    print(frames[i % len(frames)])
    time.sleep(0.2)

# Основной код
print("БОНЕС СОЗДАТЕЛЬ КОДА!")
