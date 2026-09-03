class School:
    
    def __init__(self):
        self.students = {}
        self._added = []

    def add_student(self, name, grade):
        if name in self.students:
            self._added.append(False)
            return

        self.students[name] = grade
        self._added.append(True)

    def roster(self):
        return sorted(
            self.students,
            key=lambda name: (self.students[name], name)
        )

    def grade(self, grade_number):
        return sorted(
            name
            for name, grade in self.students.items()
            if grade == grade_number
        )

    def added(self):
        return self._added