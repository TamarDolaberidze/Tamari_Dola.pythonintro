import json
from datetime import datetime

user_data_file = "users.json" #მომხმარებლების ფაილი
parking_data_file = "parkingZones.json" #პარკინგის ზონების ფაილი


class AdminMenu:
    def __init__(self):
        self.admin_menu()
    
    #მომხმარებელთა ინფორმაციის გასაშვები ფუნქცია
    def load_user_data(self):
        try:
            with open(user_data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("❌ Error: User data not found.")
            return None
     
    #პარკინგის ზონების ფაილის გასაშვები ფუნქცია, რათა სადაც გვენდომება გავუშვათ
    def load_parking_data(self):
        try:
            with open(parking_data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("❌ Error: Parking zones data not found.")
            return None

    #ფუნქცია ადმინს აძლევს საშუალებას, აირჩიოს ერთი რომელიმე მისი უფლებებიდან
    def admin_menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. View All Registered Users")
            print("2. Edit User Info")
            print("3. Delete a User")
            print("4. View All Parking Zones (Status and Fees)")
            print("5. View Parking History")
            print("6. Add a New Parking Zone")
            print("7. Edit Parking Zone")
            print("8. Delete a Parking Zone")
            print("9. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.view_all_users()
            elif choice == "2":
                self.edit_user_info()
            elif choice == "3":
                self.delete_user()
            elif choice == "4":
                self.get_zone_status()
            elif choice == "5":
                self.view_parking_history()
            elif choice == "6":
                self.add_parking_zone()
            elif choice == "7":
                self.edit_parking_zone()
            elif choice == "8":
                self.delete_parking_zone()
            elif choice == "9":
                print("👋 Exiting Admin Menu.")
                break
            else:
                print("❌ Invalid choice. Please try again.")

    def view_all_users(self): #ყველა მომხმარებლის ნახვის ფუნქცია
        users_data = self.load_user_data()
        if not users_data:
            return ("No users found.")

        print("\n📄 Registered Users:")
        for user in users_data:
            print(f"ID: {user['user_id']}, Username: {user['username']}, Balance: {user['balance']}")

    def edit_user_info(self):
        #ადმინს აძლევს საშუალებას, მომხმარებლის ინფორმაცია დააედითოს
        user_id = input("Enter the User ID to edit:")

        users_data = self.load_user_data()
        if not users_data:
            return ("No users found.")
            
        #ნექსთი აბრუნებს პირველივე მომხმარებლის აიდის, რომელიც ადმინის შეყვანილ აიდის ემთხვევა
        user = next((u for u in users_data if str(u["user_id"]) == user_id), None)
        if user: 
            print("\nEditing User:")
            print(f"Current Username: {user['username']}")
            new_username = input("Enter new username (or press Enter to keep the same): ")
            print(f"Current Password: {user['password']}")
            new_password = input("Enter new password (or press Enter to keep the same): ")
            print(f"Current Balance: {user['balance']}")
            new_balance = input("Enter new balance (or press Enter to keep the same): ")

        # მომხმარებლების მონაცემების დარედაქტირება ჯსონ ფაილში
            if new_username:
                user['username'] = new_username
            if new_password:
                user['password'] = new_password
            if new_balance:
                user['balance'] = new_balance

            with open(user_data_file, 'w') as file:
                json.dump(users_data, file, indent=4)

            print("✅ User info updated successfully.")
        else:
            print("❌ User not found.")

    def delete_user(self):
        #ადმინს აძლევს საშუალებას, წაშალოს მომხმარებელი
        user_id = input("Enter the user ID to delete: ")

        users_data = self.load_user_data()
        if not users_data:
            return ("No users found.")
       
        updated_users = [user for user in users_data if str(user["user_id"]) != user_id]  

        if len(updated_users) < len(users_data):
            with open(user_data_file, 'w') as file:
                json.dump(updated_users, file, indent=4)
            print("✅ User deleted successfully.")
        else:
            print("❌ User not found.")

    def get_zone_status(self):
        #ადმინს საშუალებას აძლევს, ნახოს ყველა საპარკინგე ზონა მათი სტატუსისა და გადასახადის
        data = self.load_parking_data()
        if not data:
            return

        parking_zones = data["parking_zones"]
        print("\n📍 Parking Zones Status:")
        for zone in parking_zones:
            #active_slot ეძებს აქტიურ მანქანას ზონაში. პირველივე შემხვედრ აქტიურს რომ ნახავს, any აბრუნებს True ან False-ს
            active_slot = any(entry['status'] == 'active' for entry in zone['history'])
            #პრინტავს ზონის ინფორმაციას სტატუსის გარდა
            print(f"- {zone['name']} (Address: {zone['address']}, Price: {zone['price']}$)")
            #პრინტავს ზონის სტატუსს
            print(f"  Status: {'Occupied' if active_slot else 'Empty'}")
            
            if active_slot:
                total_fee = 0  

                print(f"  Active cars in {zone['name']}:")
                for entry in zone['history']:
                    if entry['status'] == 'active':
                        # აქტიური მანქანებისთვის პარკირების გადასახადის დათვლა
                        start_time = datetime.strptime(entry['start_time'], "%Y-%m-%d %H:%M:%S")
                        end_time = datetime.now()
                        duration = (end_time - start_time).total_seconds() / 3600  
                        price_per_hour = zone['price']
                        fee = duration * price_per_hour  

                        total_fee += fee  

                        print(f"    - Car {entry['license_plate']} (Owner: {entry['Owner_id']}): {fee:.2f}$ for {duration:.2f} hours")

                print(f"  Total amount to be paid for active cars in this zone: {total_fee:.2f}$")


    def view_parking_history(self):
        #ადმინს უბრალოდ საშუალებას აძლევს, ნახოს პარკინგის ისტორია თითოეულ ზონაზე
        data = self.load_parking_data()
        if not data:
            return
        
        parking_zones = data["parking_zones"]

        print("\n📄 Parking History:")
        for zone in parking_zones:
            print(f"\nZone: {zone['name']}")
            for entry in zone['history']:
                print(f"  License Plate: {entry['license_plate']}, Start Time: {entry['start_time']}, End Time:{entry['end_time']}, Status: {entry['status']}")
    
    def add_parking_zone(self):
        #ადმინს საშუალებას აძლევს, დაამატოს ახალი საპარკინგე ზონა
        #სფეისებს ვუშლი დასახელებებს 
        zone_name = input("Enter the new zone name: ").strip()
        address = input("Enter the zone address: ").strip()

        #ფასი უნდა იყოს >= 0-ზე
        while True:
            try:
                price = float(input("Enter the zone price: "))
                if price < 0:
                    print("❌ Price must be greater than or equal to 0. Please try again.")
                    continue
                break
            except ValueError:
                print("❌ Invalid input. Please enter a valid number for the price.")

        data = self.load_parking_data()
        if not data:
            return
        
        parking_zones = data["parking_zones"]
        
        #ვამოწმებ დასახელებას(თუ მსგავსი არსებობს არ დაამატოს, დიდი/პატარა ასოს ვუგუველყოფ)
        for zone in parking_zones:
            if zone["name"].strip().lower() == zone_name.lower():
                print(f"❌ A parking zone with the name '{zone_name}' already exists. Please choose a different name.")
                return
                
    
        new_zone = {
                "name": zone_name,
                "address": address,
                "price": price,
                "history": []
            }
        parking_zones.append(new_zone) #ახალი ზონის დამატება

        with open(parking_data_file, 'w') as file:
            json.dump(data, file, indent=4) #ახალი ზონის ჩაწერა არსებულ ფაილში

        print("✅ New parking zone added successfully.")

    def edit_parking_zone(self):
        #ადმინს საშუალებას აძლევს, დააედითოს საპარკინგე ზონის ინფორმაცია. თუ ზონა აქტიურია (ერთი მანქანა აქტიურია), ვეღარ დააედითებს  
        data = self.load_parking_data()
        if not data:
            return
        
        parking_zones = data["parking_zones"]
                
        print("\n📄 Existing parking zones:")
        for zone in parking_zones:
            active_slot = any(entry['status'] == 'active' for entry in zone['history'])
            print(f"Active: {zone['name']}" if active_slot else f"Non-active: {zone['name']}")
        zone_name = input("Enter the Non-active zone name to edit: ") #ზონის სახელის შეყვანა, რომელიც უნდა დაედითდეს

        zone = next((z for z in parking_zones if z["name"].lower() == zone_name.lower()), None) #გენერატორი next ფუნქციით (აბრუნებს პირველივე match-ს), რათა შევადაროთ ადმინის მიერ შეყვანილი ზონის სახელი ფაილში არსებულს

        if zone:
            active_slot = any(entry['status'] == 'active' for entry in zone['history']) #ამოწმებს ადმინის მიერ დასაედითებელ ზონაში თუ არის აქტიური მანქანა (ანუ ზონის სტატუსი როგორია). True ან False-ს აბრუნებს

            if active_slot: #თუ ზონის სტატუსი აქტიურია, დაედითება ვერ მოხდება
                print("❌ This zone is currently occupied. You cannot edit an occupied zone.")
                return

            #else-ის შემთხვევა, ანუ თუ ზონის სტატუსი expired არის მთლიანად (ყველა მანქანა expired არის). ადმინს ახალი ინფორმაციები შეჰყავს ზონაზე, რიგორც ეს მას სურს
            new_name = input("Enter the new zone name (or press Enter to keep the same): ")
            new_address = input("Enter the new address (or press Enter to keep the same): ")
            new_price = input("Enter the new price (or press Enter to keep the same): ")

            if new_name:
                zone["name"] = new_name
            if new_address:
                zone["address"] = new_address
            if new_price:
                zone["price"] = float(new_price)

            with open(parking_data_file, 'w') as file: #ჩაწერის რეჟიმით ედითდება პარკინგის ზონების ფაილი
                json.dump(data, file, indent=4)

            print("✅ Parking zone updated successfully.")
        else:
            print("❌ Zone not found.")

    def delete_parking_zone(self):
        #ადმინს საშუალებას აძლევს, წაშალოს საპარკინგე ზონა, თუ ის არააქტიურია (ყველა მანქანა expired არის)
        
        zone_name = input("Enter the zone name to delete: ") #ადმინს შეყავს ზონის სახელი, რომლის წაშლაც სურს

        data = self.load_parking_data()
        if not data:
            return
        
        parking_zones = data["parking_zones"]

        zone = next((z for z in parking_zones if z["name"].lower() == zone_name.lower()), None) #გენერატორი next ფუნქციით (აბრუნებს პირველივე match-ს), რათა შევადაროთ ადმინის მიერ შეყვანილი ზონის სახელი ფაილში არსებულს

        if zone:
            active_slot = any(entry['status'] == 'active' for entry in zone['history']) #ამოწმებს ადმინის მიერ დასაედითებელ ზონაში თუ არის აქტიური მანქანა (ანუ ზონის სტატუსი როგორია). True ან False-ს აბრუნებს

            if active_slot: #თუ ზონის სტატუსი აქტიურია, დაედითება ვერ მოხდება
                print("❌ This zone is currently occupied. You cannot delete an occupied zone.")
                return

            parking_zones.remove(zone) #თუ ზონის სტატუსი არააქტიურია, წაიშლება ზონა 

            with open(parking_data_file, 'w') as file: #ჩაწერის რეჟიმით ედითდება პარკინგის ზონების ფაილი
                json.dump(data, file, indent=4)

            print("✅ Parking zone deleted successfully.")
        else:
            print("❌ Zone not found.")


