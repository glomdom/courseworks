from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
    
    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class ElectricityBill(ABC):
    @abstractmethod
    def calculate_bill(self, consumption):
        pass

class ResidentialBill(ElectricityBill):
    def calculate_bill(self, consumption):
        return consumption * 0.12

class CommercialBill(ElectricityBill):
    def calculate_bill(self, consumption):
        return consumption * 0.15

full_time = FullTimeEmployee(5000)
part_time = PartTimeEmployee(20, 80)

print("full-time employee salary ->", full_time.calculate_salary())
print("part-time employee salary ->", part_time.calculate_salary())

residential = ResidentialBill()
commercial = CommercialBill()

print("residential Bill for 500 kWh ->", residential.calculate_bill(500))
print("commercial Bill for 500 kWh ->", commercial.calculate_bill(500))