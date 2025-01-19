# ფინალური პროექტი - პარკინგის აპლიკაცია

პროექტი არის ავტომობილის პარკინგის აპლიკაცია, რომელსაც აქვს ადმინისტრატორისა და მომხმარებლის მხარე, თავისი ფუნქციებით. გარდა ამისა, გვაქვს სამი json ფაილი - მომხმარებლების მონაცემების, ადმინისტრატორის აპლიკაციაში შესასვლელი მონაცემებისა და პარკინგის ზონების შესახებ (users.json, adminPsw.json, parkingZones.json). პროექტის ლოგიკა დაწერილია Python-ში.

## აღწერა

- მომხმარბლის მხარეს საჭიროა: რეგისტრაცია, ავტორიზაცია და სხვადასხვა უფლებამოსილება, რომლებიც მომხმარებელს გააჩნია:
    1. ხელმისაწვდომი საპარკინგე ზონის პოვნა და მანქანის იქ დარეგისტრირება;
    2. მანქანის საპარკინგე ზონიდან წაშლა, რის შემდეგაც აუცილებელია არსებული გადასახადი დაიფაროს;
    3. მიმდინარე ბალანსის შემოწმება, გადასახადის გამოთვლა ზონებისთვის/ზონისთვის, სადაც მანქანა აქვს დაპარკინგებული.

- ადმინისტრატორის მხარეს საჭიროა:
    1. ყველა დარეგისტრირებული მომხმარებლის ინფორმაციის ნახვა;
    2. ყველა დარეგისტრირებული მომხმარებლის ინფორმაციის ცვლილება;
    3. მომხმარებლის წაშლა;
    4. ყველა პარკინგის ზონის ნახვა მათი სტატუსისა და გადასახადის მიხედვით;
    5. პარკინგის ისტორიის ნახვა;
    6. ახალი საპარკინგე ზონის დამატება;
    7. საპარკინგე ზონის ცვლილება;
    8. საპარკინგე ზონის წაშლა.

## ტექნიკური იმპლემენტაცია

ყველა ძირითადი ოპერაცია მიყვება ობიექტზე ორიენტირებული პროგრამირების პრინციპებს და გამოყოფილია ცალ-ცალკე მეთოდებად კლასებში, რაც პარკინგის აპლიკაციის წესებსა და ნაბიჯებს მარტივად გასაგებსა და ლოგიკურად თანმიმდევრულს ხდის. ფუნქციები გაწერილია ისე, რომ მათი სხვა ფაილებში დაიმპორტება/გამოყენება შეიძლება. გამოყენებულია სხვადასხვა მონაცემთა სტრუქტურა: სიები, ლექსიკონები, კორტეჟი. გამოყენებულია for და while ციკლები, error handling, context manager, json ფორმატის ფაილები, დეკორატორები და ა.შ. მომხმარებლის ინტერაქცია ხდება კონსოლის ინტერფეისის (CLI) მეშვეობით. მოდულებიდან გამოყენებულია JSON, datetime, getpass მოდულები და მათი სხვადასხვა მეთოდი.

აპლიკაციის მთელი ციკლი კონტროლდება main() ფუნქციიდან: ადმინის აპლიკაციაში შესვლა, მომხმარებლის დარეგისტრირება, მოხმარებლის აპლიკაციაში შესვლა. ამ სამი არჩევანის შედეგად ყველა არსებული კლასის გამოძახება.

## ფუნქციონალი

პროგრამა მოიცავს შემდეგ კლასებსა და მეთოდებს:

1. **class UserAuth**
    ეს კლასი უზრუნველყოფს მოხმარებლის სისტემაში შესვლას

    - login მეთოდი: მომხმარებელს აქვს სამი ცდა მონაცემების სწორად შესაყვანად და სისტემაში შესასვლელად. users.json-ში მის მიერ შეყვანილი ინფორმაციის ძებნა.
    - get_user_id მეთოდი: აბრუნებს მომხმარებლის id-ის.

2. **class User**
    - ეს კლასი აღწერს მომხმარებლის ობიექტს. მას აქვს ოთხი ატრიბუტი:
    user_id: მომხმარებლის უნიკალური ID.
    username: მომხმარებლის სახელი.
    password: მომხმარებლის პაროლი.
    balance: მომხმარებლის თანხის ბალანსი.

3. **class UserManager**

    ეს კლასი გამოიყენება მომხმარებლების მართვისთვის, მათ შორის რეგისტრაციისთვის, მონაცემების შენახვისა და სხვა ოპერაციებისთვის:

    - load_users(): ამ მეთოდით იკითხება users.json ფაილი. თუ ფაილი არ არსებობს ან მასში არ არის მონაცემები, ვაბრუნებთ ცარიელ სიას
    - save_users(): ამ მეთოდით ინახება ყველა მომხმარებლის მონაცემები JSON ფორმატში users.json ფაილში.
    - get_next_id(): ამ მეთოდით გამოითვლება მომდევნო მომხმარებლის ID.
    - register_user(username, password, balance): ამ მეთოდით რეგისტრირდება ახალი მომხმარებელი. პირველ რიგში ხდება username-ის უნიკალურობის შემოწმება, და თუ ეს ეს მომხმარებლის სახელი უკვე არსებობს, მომხმარებელს სთხოვენ შეარჩიოს სხვა. ამის შემდეგ მომხმარებლის მონაცემები ინახება users კორტეჟში, და საბოლოოდ მონაცემები ინახება users.json ფაილში.

