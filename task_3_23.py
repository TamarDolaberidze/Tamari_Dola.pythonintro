class Student:
    def __init__(self, name):
        self._name = name  
        self._scores = []  
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def scores(self):
        return self._scores
    
    def add_score(self, score):
        if 0 <= score <= 100: 
            self._scores.append(score)
        else:
            print("Invalid score")  
    
    def get_average(self):
        if len(self._scores) == 0:
            return 0  
        return sum(self._scores) / len(self._scores)
    
    def get_scores(self):
        return self._scores

def main():
    students = [
        Student("Ana"),
        Student("Lela"),
        Student("Sandro"),
        Student("Tekla")
    ]
    
    students[0].add_score(85)
    students[0].add_score(90)

    students[1].add_score(78)
    students[1].add_score(82)

    students[2].add_score(88)
    students[2].add_score(92)

    students[3].add_score(75)
    students[3].add_score(80)

    students[0].add_score(105) 

    new_student = Student("Dato")
    new_student.add_score(60)
    new_student.add_score(70)

    for student in students:
        print(f"{student.name}'s scores: {student.get_scores()} | Average: {student.get_average():.2f}")

    print(f"{new_student.name}'s scores: {new_student.get_scores()} | Average: {new_student.get_average():.2f}")

if __name__ == "__main__":
    main()
