import time
import os

# Отримуємо змінні середовища, які ми передали при запуску
ship_type = os.getenv('SHIP_TYPE', 'Unknown')
pilot_level = os.getenv('AUTOPILOT_LEVEL', 'Unknown')

print(f"--- Моніторинг судна: {ship_type} ---")
print(f"--- Рівень автопілота: {pilot_level} ---")

while True:
    print("Статус: Курс стабільний. Перешкод не виявлено...")
    time.sleep(5)  # Чекаємо 5 секунд перед наступним записом