4. **class UserFunctions**

    ეს კლასი უზრუნველყოფს მომხმარებლისთვის პარკინგის სისტემის მენიუსა და სხვადასხვა ფუნქციების გამოყენებას, როგორიცაა მანქანის რეგისტრაცია, პარკინგიდან წაშლა და ბალანსის შემოწმება.

    - init კონსტრუქტორი, რომელიც აინიცირებს მომხმარებლის მენიუს გამოჩენას, როდესაც იუზერი შედის სისტემაში.
    - user_menu: მომხმარებლის მენიუს ჩვენება და მისი მოქმედებების დამუშავება (მანქანის რეგისტრაცია, წაშლა, ბალანსი და გამოსვლა).
    - load_parking_zones მეთოდი ტვირთავს პარკინგის ზონების მონაცემებს JSON ფაილიდან.
    - list_available_zones მეთოდი აბრუნებს არააქტიური პარკინგის ზონებს, რომლებიც ხელმისაწვდომია რეგისტრაციისთვის. ასეთ ზონებში ყველა მანქანის სტატუსი expired არის.
    - save_parking_zones მეთოდი ინახავს პარკინგის ზონებს JSON ფაილში, სადაც საჭირო იქნება გამოვიძახებთ.
    - register_car_in_zone მეთოდი არეგისტრირებს მანქანას ხელმისაწვდომ პარკინგის ზონაში.
    - remove_car_from_zone მეთოდი წაშლის მანქანას პარკინგის ზონიდან და განახორციელებს გადახდას.
    - check_balance(self): შემოწმებს მომხმარებლის ბალანსს და ზუსტდება გადასახდელი თანხა აქტიურ პარკირების სესიებზე.

5. **class ParkingPayment**
    ეს კლასი უზრუნველყოფს პარკინგის გადასახადების გამოთვლასა და მომხმარებლის ბალანსის განახლებას პარკინგის სესიის დასრულების შემდეგ.

    - parking_payment არის სტატიკური მეთოდი, რომელიც გადამოწმებს პარკინგის სესიის აქტიურობას, გაიანგარიშებს პარკინგის გადასახადს, განახორციელებს გადახდას და მომხმარებლის ბალანსს განაახლებს.

6. **class AdminAuth**
    ეს კლასი უზრუნველყოფს ადმინისტრატორის სისტემაში შესვლის სერვისს, რომელიც იწვევს მის მიერ შეყვანილი მონაცემების სისწორის შემოწმებასა და შეზღუდულ 3 ცდაში შესვლას.

    - login მეთოდი, რომელიც საშუალებას აძლევს ადმინისტრატორს შევიდეს სისტემაში, მკაცრად ამოწმებს პასვორდის და ადმინის სახელის სისწორეს, და განსაზღვრავს შესვლის ცდების მაქსიმუმს.
    - იმავე admin_auth ფაილში კლასის გარეთ არის load_admin_credentials ფუნქცია, რომელიც კითხულობს JSON (adminPsw.json) ფაილს, სადაც დაცულია ადმინისტრატორის მონაცემები (მ სახელი და პაროლ ი). აბრუნებს ადმინისტრატორის სახელსა და პაროლს.

7. **class AdminMenu**
    ეს კლასი მოიცავს ყველა ადმინისტრატორისთვის საჭირო ფუნქციას, მათ შორის მომხმარებელთა მართვას, პარკინგის ზონების მართვას, ისტორიის ნახვას და ახალი ზონების დამატებას.

    - init(self) ეს კონსტრუქტორი აინიცირებს ადმინისტრატორის მენიუს.
    - load_user_data: მეთოდი ტვირთავს მომხმარებელთა მონაცემებს JSON ფაილიდან.
    - load_parking_data: მეთოდი, რომელიც ტვირთავს პარკინგის ზონების მონაცემებს JSON ფაილიდან.
    - admin_menu: ეს არის მთავარი მენიუ, რომელიც აჩვენებს ადმინისტრატორს ყველა შესაძლო არჩევანს, რათა აირჩიოს ერთი და იმოქმედოს შესაბამისად.
    - view_all_users: მეთოდი ადმინისტრატორს აძლევს საშუალებას, ნახოს ყველა რეგისტრირებული მომხმარებელს.
    - edit_user_info: საშუალებას აძლევს ადმინისტრატორს შეცვალოს კონკრეტული მომხმარებლის მონაცემები.
    - delete_user: აღნიშნავს მეთოდს, რომელიც საშუალებას აძლევს ადმინისტრატორს წაშალოს მომხმარებელი.
    - get_zone_status: აჩვენებს ყველა პარკინგის ზონის სტატუსსა და გადასახადს.
    - view_parking_history: აჩვენებს ყველა პარკინგის ისტორიის ჩანაწერს.
    - add_parking_zone: მეთოდი, რომელიც ახალ პარკინგის ზონის დამატების საშუალებას იძლევა.
    - edit_parking_zone: მეთოდი, რომელიც საშუალებას აძლევს ადმინისტრატორს შეცვალოს პარკინგის ზონის მონაცემები.
    - delete_parking_zone: მეთოდი, რომელიც საშუალებას აძლევს ადმინისტრატორს წაშალოს პარკინგის ზონა, თუ ის არააქტიურია.

## გაშვების ინსტრუქცია

პროგრამის გაშვებისთვის საჭიროა:

1. Python-ის ვერსია 3.8 ან ზემოთ.
2. ფაილის გაშვება ტერმინალში "Run Python File" ბრძანებით.
3. არ არის საჭირო დამატებითი ბიბლიოთეკები.
