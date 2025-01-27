class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Person: {self.first_name} {self.last_name}, Age: {self.age}"

    def info(self):
        return str(self)

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}, ID: {self.student_id}"

    def info(self):
        return str(self)

class GroupLimitError(Exception):
    """Custom exception for exceeding the student limit in a group."""
    pass

class Group:
    MAX_STUDENTS = 10

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= self.MAX_STUDENTS:
            raise GroupLimitError("Cannot add more than 10 students to the group.")
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise ValueError("Only instances of Student can be added.")

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def remove_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)
            return True
        return False

    def __str__(self):
        if not self.students:
            return "The group is empty."
        return "\n".join(str(student) for student in self.students)

# Пример использования
if __name__ == "__main__":
    group = Group()

    student1 = Student("Alice", "Smith", 20, "S001")
    student2 = Student("Bob", "Brown", 21, "S002")
    student3 = Student("Charlie", "Davis", 22, "S003")
    student4 = Student("David", "Evans", 23, "S004")
    student5 = Student("Ella", "Frank", 24, "S005")
    student6 = Student("Frank", "Green", 25, "S006")
    student7 = Student("Grace", "Hill", 26, "S007")
    student8 = Student("Hannah", "Irwin", 27, "S008")
    student9 = Student("Ian", "Jones", 28, "S009")
    student10 = Student("Jack", "King", 29, "S010")
    student11 = Student("Kelly", "Lewis", 30, "S011")

    try:
        group.add_student(student1)
        group.add_student(student2)
        group.add_student(student3)
        group.add_student(student4)
        group.add_student(student5)
        group.add_student(student6)
        group.add_student(student7)
        group.add_student(student8)
        group.add_student(student9)
        group.add_student(student10)

        print("Initial group:")
        print(group)

        print("\nAttempting to add an 11th student:")
        group.add_student(student11)
    except GroupLimitError as e:
        print(f"Error: {e}")

    print("\nGroup after all operations:")
    print(group)
