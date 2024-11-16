import random 

random_numbers = [random.randint(1, 100) for _ in range(100)]

even_count = sum(1 for num in random_numbers if num % 2 == 0)
odd_count = sum(1 for num in random_numbers if num % 2 != 0)

result = {"even": even_count, "odd": odd_count}

print(result)
