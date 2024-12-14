import json
try:
    with open("Homeworks\\homework_1 (1).json", "r") as file:
        departments_file = json.load(file)
except FileNotFoundError as e:
    print("File doesn't exist")

class Department:
    def __init__(self, name, description, employees_data):
        self.name = name
        self.description = description
        self.employees = [Employee(emp["name"], emp["position"], emp["salary"]) for emp in employees_data]
    
    def average_salary(self):
        if not self.employees:
            return 0
        return sum(emp.salary for emp in self.employees)/len(self.employees)
    
    def max_salary(self):
        if not self.employees:
            return 0
        return max(emp.salary for emp in self.employees)

    def min_salary(self):
        if not self.employees:
            return 0
        return min(emp.salary for emp in self.employees)
    
    def positions (self):
        positions_count_dict = {}
        for emp in self.employees:
            if emp.position in positions_count_dict:
                positions_count_dict[emp.position] += 1
            else:
                positions_count_dict[emp.position] = 1
        return positions_count_dict

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = float(salary)

def main():
    departments = []
    for dep_key, dep_value in departments_file.items():
        department = Department(dep_value["name"], dep_value["description"], dep_value["employees"])
        departments.append(department)

    for department in departments:
        print(f"Department: {department.name}")
        print(f"Description: {department.description}")
        print(f"Average Salary: {department.average_salary():.2f}")
        print(f"Maximum Salary: {department.max_salary()}")
        print(f"Minimum salary: {department.min_salary()}")

        for position, count in department.positions().items():
            print(f"Position - {position} : Count - {count}")

        print("-" * 40)  

if __name__ == "__main__":
    main()


