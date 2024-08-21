

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hours_worked * self.hourly_rate
        else:
            regular_pay = 40 * self.hourly_rate
            overtime_hours = self.hours_worked - 40
            overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
            return regular_pay + overtime_pay

class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        return base_pay + self.bonus

if __name__ == "__main__":
                   #Creating an Employee instance
    employee = Employee("John Doe", 45, 20.0)
    employee
