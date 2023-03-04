Bank = """
=====================================================
                Welcome To 
             DIGITAL BANK OF INDIA
*****************************************************
------ 1. Open A New Account             ------
------ 2. Withdraw Money                 ------
------ 3. Deposit Money                  ------
------ 4. Check Customers Balance        ------
------ 5. Exit / Quit                    ------
*****************************************************
=====================================================
"""
customers={"suresh":[1122,10000],"ravi":[1234,15000],"tarun":[0000,5000],"surya":[1111,3000]}
while True:
    print(Bank)
    option=int(input("select your choice number above the menu:"))
    if option==1:
        name=input("Enter the full name:")
        def pin_generate(customers):
            pin=int(input("please generate your four digit pin:"))
            if len(str(pin))==4:
                balance=int(input("please enter a amount to deposit to start an account:"))
                customers[name]=[pin,balance]
                print("-----------------------------------------------------")
                print("Name:",name)
                print("Pin:",pin)
                print("Balance:",balance)
                print("---Your name added to the customer system    ---")
                print("---Your pin added to the customer system     ---")
                print("---Your balance added to the customer system ---")
                print()
                print("******New Account Created Successfully******")
                print()
                print(" Note! Please Remember your Name and Pin !")
                print("______________________________________________________")
                key=input(" please press Enter Key to go back to Main Menu to Choose another options or Exist...")
            else:
                print("Please enter 4 digits pin !")
                pin_generate(customers)


        pin_generate(customers)
    elif option==2:
        print("choice number 2 is selected by the customer")
        def check_name(customers):
            name=input("please provide your full name:")
            if name in customers:
                def check_pin (customers):
                    pin=int(input("please provide your four digit pin:"))
                    if pin==customers[name][0]:
                        print("your current balance:",customers[name][1],"/Rs")
                        print()
                        print()
                        def draw_amount (customers):
                            withdraw=int(input("Enter amount to withdraw:"))
                            if withdraw>customers[name][1]:
                                print("###### Insufficient balance ######")
                                print()
                                print("**************************************")
                                draw_amount(customers)
                            else:
                                customers[name][1]-=withdraw
                                print()
                                print("______ withdraw successful_____")
                                print("your new balance:",customers[name][1],"-/Rs")
                                print()
                                print()
                                key=input("please press Enter Key to go back to Main Menu to Choose another options or Exist...")
                        draw_amount(customers)
                    else:
                        print("Enter valid pin !")
                        check_pin(customers)
                check_pin(customers)
            else:
                print("please Enter valid user name:")
                check_name(customers)
        check_name(customers)
    elif option==3:
        print("choice number 3 is selected by the customer")
        def check_name(customers):
            name=input("please provide your full name :")
            if name in customers:
                def check_pin (customers):
                    pin=int(input("please provide your four digit pin:"))
                    if pin==customers[name][0]:
                        print("your current balance:",customers[name][1],"/Rs")
                        print()
                        print()
                        deposit=int(input("Enter amount to deposit:"))
                        customers[name][1]+=deposit
                        print()
                        print("------ Deposit Successful ------")
                        print("your new balance:",customers [name][1],"-/Rs")
                        print()
                        print()
                        key=input("please press Enter key to go back to main menu to choose another options or Exist...")
                    else:
                        print("Enter valid pin: ")
                        check_pin(customers)
                check_pin (customers)
            else:
                print("please Enter valid user name !")
                check_name (customers)
        check_name(customers)
    elif option==4:
        print("choice number 4 is selected by the customer")
        def check_name(customers):
            name=input("please provide your full name:")
            if name in customers:
                def check_pin(customers):
                    pin=int(input("please provide your four digit pin"))
                    if pin==customers[name][0]:
                        print("=======================================================")
                        print("your current balance:",customers[name][1],"/Rs")
                        print()
                        key=input("please press Enter key to go back to main menu to choose another options or Exist..")
                    else:
                        print("Enter valid pin")
                        check_pin (customers)
                check_pin(customers)
            else:
                print("please Enter valid user name:")
                check_name(customers)
        check_name(customers)
        #.........
    elif option==5:
        print("choice number 5 is selected by the customer")
        print("Thank you for using DBI banking system")
        print()
        print()
        print("your done fantastic job")
        print("Have A Nice Day !")
        print("Bye")
        break
    else:
        print("please Enter valid option !")















