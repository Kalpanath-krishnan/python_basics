class Teacher:
    def __init__(self, name, emp_code, basic_salary, department):
        self.name = name
        self.emp_code = emp_code
        self.basic_salary = basic_salary
        self.department = department
        self.students = []
    
    def add_student_attendance(self, attendance):
        self.students.append(attendance)
    
    def calculate_salary(self):
        da = 0.1 * self.basic_salary  # Dearness Allowance
        hra = 0.15 * self.basic_salary  # House Rent Allowance
        pf = 0.03 * self.basic_salary  # Provident Fund
        net_salary = self.basic_salary + da + hra - pf
        return da, hra, pf, net_salary
    
    def display(self):
        da, hra, pf, net_salary = self.calculate_salary()
        print(f"{'-'*50}")
        print(f"Name           : {self.name}")
        print(f"Empcode        : {self.emp_code}")
        print(f"Department     : {self.department}")
        print(f"Basic salary   : {self.basic_salary}")
        print(f"DA             : {da}")
        print(f"HRA            : {hra}")
        print(f"PF             : {pf}")
        print(f"Net salary     : {net_salary}")
        present_students = [i+1 for i, present in enumerate(self.students) if present == 1]
        absent_students = [i+1 for i, present in enumerate(self.students) if present == 0]
        print(f"List of present students")
        print(*present_students, sep=", ")
        print(f"List of absent students")
        print(*absent_students, sep=", ")
        print(f"{'-'*50}")


def main():
    num_teachers = int(input("Enter the number of teachers: "))
    teachers = []
    
    for _ in range(num_teachers):
        name = input("Enter the name of teacher: ")
        emp_code = input("Enter the code of teacher: ")
        basic_salary = float(input("Enter the basic salary of teacher: "))
        department = input("Enter the department of the teacher: ")
        teacher = Teacher(name, emp_code, basic_salary, department)
        
        num_students = int(input("Enter the number of students: "))
        print("Enter the attendance rollno wise (1-present/0-absent)")
        for _ in range(num_students):
            attendance = int(input())
            teacher.add_student_attendance(attendance)
        
        teachers.append(teacher)
    
    print("\n" + "-"*50 + "\n")
    for teacher in teachers:
        teacher.display()

if __name__ == "__main__":
    main()
