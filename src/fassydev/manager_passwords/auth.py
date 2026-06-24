import getpass
import random
import time
from src.fassydev.manager_passwords.config import MASTER_PASSWORD, MAX_ATTEMPTS

def authenticate():
    attempts = MAX_ATTEMPTS

    while attempts > 0:
        master_password = getpass.getpass("Введите мастер-пароль: ")
        print("Проверка пароля...")
    
        if master_password == MASTER_PASSWORD:
            print("Доступ разрешен!")
            return True
        else:
            attempts -= 1
            time.sleep(random.uniform(1.5, 3)) 
        
        if attempts > 0:
            print(f"Доступ запрещен! Осталось попыток: {attempts}\n")
        else:
            print("Доступ запрещен! Все попытки исчерпаны. Выход из программы.")
            return False
