from admin_auth import *
from admin_menu import *
from user_register import *
from user_auth import *
from user_func import *


# 🚀 Main Program
def main():
    #თავიდან ვირჩევთ ადმინის შესვლას, იუზერის შესვლას ან იუზერის რეგისტრაციას
    while True:
        print("\n1. Login Admin")
        print("2. Register User")
        print("3. Login User")
        
        answer = input("Enter your choice(1,2 or 3): ")

        if answer == "1":
            #load_admin_credentials გადაეცემა ადმინისტრატორის იუზერი და პაროლი
            username, password = load_admin_credentials(admin_auth) 
            #თუ იუზეირნეიმი ან პაროლი ვერ მოიძებნა გამოდის სისტემიდან
            if username is None or password is None:
                print("Exiting the system.")
                return #თიშავს პროგრამას, თუ credentials არ იძებნება

            #მოწმდება ადმინის მიერ შეყვანილი მონაცემები
            admin = AdminAuth(username, password)
            if admin.login():
                print("\n🚗 Parking Zone Management System Loading...")
                AdminMenu()
            else:
                print("Exiting the system.")
                return
        elif answer == "2":
            
            user_manager = UserManager()

            while True:
                print("\n1. Start registration")
                print("2. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    balance = input("Enter a balance: ")
                    user_manager.register_user(username, password, balance)
                    return
                elif choice == "2":
                    print("Exiting the program.")
                    return
                else:
                    print("Invalid choice. Please try again.")
        elif answer == "3":
          #load_user_credentials გადაეცემა იუზერის იუზერნეიმი და პაროლი
            users_all = load_user_credentials(User_auth)
            #თუ ფაილი ვერ მოიძებნა გამოდის სისტემიდან
            if not users_all:
                print("Exiting the system.")
                return

            #მოწმდება მომხმარებლის მიერ შეყვანილი მონაცემები
            users_element = UserAuth(users_all)
            if users_element.login():
                print("\n🚗 Parking Zone Management System Loading...")
                
                #მას შემდეგ, რაც მომხმარებელი წარმატებით გააკეთებს log in-ს, UserFunctions კლასს user_id გადაეცემა
                UserFunctions(users_element.get_user_id())
            else:
                print("Exiting the system.")
                return 
            
        else:
            print("Please enter the correct number (1, 2 or 3)")
            restart_answer = input("restart? y or n: ")
            if restart_answer == "y":
                main()
            elif restart_answer == "n":
                print("Exiting the system")
                return
            else:
                print("incorrect answer")
                return


# Run the program
if __name__ == "__main__":
    main()





