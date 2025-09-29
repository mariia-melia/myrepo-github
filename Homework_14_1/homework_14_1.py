class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def update_grade(self, new_grade):
        self.average_grade = new_grade

    def display_info(self):
        print(f"Student: {self.name} {self.surname}, Age: {self.age}, Average Grade: {self.average_grade}")


# створюємо об'єкт класу
student1 = Student("Maria", "Melnychuk", 30, 85)

# виводимо початкову інформацію
student1.display_info()

# змінюємо середній бал
student1.update_grade(92)

# ще раз виводимо інформацію
student1.display_info()