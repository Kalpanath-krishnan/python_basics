class Employee:
    def __init__(self, ename, ecode, ebs):
        self.emp_name = ename
        self.emp_code = ecode
        self.emp_basic = ebs
        self.emp_da = 0
        self.emp_hra = 0
        self.emp_pf = 0
        self.emp_ns = 0
    
    def calculate(self):
        # Calculation without the last condition
        if self.emp_basic <= 10000:
            self.emp_da = self.emp_basic * 0.2
            self.emp_hra = self.emp_basic * 0.25
            self.emp_pf = self.emp_basic * 0.05
            # Net salary calculation
            self.emp_ns = self.emp_basic + self.emp_da + self.emp_hra - self.emp_pf
        else:
            # If basic salary > 10000, set allowances and net salary to basic salary
            self.emp_da = 0
            self.emp_hra = 0
            self.emp_pf = 0
            self.emp_ns = self.emp_basic
    
    def display(self):
        print("Name          :", self.emp_name)
        print("Empcode       :", self.emp_code)
        print("Basic salary  :", self.emp_basic)
        print("DA            :", self.emp_da)
        print("HRA           :", self.emp_hra)
        print("PF            :", self.emp_pf)
        print("Net Salary    :", self.emp_ns)


class Teacher(Employee):
    def __init__(self, ename, ecode, ebs, dept):
        super().__init__(ename, ecode, ebs)
        self.department = dept
        self.students = []
    
    def mark_attendance(self, n):
        self.count = n
        print("Enter the attendance (1-present 0-absent)")
        for _ in range(n):
            att = int(input())
            self.students.append(att)
    
    def display_attendance(self):
        # Display present students only
        print("Present students")
        for i in range(self.count):
            if self.students[i] == 1:
                print(f"Student {i + 1}")
    
    def display(self):
        # Display Teacher details
        super().display()
        print("Department    :", self.department)


def main():
    teacher_list = []
    m = int(input("Enter the number of teachers: "))
    
    # Loop to gather teacher details
    for _ in range(m):
        nme = input("Enter your name: ")
        c = int(input("Employee code: "))
        ebs = int(input("Salary: "))
        dept = input("Enter department: ")
        no = int(input("Number of students: "))
        
        # Create Teacher object and calculate salary
        obj = Teacher(nme, c, ebs, dept)
        obj.mark_attendance(no)
        obj.calculate()
        teacher_list.append(obj)
    
    # Display each teacher's details and attendance
    for teacher in teacher_list:
        print("\n------------------Details------------------")
        teacher.display()
        teacher.display_attendance()




