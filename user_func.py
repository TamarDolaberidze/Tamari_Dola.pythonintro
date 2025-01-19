import json
from datetime import datetime
from user_auth import *
from parking_payment import *

parking_data_file = "parkingZones.json"
User_auth = "users.json"

class UserFunctions:
    def __init__(self, user_id):
        self.user_id = user_id #როცა იუზერი log in-ს აკეთებს, user_id გადაეცემა
        self.user_menu()
    
    def user_menu(self): 
        #მომხმარებლის მენიუ, თუ უნდა მანქანის დარეგისტრირება არააქტიურ პარკინგის ზონაში
        while True:
            print("\n--- User Menu ---")
            print("1. Find Available Zone and Register Car in Parking Zone")
            print("2. Remove your car from the parking zone")
            print("3. Check your balance")
            print("4. Leave Account")


            choice = input("Choose an option: ")
            if choice == "1":
                self.register_car_in_zone()  #მანქანის დასარეგისტრირებლად მეთოდის გამოძახება
            elif choice == "2": 
                self.remove_car_from_zone() #მანქანის პარკინგიდან წაშლის მეთოდის გამოძახება
            elif choice == "3":
                self.check_balance() #იუზერის ბალანსის შემოწმების მეთოდის გამოძახება
            elif choice == "4":
                print("👋 Exiting User Menu.")
                break  
            else:
                print("❌ Invalid choice. Please try again.")
                      
    def load_parking_zones(self):
        #მეთოდი ზონების სიად დასაბრუნებლად
        try:
            with open(parking_data_file, "r") as file:
                data = json.load(file)
                return data.get("parking_zones", []) #აბრუნებს ყველა ზონას თავისი მონაცემებით, სიად
            
        except (FileNotFoundError, json.JSONDecodeError):
            print("❌ Error: Parking zones data not found.")
            return None
    
    def list_available_zones(self):
        #მეთოდი აბრუნებს ზონებს, რომლებიც აქტიური არაა
        parking_zones = self.load_parking_zones()
        if not parking_zones:
            return 
        
        #ხელმისაწვდომი ანუ არააქტიური საპარკინგო ზონების სია
        available_zones = [zone for zone in parking_zones if not any(entry['status'] == 'active' for entry in zone['history'])]

        #ხელმისაწვდომი ზონების დაპრინტვა ინდექსით
        if available_zones:
            print("\n🚗 Available Parking Zones:")
            index = 1
            for zone in available_zones:
                print(f"{index}. {zone['name']} (Address: {zone['address']}, Price: {zone['price']}$)")
                index += 1
            return available_zones
        else:
            print("❌ No available parking zones.")
            return None
    
    def save_parking_zones(self, parking_zones): #პარკინგის ზონების შესანახად. როცა საჭირო იქნება გამოვიძახებთ
        try:
            with open(parking_data_file, 'w') as file:
                json.dump({"parking_zones": parking_zones}, file, indent=4)
        except Exception as e:
            print(f"❌ Error saving parking zones: {e}")
    
    def register_car_in_zone(self): 
        #მეთოდი ზონაში მანქანის დასარეგისტრირებლად

        #ხელმისაწვდომი პარკირების ზონების გაშვება
        available_zones = self.list_available_zones()
        #თუ ზონები არ არის ხელმისაწვდომი
        if not available_zones:
            return
        
        try:
            #მომხმარებელმა აირჩიოს რიგითი ნომრები იმ ზონების, სადაც დაპარკინგება უნდა (ან ერთი ზონის). გამოყოს მძიმით ან სფეისით
            zone_choices = input("\nEnter the sequence number of the zones you want to park (separate by spaces or commas): ")

            #ქმნის სიას, რომელიც არჩეული რიგის ნომრებს ყველას აქცევს ინტეჯერად და აკლებს ერთს (რადგანაც ხელმისაწვდომი პარკირების სიაში პირველი ელემენტი 0 ინდექსზეა)
            selected_indexes = [int(num) - 1 for num in zone_choices.replace(",", " ").split()]

            #ვამოწმებთ მომხმარებლის მიერ არჩეული ნომერი თუ არის ვალიდურ რეინჯში
            if any(index < 0 or index >= len(available_zones) for index in selected_indexes):
                print("❌ Invalid choice. Please select from the list.")
                return #მეთოდის დაქენსელება, თუ არავალიდური არჩევანია
            
            for index in selected_indexes:

            #თუ ვალიდური არჩევანია, ხელმისაწვდომი ზონებიდან selected_zone-ს ვანიჭებთ მომხმარებლის მიერ არჩეულ ზონას
                selected_zone = available_zones[index]

                #მომხმარებელს ვთხოვთ მანქანის ნომრის შეყვანას
                license_plate = input("Enter your car's license plate: ")

                #ახლანდელ დროს ვუთითებთ საწყის დროდ
                start_time = datetime.now()

                #ვქმნით ახალ ელემენტს მომხმარებლის მიერ არჩეულ ზონაში დასამატებლად
                new_entry = {
                    "license_plate": license_plate,
                    "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "Owner_id": self.user_id, 
                    "end_time": "",
                    "status": "active"}

                #გავუშათ ახლანდელი ზონები ჯსონ ფაილიდან
                parking_zones = self.load_parking_zones() 

                #თუ არ ეშვება ფაილი, ვაქენსელებთ მეთოდს
                if parking_zones is None:
                    return

                #პარკირების ზონების ჯსონ ფაილში ციკლით მივყვებით თითოეულ ზონას, რათა ვიპოვოთ მომხმარებლის მიერ არჩეული ზონა
                for zone in parking_zones:
                    if zone["name"] == selected_zone["name"]:
                        zone["history"].append(new_entry) #დავამატოთ ახალი ელემენტი 
                        break #სწორ ზონას როცა ვიპოვით, გავაჩეროთ ციკლი
                
                self.save_parking_zones(parking_zones) #შევინახოთ დააფდეითბული პარკინგის ზონები ჯსონ ფაილში

                #ვაცნობოთ მომხმარებელს, რომ მისი მანქანა წარმატებით დარეგისტრირდა ზონაში
                print(f"✅ Car registered successfully in {selected_zone['name']}.")

        except ValueError: #როცა არავალიდურ choice number-ს შეიყვანს მომხმარებელი
                print("❌ Please enter a valid number.")

    def remove_car_from_zone(self):
        #მეთოდი შესაბამისი პარკინგის ზონიდან მანქანის წასაშლელად
        parking_zones = self.load_parking_zones()

        if not parking_zones:
            return

        #ვქმნით ჯერ ცარიელ სიას, რომელშიც ჩაეწერება იუზეირის აიდის შესაბამისი ზონა და ზონის ელემენტი, რომელის სტატუსიც აქტიურია
        user_parking_history = []
        for zone in parking_zones:
            for entry in zone['history']:
                if entry.get('Owner_id') == self.user_id and entry.get('status') == 'active': #get მეთოდი, რათა მივწვდეთ ლექსიკონის key-ს 
                    user_parking_history.append((zone, entry))

        if not user_parking_history:
            print("❌ You don't have any active parking reservations.")
            return

        #მომხმარებელს ჩამოვუწერთ აქტიურ ზონებს, რომლებშიც მათი მანქანაა დაპარკინგებული, ზონას თან მოყვება მანქანის ნომერი, დაწყებისა და დასრულების თარიღი
        print("\n🚗 Your active parking zones:")
        index = 1
        for zone, entry in user_parking_history:
            print(f"{index}. {zone['name']} (License Plate: {entry['license_plate']}, Start Time: {entry['start_time']}, End Time: {entry['end_time']})")
            index += 1

        try:
            #მომხმარებელს ვთხოვთ ჩამოთვლილი ზონებიდან აირჩიოს ზონების რიგითი ნომრები, რომლებიდანაც უნდა მანქანის წაშლა (სტატუსის შეცვლა)
            zone_choices = input("\nEnter the sequence numbers of the zones to remove your car from (separate by spaces or commas): ")
            #ქმნის სიას, რომელიც არჩეული რიგის ნომრებს აქცევს ინტეჯერად და ყველას აკლებს ერთს (რადგანაც user_parking_history სიაში პირველი ელემენტი 0 ინდექსზეა)
            selected_indexes = [int(choice.strip()) - 1 for choice in zone_choices.replace(",", " ").split()]

            #ვამოწმებთ მომხმარებლის მიერ არჩეული ნომერი თუ არის ვალიდურ რეინჯში
            if any(index < 0 or index >= len(user_parking_history) for index in selected_indexes):
                print("❌ Invalid selection.")
                return

            # იტერაცია selected_index სიაზე და მანქანის სტატუსის შეცვლა "expired"-ზე
            for selected_choice in selected_indexes:
                #user_paking_history არის tuple-ებისგან შემდგარი სია, ხდება ზონისა და ზონის tuple ელემენტების unpacking
                zone_choices, selected_entry = user_parking_history[selected_choice]
                
                #end_time-ის დაყენება ზონის სტატუსშესაცვლელ ელემენტზე
                selected_entry['end_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                #სტატუსის ცვლილება "expired-ზე"
                selected_entry['status'] = 'expired'
                
                #პარკინგის გადახდის ფუნქციის მეთოდის გამოძახება, რათა დაიჩარჯოს და დააფდეითდეს ბალანსი
                print(f"Processing payment for car with license plate {selected_entry['license_plate']}...")
                ParkingPayment.parking_payment(self.user_id, selected_entry['license_plate'])


            # შეინახე დააფდეითბული საპარკინგე ზონები ან ზონიდან
            self.save_parking_zones(parking_zones)

            # დააკონფირმე მანქანის წაშლა საპარკინგე ზონებიდან ან ზონიდან
            print(f"✅ Selected cars removed from the parking zones.")

        except ValueError:
            print("❌ Please enter valid numbers.")
    
    def check_balance(self):
        #მეთოდი, რომელიც მომხმარებელს შეამოწმებინებს ბალანსს და გამოუთვლის რამდენი აქვს გადასახდელი
 
        try:
            with open (User_auth, "r") as file:
                users = json.load(file)

                #ვიპოვოთ იუზერი მისი აიდით
                user = next((user for user in users if user["user_id"] == self.user_id), None)

                if user:
                  #ხელმისაწვდომი ზონების (სადაც იუზერის აქტიური მანქანაა) გასაშვებად მეთოდის გამოძახება
                    parking_zones = self.load_parking_zones()
                if not parking_zones:
                    return

                total_fee = 0 #ზონებისთვის/ზონისთვის მთლიანი გადასახადის ინციალიზება
                active_cars_fees = [] #სია თითოეული აქტიური მანქანის გადასახადის შესანახად

                #საბოლოო ინფორმაციის გამოტანა მომხმარებლისთვის
                print(f"Your current balance is {user['balance']} $.") #ახლანდელი ბალანსის ჩვენება

                #იტერაცია პარკინგის ზონებზე, რათა აქტიური entry-სთვის გამოვითვალოთ მთლიანი გადასახადი
                for zone in parking_zones:
                    for entry in zone['history']:
                        if entry.get('Owner_id') == self.user_id and entry.get('status') == 'active':
                            
                            #start_time-ის სტრინგს ვპარსავთ და ვაქცევთ datetime ობიექტად
                            start_time = datetime.strptime(entry["start_time"], "%Y-%m-%d %H:%M:%S")

                            end_time = datetime.now()  #ახლანდელი დრო ხდება end_time
                            
                            duration = (end_time - start_time).total_seconds() / 3600  #პარკინგის ხანგრძლივობა საათებში
                            
                            zone_fee = duration * zone["price"] #გადასახადის გამოთვლა ზონისთვის

                            total_fee += zone_fee #ყველა ზონების/ზონის გადასახადის გამოთვლა

                            active_cars_fees.append({
                                'license_plate': entry['license_plate'],
                                'zone_name': zone['name'],
                                'fee': zone_fee
                            }) #აქტიური მანქანების გადასახადის ზემოთ ინიციალიზებულ ლისთს ვამატებთ გადასახადის შესახებ ინფორმაციას თითოეული ზონისა და მანქანისთვის (თუ ერთზე მეტი ასეთი მაქანაა, ერთზე მეტისთვის)


                if active_cars_fees:
                    print(f"\nTotal amount to pay for active parking sessions: {total_fee:.2f} $.") #საერთო გადასახადის ჩვენება ყველა ზონისთვის/ერთი ზონისთვის

                    print("\nPayment details for active parking sessions:")
                    for car in active_cars_fees:
                        print(f"  - Car {car['license_plate']} in {car['zone_name']}: {car['fee']:.2f} $") #თითოეული ზონის, მანქანისა და გადასახადის ინფორმაციის გამოტანა
                else:
                    print("❌ You don't have any active parking sessions.")
    
        except Exception as e:
            print(f"❌ Error checking balance: {e}")