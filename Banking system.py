from datetime import datetime
now = datetime.now()
date = now.strftime('%x')
time = now.strftime('%I:%M%p')

import random

database = {
    6785078616: ['Sheriff', 'Ochofie', 'Musa', 'kuch502@gmail.com', 'pwordsheriff'],
    2813251099: [ 'Michael', 'Uchechukwu', 'Ani', 'mavisjnr@gmail.com', 'pwordmikey'],
    2656330584: [ 'Francis', 'Oluchukwu', 'Nnaji', 'winterfrancis54@gmail.com', 'pwordwinter']

}
balance = 10000

def init():
    print ("Welcome to Flintstone Bank")

    have_account = int(input("Do you have an account with us: 1 (Yes) 2 (No) \n"))
    if (have_account == 1):
            login()

    elif(have_account == 2):
            register()

    else:
        print('Invalid Option selected')

def login():
    print('Login to your account')

    account_number_user = int(input("Enter your account number: \n"))
    password = input('Enter your password: \n')

    for account_number, user_details in database.items():

        if (account_number == account_number_user):
            if (user_details[4] == password):

                print('Welcome, %s %s' % (user_details[0], user_details[2]))
                print ('The current date and time is {} and {}'.format(date,time))  
               
                bank_operations()
    
    print ('Password or Account Incorrect, please try again')
    login()

def bank_operations():
    print('What would you like to do today:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
        
    selected_option = int(input('Please, select a transaction: \n'))
        
    if (selected_option == 1):

        withdrawal()

    elif (selected_option == 2):

        deposit()

    elif (selected_option == 3): 
       complaint()
        
    elif (selected_option == 4):
        logout()

    else:
        print ('Invalid Option selected. Please, try again')
 

def register():
    
    print('********** Register **********')

    email = input("Enter a valid email address: \n")
    first_name = input("Enter your first name: \n")
    other_name = input("Enter your other name \n")
    last_name = input("Enter your last name: \n")
    password = input("Create a password for yourself \n")

    account_number = generate_account_number()

    database[account_number] = [first_name, other_name, last_name, email, password, 0]
    
    print('Your account has been created')

    print('*****************************')

    print('Your account number is: %d' % account_number)
   
    print('*****************************')

    login()

def generate_account_number():

    return random.randrange(1111111111, 9999999999)

def get_current_balance(user_details):
    return user_details[5]
    

def withdrawal():

    balance = 10000

    print('******* Withdrawal *******')

    print('Current Balance: N', balance)
            
    amount = eval(input ('Enter an amount to withdraw: \n'))
    if amount < balance:
        currentBal = balance - amount
        print('Collect your cash')
        print('Current Balance: N', currentBal)

    else:
        print('Insufficient funds')
        
    logout()

def deposit():
    balance = 10000

    print(' ******* Deposit ******* ')

    print('Current Balance: N', balance)

    deposit = eval(input ('Enter an amount to deposit: \n'))
    currentBal = deposit + balance
    print ('Your deposit was successsful')
    print ('Current Balance: N', currentBal)
    logout()

def complaint():
    
        print('***** Complaint ******')
        input ('What would you like to report? \n')
        print ('Thank you for contacting us')
        logout()

def logout():
    selected_answer = int(input('Would you like to logout? 1) Yes 2) No \n'))
    
    if (selected_answer == 1):
        exit()

    else:
        bank_operations()



init()
