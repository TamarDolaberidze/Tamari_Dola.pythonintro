def x(*producers, launch_year = 2024):
    if not producers:
        return "enter the producer"
    else:
        print("Producers: ", end = "")
        for producer in producers:
            print(f" - {producer}", end = "")
    print()
    return f"Launch year: {launch_year}"

result1 = x("mazda", "chevrolet")
print(result1)
result2 = x("mazda", "mercedes", launch_year = 1997)
print(result2)



