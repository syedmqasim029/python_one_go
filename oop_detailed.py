class Atm:
    
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.__menu()
        
    def create_pin(self):
        self.__pin = input("Enter new pin: ")
        print("Pin created successfully")
        
    def check_balance(self):
        pin = input("Enter pin: ")
        if pin == self.__pin:
            print(f"Your balance is {self.__balance}")
        else:
            print("Invalid pin")
        
    def withdraw(self):
        pin = input("Enter pin: ")
        if pin == self.__pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdraw successful. Balance: {self.__balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")
            
    def deposit(self):
        pin = input("Enter pin: ")
        if pin == self.__pin:
            amount = int(input("Enter amount to deposit: "))
            self.__balance += amount
            print(f"Deposit successful. Balance: {self.__balance}")
        else:
            print("Invalid pin")

    def __menu(self):
        while True:
            choice = input("""
        1. Create Pin
        2. Check Balance
        3. Withdraw
        4. Deposit
        5. Exit
        Choose an option: """)

            if choice == "1":
                self.create_pin()
            elif choice == "2":
                self.check_balance()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.deposit()
            elif choice == "5":
                print("Thank you for using ATM")
                break
            else:
                print("Invalid choice")
atm = Atm()



