
class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []  

    def update_teacher_info(self, new_email):
        self.email = new_email

    def display_teacher_info(self):
        return f"Teacher ID: {self.teacher_id}\nName: {self.first_name} {self.last_name}\nEmail: {self.email}"

    def get_assigned_courses(self):
        return [course.course_name for course in self.assigned_courses]
