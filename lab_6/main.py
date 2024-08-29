from bank_customer import BankCustomer


def main():
    customers = [
        BankCustomer("Шевченко", "Ігор", "Дмитрович", "1954-03-09",
                     "AB123456", "Чоловік", 10000, "+380123456789"),
        BankCustomer("Косач", "Марина", "Петрівна", "1991-02-25",
                     "CD654321", "Жінка", 15000, "+380987654321"),
        BankCustomer("Франко", "Григорій", "Іванович", "1986-08-27",
                     "EF789012", "Чоловік", 20000, "+380112233445"),
    ]

    total_credit = sum(customer.credit_amount for customer in customers)
    male_customers = [customer for customer in customers if customer.gender == "Чоловік"]
    average_age_male = sum(customer.get_age() for customer in male_customers) / len(
        male_customers) if male_customers else 0

    for customer in customers:
        print(customer)

    print(f'\nTotal amount of credits: {total_credit} UAH')
    print(f'Average age of male clients: {average_age_male: .2f} years')


if __name__ == "__main__":
    main()