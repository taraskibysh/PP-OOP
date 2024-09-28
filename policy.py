import uuid


class Insurance:
    def __init__(self, type, **kwargs):
        self._id = uuid.uuid4()
        self.type = type

    def count_cost(self, cost):
        return cost

    def is_possible_to_insure(self):

        pass

    @staticmethod
    def rules():
        print("Auto Insurance rules :\n"
              " 1. Your car must be manufactured after 1960 \n"
              " 2. We do not insure the following car brands: Acura, Chery, VAZ\n"
              "Health Insurance Rules:\n"
              " 1. You must be younger than 60 years old.\n"
              "House Insurance Rules :\n"
              " 1. Your house should be larger than 60 square meters.\n"
              " 2. We do not insure properties in terrorist countries.\n")
    def ID(self):
        print(self._id)

class AutoInsurance(Insurance):
    def __init__(self, name, year, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.year = year

    def count_cost(self, cost):
        if self.year < 2010:
            cost *= 2
        elif self.year >= 2022:
            cost *= 1.5  # Використовуйте крапку для десяткових дробів

        if self.type.lower() == "half":
            cost /= 2
        elif self.type.lower() == "quarter":
            cost /= 4

        return cost

    def is_possible_to_insure(self):
        if self.year < 1960:
            print("Your car is to old for insurance")
            return False
        if self.name in ["Chery", "Acura", "VAZ"]:
            print("You model isn't supported yet")

            return False
        return True


class HealthInsurance(Insurance):
    def __init__(self, age, health_status, **kwargs):
        super().__init__(**kwargs)
        self.age = age
        self.health_status = health_status

    def count_cost(self, cost):
        if self.age > 50:
            cost *= 2
        if self.health_status not in ["good", "normal"]:
            cost *= 3

        if self.type.lower() == "half":
            cost /= 2
        elif self.type.lower() == "quarter":
            cost /= 4

        return cost

    def is_possible_to_insure(self):
        if self.age > 60:
            print("You are to old for insurance")
            return False
        return True


class HouseInsurance(Insurance):
    _BlackListCountry = ["Russia", "China", "Vietnam", "Cuba"]
    _ExpensiveCountry = ["USA", "Italy", "Germany", "Japan"]

    def __init__(self, country, area, **kwargs):
        super().__init__(**kwargs)
        self.country = country
        self.area = area

    def count_cost(self, cost):
        if self.area > 150:
            cost *= 2
        if self.country in self._ExpensiveCountry:
            cost *= 3

        if self.type.lower() == "half":
            cost /= 2
        elif self.type.lower() == "quarter":
            cost /= 4

        return cost

    def is_possible_to_insure(self):
        if self.area < 60:
            print("Your area is too small for insurance")
            return False
        if self.country in self._BlackListCountry:
            print("You house placed in terroristic country")
            return False
        return True


class FullInsurance(AutoInsurance, HealthInsurance, HouseInsurance):
    def __init__(self, type, name, model, year, age, health_status, country, area):
        super().__init__(type=type, name=name, model=model, year=year,
                         age=age, health_status=health_status, country=country, area=area)

    def count_cost(self, auto_cost, health_cost, house_cost):
        final_cost = 0
        final_cost += AutoInsurance.count_cost(self, auto_cost)
        final_cost += HealthInsurance.count_cost(self, health_cost)
        final_cost += HouseInsurance.count_cost(self, house_cost)
        return final_cost

    def is_possible_to_insure(self):
        n1 = AutoInsurance.is_possible_to_insure()
        n2 = HealthInsurance.is_possible_to_insure()
        n3 = HouseInsurance.is_possible_to_insure()

        if n1 and n2 and n3:
            return True
        else:
            return False


