class Consumer:

    def __init__(self, name, surname, company, salary):
        self.name = name
        self.surname = surname
        self.company = company
        self.salary = salary

    def info(self):
        print(f"{self.name}"
              f"\n{self.surname}"
              f"\n{self.company}"
              f"\n{self.salary}")

    def CheckForInsurance(self, policy, cost):
        if policy.is_possible_to_insure():
            result = policy.count_cost(cost)
            if self.salary / 10 > result:
                print("everything is fine you can be our customer")
            else:
                print("Oops sorry, your salary is too low")

