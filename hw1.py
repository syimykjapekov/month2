class Student:
    """Класс Student - описывает студента"""
    def __init__(self, name,age, speciality):
        self.name = name
        self.age = age
        self.speciality =speciality
        self.visit = 0
        self.is_tired = True


    def study  (self, subject):
        """Студент на обучении"""
        self.is_tired = True
        return f"{self.name} изучает предмет: {subject}"

    def rest (self):
        """Студент восстановливает силы"""
        self.is_tired =False
        return f"{self.name} отдохнул и готов к обучению"

    def visit(self):
        """Студент посещает занятие"""
        self.visit += 1
        return f"{self.name} посетил. Всего занятии:{self.visit} "


    def info(self):
        """Информация о студенте"""
        status = "Уставший" if self.is_tired  else "бодрый "
        return (f"Студент {self.name},{self.age} лет, специальность: {self.speciality}"
                f"посещено занятии: {self.visit}, сейчас {status}")

student1 = Student("Саламат", 19, "Программное обеспечение ")
student2 = Student("Канимет", 19, "Бухгалтерский учет")
student3 = Student("Азамат", 19, "Программное обеспечение ")
student4 = Student("Перизат", 19, "Бухгалтерский учет ")

print(student1.info())
print(student2.info())
print(student1.study("Основы алгоритмики"))
print(student1.study("Теоретическая информатика"))
print(student2.study("Методы расчетов"))
print(student2.study("Основы алгоритмики"))
print(student1.visit)
print(student2.visit)
print(student1.rest)
print(student2.rest)
print(student1.info())
print("\n"+ student2.info())
print(student2.study("Микрорасчеты"))

