import json

with open("homework18/data.txt", "r") as file:  
    max_sale = 0
    list_users_max = []
    max_sum_price = 0
    ist_users_maxprice = []
    total_price = 0
    total_items = 0
    counter_lines = 0
    list_max_quantity_products = []

    for line in file:
        sep_line = line.strip().split(",")
        items_bought = int(sep_line[2])
        if items_bought > max_sale:
            max_sale = items_bought
            list_users_max = [sep_line[0]]
            list_max_quantity_products = [sep_line[1]]
        elif items_bought == max_sale:
            list_users_max.append(sep_line[0])
            list_max_quantity_products = [sep_line[1]]
    

        quantity = int(sep_line[2])
        price = float(sep_line[3])
        sum_bought_price = quantity * price
        if sum_bought_price > max_sum_price:
            max_sum_price = sum_bought_price
            list_users_maxprice = [sep_line[0]]
        elif sum_bought_price == max_sum_price:
            list_users_maxprice.append(sep_line[0])
        
        total_price += sum_bought_price
        total_items += quantity
        counter_lines += 1
    average_price = total_price / total_items
    average_quantity = total_items / counter_lines

    
    print(f"User with maximum sale quantity is {', '.join(list_users_max)}")
    print(f"User with maximum sum price is {', '.join(list_users_maxprice)}")
    print(f"Average price is {average_price}")
    print(f"Average quantity is {average_quantity}")
    print(f"Maximum sales quantity product is {', '.join(list_max_quantity_products)}")

    dict_data = {"Username" : list_users_max[0],
                 "Max sale" : list_users_maxprice[0],
                 "Average price" : average_price,
                 "Average quantity" : average_quantity,
                 "Product" : list_max_quantity_products[0]}
    print(dict_data)
    
    with open("homework18/stats.json", "w") as json_file:
        json.dump(dict_data, json_file, indent=4)