import json

try:
    with open (r"C:\Users\Tamar.Dolaberidze\Desktop\Python\D&O Training\Homeworks\homework_1.json", "r") as file:
        data = json.load(file)
        print(data)
except FileNotFoundError as e:
    print("File doesn't exist")

avg_salaries = {}    

for departments_key, departments_value in data.items():
    employees = departments_value["employees"]
    salaries = []

    for employee in employees:
        salary = employee["salary"] 

        try:
            salary_int = int(salary)
            salaries.append(salary_int)
        except ValueError:
            print("Invalid Salary")
    try:
        average_salary = sum(salaries) / len(salaries)
        avg_salaries[departments_key] = average_salary
    except ZeroDivisionError:
        print("No valid salaries to calculate average")

try:
    with open ("avg_salary.json", "w") as output_file:
        json.dump(avg_salaries, output_file, indent=4)
except Exception as e:
    print("Error while writing an output file", e)
    



