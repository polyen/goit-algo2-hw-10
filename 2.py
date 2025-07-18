# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def assign_subject(self, subject):
        if subject in self.can_teach_subjects:
            self.assigned_subjects.add(subject)
        else:
            raise ValueError(f"{self.first_name} {self.last_name} не може викладати {subject}")



def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    result = []

    while uncovered_subjects:
        best_teacher = None
        max_coverage = 0

        for teacher in teachers:
            coverage = len(teacher.can_teach_subjects & uncovered_subjects)
            if coverage > max_coverage:
                best_teacher = teacher
                max_coverage = coverage
            elif coverage == max_coverage and best_teacher and teacher.age < best_teacher.age:
                best_teacher = teacher

        if max_coverage == 0:
            return None


        subjects_to_assign = best_teacher.can_teach_subjects & uncovered_subjects
        for subject in subjects_to_assign:
            best_teacher.assign_subject(subject)
        uncovered_subjects -= subjects_to_assign
        teachers.remove(best_teacher)
        result.append(best_teacher)

    return result



if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [
        Teacher('Олександр', 'Олександр', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
