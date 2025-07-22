#Creating a class Account and it functions
class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            return False, 'The amount must be positive.'

        elif amount > self.balance:
            return False, 'Insufficient funds'

        elif amount <= self.balance:
            self.balance -= amount
            return True, 'Withdraw successfully done!'

        else:
            return False, 'Insert a valid amount.'

    def deposit(self, amount):
        if amount < 0:
            return False, 'Amount must be positive.'

        elif amount > 0:
            self.balance += amount
            return True, 'Deposit successfully done!'

        else:
            return False, 'Insert a valid amount.'


    def statement(self):
        return f"\nHolder: {self.account_holder} | Balance: R${self.balance:.2f}"


accounts = {} #Dictionary of accounts

#First Interface
def first_interface():


    while True:
        print('-'*25)
        print('[1] Create an account')
        print('[2] Log in')
        print('[3] Exit')
        print('-' * 25)

        initial_choice= input('Choose an option:  ').strip()

        #Creating an account
        if initial_choice == '1':
            while True:
                new_username = (input('\nChoose an username (or 0 to cancel):\n')).strip()
                if new_username == '0': #Conditional to return to main menu
                    print('Operation cancelled')
                    break

                elif new_username == '': #Username cannot be just spaces
                    print('Username cannot be empty! Try a valid one')

                elif new_username in accounts:
                    print('This username is already taken, Try a different one.')

                else:
                    try:
                        balance = float(input('Initial balance: R$ '))
                        if balance == 0:
                            print('Operation cancelled')
                            break

                        elif balance < 0:
                            print('Initial balance must be greater than zero.')
                            continue
                        accounts[new_username] = Account(new_username, balance)
                        print('Username successfully created\n')

                        #After creating an account redirect the user to the second interface
                        second_interface(accounts[new_username])

                    except ValueError:
                        print('Invalid balance. Please enter a number')

        elif initial_choice == '2':
            while True:
                login_username = input('\nUsername to log in (type 0 to go back):\n').strip()
                if login_username == '0':
                    print('Operation cancelled')
                    break
                elif login_username in accounts:
                    print(f'Welcome back, {login_username}!\n')
                    second_interface(accounts[login_username])

                else:
                    print('Account not found. Try a valid account')

        elif initial_choice == '3':
            print('Have a great day. Exiting...')
            break

        else:
            print('\nInvalid option. Choose a valid option')

#Interface pós login
def second_interface(account):
#Creating a loop for the second interface
    while True:
        print('-' * 25)
        print('[1] Deposit')
        print('[2] Withdraw')
        print('[3] Statement')
        print('[4] Exit')
        print('-' * 25)

#User input
        choice=input('Choose an option:  ').strip()


        if choice == '1':
            amount_input = input('\nDeposit amount: R$\n(type 0 to cancel)\n').strip()
            if amount_input == '0':
                print('Operation cancelled\n')
                continue

            else:
                amount = float(amount_input)
                success, message = account.deposit(amount)
                print(message)



        elif choice == '2':
            amount_input = input('\nWithdraw amount: R$\n(type 0 to cancel)\n')
            if amount_input == '0':
                print('Operation cancelled')
                continue

            else:
                amount = float(amount_input)
                success, message = account.withdraw(amount)
                print(message)


        elif choice == '3':
            if account:
                print(account.statement())

        elif choice == '4':
            print('Have a great day! Exiting program...')
            break

        else:
            print('Invalid option. Try again')

first_interface()







