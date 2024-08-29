from datetime import datetime


class Person:
    def __init__(self, lastname, firstname, middle_name, birth_date):
        self.lastname = lastname
        self.firstname = firstname
        self.middle_name = middle_name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def __str__(self):
        return (f"Lastname: {self.lastname}, firstname: {self.firstname}, middle name: {self.middle_name},"
                f"age: {self.get_age()}")
