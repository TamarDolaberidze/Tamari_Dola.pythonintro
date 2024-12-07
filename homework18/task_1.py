with open("homework18/data.txt", "r") as file:  
    with open("homework18/small.txt", "w") as new_file_1, \
         open("homework18/high.txt", "w") as new_file_2:
        for line in file:
            sep_line = line.strip().split(",")
            price = float(sep_line[3])
            if price < 10:
                new_file_1.write(line)
            else:
                new_file_2.write(line)
