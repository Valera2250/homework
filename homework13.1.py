class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Возраст: {self.age}"


class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Студент: {self.first_name} {self.last_name}, ID: {self.student_id}, Возраст: {self.age}"


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def find_student_by_last_name(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def remove_student_by_last_name(self, last_name):
        student = self.find_student_by_last_name(last_name)
        if student:
            self.students.remove(student)

    def __str__(self):
        students_info = "\n".join(str(student) for student in self.students)
        return f"Группа: {self.group_name}\nСтуденты:\n{students_info}" if self.students else f"Группа: {self.group_name}\nСтуденты отсутствуют"




student1 = Student("Иван", "Иванов", 20, "S001")
student2 = Student("Петр", "Петров", 21, "S002")
student3 = Student("Анна", "Сидорова", 19, "S003")


group = Group("Группа 1")


group.add_student(student1)
group.add_student(student2)
group.add_student(student3)


print(group)


found_student = group.find_student_by_last_name("Петров")
print("Найденный студент:", found_student)


group.remove_student_by_last_name("Петров")
print("После удаления:")
print(group)
