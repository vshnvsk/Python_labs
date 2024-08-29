from person import Person


class BankCustomer(Person):
    def __init__(self, lastname, firstname, middle_name, birth_date,
                 passport_series, gender, credit_amount, phone):
        super().__init__(lastname, firstname, middle_name, birth_date)
        self.passport_series = passport_series
        self.gender = gender
        self.credit_amount = credit_amount
        self.phone = phone

    def __str__(self):
        return (f"{super().__str__()}, passport: {self.passport_series}, gender: {self.gender}, "
                f"credit: {self.credit_amount} UAN, phone number: {self.phone}")