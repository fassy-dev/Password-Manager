import random
import time
from src.fassydev.manager_passwords.storage import load_data, save_data
from src.fassydev.manager_passwords.generator import generate_password
from src.fassydev.manager_passwords.auth import authenticate

def main():
    print("Добро пожаловать в Менеджер паролей!")

    if not authenticate():
        return

    passwords = load_data()

    while True:
        print("\nВыберите действие:")
        print("1. Посмотреть сохраненные пароли")
        print("2. Добавить новый пароль")
        print("3. Удаление пароля")
        print("9. Выход")

        choice = input("Номер действия: ")

        if choice == "1":
            print("Загрузка базы данных...")
            time.sleep(random.uniform(1.333, 4.3))
            if not passwords:
                print("База данных пуста.")
            else:
                print("\nВаши пароли:")
                for service, credentials in passwords.items():
                    print("---------------")
                    print(f"Сервис: {service}")
                    print(f"Логин: {credentials['login']}") 
                    print(f"Пароль: {credentials['password']}")

        elif choice == "2":
            service = input("Название сервиса: ")
            login = input("Логин: ")
            password = input("Пароль (или нажмите Enter для генерации): ")
            
            if password == "":
                password = generate_password(8)
                print(f"Сгенерирован надежный пароль: {password}")

            print("Загрузка базы данных...")
            time.sleep(random.uniform(1.333, 3.3))
            print("Сохранение данных в базу данных...")
            time.sleep(random.uniform(1, 2.89))

            passwords[service] = {"login": login, "password": password}
            save_data(passwords)
            
            print(f"Пароль для {service} сохранен!")
            print("Что было добавлено в базу данных:")
            print(f"Сервис: {service}")
            print(f"Логин: {login}") 
            print(f"Пароль: {password}")

        elif choice == "3":
            service = input("Введите название сервиса, который хотите удалить: ")

            print("Загрузка базы данных...")
            time.sleep(random.uniform(1.5, 2.3))
            
            if service in passwords:
                del passwords[service]
                save_data(passwords)
                print(f"Пароль для {service} удален")
            else:
                print("Сервис не найден")

        elif choice == "9":
            print("Завершаю работу....")
            time.sleep(random.uniform(0.3, 1.8))
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nЗавершение работы программы")
