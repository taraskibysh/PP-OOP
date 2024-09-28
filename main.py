from policy import *
from consumer import Consumer



# Виведення правил
Insurance.rules()

# Автострахування
auto_policy = AutoInsurance(type="full", name="Toyota", model="Camry", year=2000)
print(f"Auto insurance cost: {auto_policy.count_cost(500)}")


# Медичне страхування
health_policy = HealthInsurance(type="full", age=70, health_status="good")
print(f"Health insurance cost: {health_policy.count_cost(1000)}")

# Страхування будинку
house_policy = HouseInsurance(type="full", country="Germany", area=200)
print(f"House insurance cost: {house_policy.count_cost(3000)}")

# Повне страхування (авто, здоров'я, будинок)
full_policy = FullInsurance(type="full", name="BMW", model="X5", year=2020,
                            age=40, health_status="good", country="Italy", area=180)
print(f"Full insurance cost: {full_policy.count_cost(500, 1000, 3000)}")





Consumer1 = Consumer( name = "Jonh",surname =  "Black", company = "SoftServe", salary = 1000)
Consumer2 = Consumer(name = "Pedro", surname = "Alonso", company = "Epam", salary = 10000000)

Consumer1.info()
Consumer1.CheckForInsurance(auto_policy, 500)
Consumer2.CheckForInsurance(health_policy, 1000)





