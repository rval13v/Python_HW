class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Внесён депозит на сумму {amount}. Текущий баланс: {self._balance}")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Снято {amount}. Текущий баланс: {self._balance}")
        else:
            print("Недостаточно средств на счету.")

    def get_balance(self):
        return self._balance


account = BankAccount(initial_balance=0)

menu = {
    "1": {"desc": "Показать баланс", "func": lambda: print(f"Текущий баланс: {account.get_balance()}")},
    "2": {"desc": "Внести деньги на счет", "func": lambda: account.deposit(float(input("Введите сумму пополнения: ")))},
    "3": {"desc": "Снять деньги со счета", "func": lambda: account.withdraw(float(input("Введите сумму снятия: ")))},
    "0": {"desc": "Выход", "func": exit}
}

def main():
    while True:
        print("\nМеню:")
        for key, item in menu.items():
            print(f"{key}. {item['desc']}")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "0":
            print("Выход из программы.")
            break
        elif choice in menu:
            action = menu[choice]['func']
            if callable(action):
                action()
        else:
            print("Неверный выбор. Повторите ввод.")

if __name__ == "__main__":
    main()
    


 
