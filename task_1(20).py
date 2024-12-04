import json

try:
    with open("Homeworks\\homework_1_recipes.json", "r") as file1, open("Homeworks\\homework_1_markets.json", "r") as file2:
        recipes = json.load(file1)
        markets = json.load(file2)
except FileNotFoundError as e:
    print("File doesn't exist")

def find_store(recipe_name):
    if recipe_name not in recipes:
        return f"Cannot cook this dish: {recipe_name}"
    
    ingredients = set(recipes[recipe_name]["ingredients"])
    visited_markets = []

    while ingredients:  
        best_market = None
        max_found = 0

        for store, products in markets.items():
            found_ingredients_number = len(ingredients & set(products)) 
            if found_ingredients_number > max_found:
                best_market = store
                max_found = found_ingredients_number
        
        if not best_market:
            return f"Ingredients for {recipe_name} cannot be found at any market"
        
        visited_markets.append(best_market)
        ingredients -= set(markets[best_market])

    return f"To cook {recipe_name}, visit the following markets: {', '.join(visited_markets)}"

def main():
    recipe_name = input("Please enter a dish name: ")
    result = find_store(recipe_name)
    print(result)

if __name__ == "__main__":
    main()
