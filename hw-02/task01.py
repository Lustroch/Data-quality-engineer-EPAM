# Смоделируйте прием успешно окончивших тренинг студентов на работу в EPAM.
# Вам необходимо будет реализовать класс Student, будущие
# создаваемые объекты которого описываются именем, фамилией, возрастом и набором навыков.
# Говоря о навыках, считается, что все без исключения студенты знают английский язык.

# Также реализуйте в классе следующие методы:

# зачисление на курс (в результате работы которого у объекта-студента изменяется логический атрибут is_learning
# на значение True; метод вызывается автоматически
# при создании объекта);

# обучение (в результате работы которого студенты помимо английского языка, смогут пополнить свой багаж знаний еще
# такими навыками, как SQL, Linux и Python);

# прием на работу (отрабатывает успешно, если студент обладает всеми необходимыми навыками).

# Создайте трех разных студентов. Двоих студентов обучите всем навыкам. Третий, к всеобщему сожалению, не выучит Python.

# Попробуйте принять всех троих на работу.


class Student:
    """Data quality engineer training model at EPAM"""

    def __init__(self, name, sec_name, age, soft_skills):
        """Assign attributes to the student"""
        self.name = name
        self.sec_name = sec_name
        self.age = age
        self.eng_skill = True
        self.soft_skills = soft_skills  # it's graduate from 1 to 5, where 1 is very bad and 5 is very good
        self.enrollment_in_a_course()

    def enrollment_in_a_course(self):
        """Making a logical attribute that the Student is learning now at the training centre"""
        self.is_learning = True

    def training(self, sql, linux, python):
        """Student learns new skills"""
        self.sql = sql
        self.linux = linux
        self.python = python

    def recruitment(self):
        """Recruiment student for work"""
        if self.sql and self.linux and self.python and self.soft_skills >= 3:
            return print(self.name, self.sec_name, 'is hired')
        else:
            return print(self.name, self.sec_name, 'is not hired')


maxim_student = Student('Maxim', 'Bondarenko', 23, 4)
george_student = Student('Georgy', 'Kamensky', 22, 5)
klement_student = Student('Klement', 'Ivanonov', 31, 3)

maxim_student.training(True, True, True)
george_student.training(True, True, True)
klement_student.training(True, True, False)

maxim_student.recruitment()
george_student.recruitment()
klement_student.recruitment()
