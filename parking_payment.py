import json
from datetime import datetime

User_auth = "users.json"
parking_data_file = "parkingZones.json"

class ParkingPayment:
    #სტატიკური მეთოდის დეკორატორი, რომელსაც არ ჭირდება ინსტანსი (self)
    @staticmethod
    def parking_payment(user_id, license_plate):
        #გავუშვათ მომხმარებელთა მონაცემები ჯსონიდან
        try:
            with open(User_auth, "r") as file:
                users = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            print("❌ Error loading users data.")
            return 
        
        #მივწვდეთ იუზერს იუზერ აიდით გაშვებული იუზერების ჯსონ დეითადან
        user = next((user for user in users if user["user_id"] == user_id), None)
        
        if not user:
            print("❌ User not found.")
            return

        #გავუშვათ პარკინგის ზონების ჯსონ ფაილი
        try:
            with open(parking_data_file, "r") as file:
                parking_data = json.load(file)
        except FileNotFoundError:
            print("❌ Parking zones data file not found.")
            return
        except (FileNotFoundError, json.JSONDecodeError):
            print("❌ Error loading parking zones data.")
            return

        #ვიპოვოთ შესაბამისი ზონა და ელემენტი/ჩანაწერი (entry)
        for zone in parking_data["parking_zones"]:
            for entry in zone["history"]:

                 #user_id და license_plate არგუმენტებით და აქტიური სტატუსით ვეძებთ გაშვებულ მომხმარებელთა დეითაში იუზერსFound the active parking entry
                if entry.get("license_plate") == license_plate and entry.get("Owner_id") == user_id and entry["status"] == "active":
                    
                    #start_time-ის სტრინგს ვპარსავთ და ვაქცევთ datetime ობიექტად
                    start_time = datetime.strptime(entry["start_time"], "%Y-%m-%d %H:%M:%S")
                    #end_time აქტიურებში ცარიელია და ვანიჭებთ ახლანდელ დროს
                    end_time = datetime.now()
                    
                    #ვითვლით პარკინგის ხანგრძლივობას საათებში
                    duration = (end_time - start_time).total_seconds() / 3600
                    
                    #პარკინგის გადასახადის დათვლა
                    price_per_hour = zone["price"]
                    total_fee = duration * price_per_hour
                    
                    #იუზერის ბალანსს ვაკლებთ მთლიან გადასახადს
                    current_balance = float(user["balance"])
                    new_balance = current_balance - total_fee
                    
                    #ვამოწმებთ ახლად დათვლილი ბალანსი ნულზე მეტი თუა
                    if new_balance < 0:
                        print(f"❌ Insufficient balance. You need {total_fee - current_balance} more.")
                        return
                    
                    #იუზერის ბალანსის დააფდეითება
                    user["balance"] = str(new_balance)
                    
                    #იუზერის სტატუსისა და end_time-ის დააფდეითება
                    entry["status"] = "expired"
                    entry["end_time"] = end_time.strftime("%Y-%m-%d %H:%M:%S")
                    
                    #შევატყობინოთ იუზერს რამდენი გამოაკლდა ბალანსიდან და რა არის ახალი ბალანსი
                    print(f"✅ Parking fee: {total_fee:.2f}$ has been deducted from your balance.")
                    print(f"Your remaining balance: {new_balance:.2f}$")

                    #იუზერის დააფდეითებულ ბალანსს ვინახავთ იუზერების ჯსონ ფაილში
                    try:
                        with open(User_auth, "w") as file:
                            json.dump(users, file, indent=4)
                    except (FileNotFoundError, json.JSONDecodeError) as e:
                        print(f"❌ Error saving users data: {e}")
                        return

                    #სტატუსისა და დასასრული დროის დააფდეითებულ ინფორმაციას ვინახავთ პარკინგის ზონების ჯსონ ფაილში
                    try:
                        with open(parking_data_file, "w") as file:
                            json.dump(parking_data, file, indent=4)
                    except (FileNotFoundError, json.JSONDecodeError) as e:
                        print(f"❌ Error saving parking zones data: {e}")
                        return
                    
                    return
                
        #შეტყობინება თუ აქტიური პარკინგი ვერ მოიძებნა ამ მანქანისთივს
        print("❌ No active parking found for this vehicle.")

