class Student:
    def read(self, roll, name, m1, m2, m3):
        self.roll = roll
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.avg = (m1 + m2 + m3) / 3
        print("Students read")

    def write(self):
        print("Student roll:", self.roll)
        print("Student name:", self.name)
        print("Mark 1:", self.m1)
        print("Mark 2:", self.m2)
        print("Mark 3:", self.m3)
        print("Average marks:", self.avg)
        print("Students write")

# --- Example usage ---
s1 = Student()
s1.read(101, "jaya", 88, 89, 90)
s1.write() 