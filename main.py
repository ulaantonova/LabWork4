import os
import time

# Зчитуємо режим. Якщо не вказано — буде 'standard'
mode = os.getenv('NAV_MODE', 'standard').lower()
ship_name = os.getenv('SHIP_NAME', 'AutoShip-01')

print(f"--- СИСТЕМА УПРАВЛІННЯ СУДНОМ: {ship_name} ---")

if mode == 'eco':
    print("РЕЖИМ: ECO (Економія палива)")
    print("ПАРАМЕТРИ: Швидкість обмежена до 12 вузлів, оптимізація курсу за течією.")
else:
    print(f"РЕЖИМ: {mode.upper()}")
    print("ПАРАМЕТРИ: Стандартні налаштування ходу.")

print("------------------------------------------")

# Імітація роботи системи
while True:
    print(f"[{time.strftime('%H:%M:%S')}] Статус: Рух у режимі {mode.upper()}... Перешкод немає.")
    time.sleep(5)