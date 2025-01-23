import os
import time
import random

MAX_TEMP_INCREASE = 70
MIN_TEMP_INCREASE = 30

MAX_TEMP_DECREASE = 40
MIN_TEMP_DECREASE = 20

class ReactorComponent:
    def __init__(self, name: str, status: str = "Operational"):
        self.name = name
        self._status = status

    def get_status(self):
        return self._status

    def set_status(self, new_status: str):
        if new_status in ["Operational", "Under Maintenance", "Inactive"]:
            self._status = new_status
        else:
            raise ValueError("Invalid status provided!")

class LoggerMixin:
    @staticmethod
    def log(message: str):
        print(f"[LOG] {message}")

class Reactor(ReactorComponent, LoggerMixin):
    MAX_TEMP = 1000
    MIN_TEMP = 300

    def __init__(self, name: str, temperature: float, status: str = "Operational"):
        super().__init__(name, status)
        self.__temperature = temperature
        self.activity = "Producing" if temperature < Reactor.MAX_TEMP else "Cooling"

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, new_temperature: float):
        if new_temperature < 0:
            raise ValueError("Temperature cannot be negative!")
        self.__temperature = new_temperature
        self.log(f"Temperature of reactor {self.name} updated to {self.__temperature}°C")
        self._update_activity()

    def update_temperature(self):
        if self.activity == "Producing":
            self.__temperature += random.randint(MIN_TEMP_INCREASE, MAX_TEMP_INCREASE)
            if self.__temperature >= Reactor.MAX_TEMP:
                self.activity = "Cooling"
        elif self.activity == "Cooling":
            self.__temperature -= random.randint(MIN_TEMP_DECREASE, MAX_TEMP_DECREASE)
            if self.__temperature <= Reactor.MIN_TEMP:
                self.activity = "Producing"

    def _update_activity(self):
        if self.__temperature >= Reactor.MAX_TEMP:
            self.activity = "Cooling"
        elif self.__temperature <= Reactor.MIN_TEMP:
            self.activity = "Producing"

    def get_summary(self):
        return {
            "Name": self.name,
            "Status": self.get_status(),
            "Temperature": self.get_temperature(),
            "Activity": self.activity,
        }

class ReactorManager(LoggerMixin):
    def __init__(self):
        self.reactors = []

    def add_reactor(self, reactor: Reactor):
        self.reactors.append(reactor)
        self.log(f"Reactor {reactor.name} added.")

    def remove_reactor(self, name: str):
        for reactor in self.reactors:
            if reactor.name == name:
                self.reactors.remove(reactor)
                self.log(f"Reactor {name} removed.")

                return

        print(f"No reactor with name '{name}' found.")

    def list_reactors(self):
        print("Reactor Summary:")

        for reactor in self.reactors:
            summary = reactor.get_summary()
            print(f"Name: {summary['Name']}, Status: {summary['Status']}, Temperature: {summary['Temperature']}°C, Activity: {summary['Activity']}")

    def update_all_reactors(self):
        for reactor in self.reactors:
            reactor.update_temperature()

    def live_update(self, cycles: int, interval: float = 1.0):
        for cycle in range(cycles):
            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"--- Simulation Cycle {cycle + 1}/{cycles} ---")
            self.update_all_reactors()
            self.list_reactors()

            time.sleep(interval)

class Validator:
    @staticmethod
    def validate_name(name: str):
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long!")

    @staticmethod
    def validate_temperature(temperature: float):
        if temperature < 0:
            raise ValueError("Temperature must be a positive value!")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    manager = ReactorManager()

    while True:
        clear_screen()
        print("\n--- Reactor Management System ---")
        print("1. Add Reactor")
        print("2. Update Reactor Status")
        print("3. Update Reactor Temperature")
        print("4. Remove Reactor")
        print("5. List Reactors")
        print("6. Simulate Reactor Activity")
        print("7. Exit")

        choice = input("Choose an option: ")
        clear_screen()

        if choice == "1":
            try:
                name = input("Enter reactor name: ")
                Validator.validate_name(name)

                temperature = float(input("Enter initial temperature (°C): "))
                Validator.validate_temperature(temperature)

                reactor = Reactor(name, temperature)
                manager.add_reactor(reactor)
            except ValueError as e:
                print(f"Error: {e}")

            input("\nPress Enter to return to the menu...")

        elif choice == "2":
            name = input("Enter reactor name: ")
            status = input("Enter new status (Operational/Under Maintenance/Inactive): ")

            for reactor in manager.reactors:
                if reactor.name == name:
                    try:
                        reactor.set_status(status)

                        print(f"Status of reactor {name} updated to {status}.")
                    except ValueError as e:
                        print(f"Error: {e}")
                    break
            else:
                print(f"No reactor with name '{name}' found.")

            input("\nPress Enter to return to the menu...")

        elif choice == "3":
            name = input("Enter reactor name: ")
            new_temp = float(input("Enter new temperature (°C): "))

            for reactor in manager.reactors:
                if reactor.name == name:
                    try:
                        reactor.set_temperature(new_temp)
                        print(f"Temperature of reactor {name} updated.")
                    except ValueError as e:
                        print(f"Error: {e}")

                    break
            else:
                print(f"No reactor with name '{name}' found.")

            input("\nPress Enter to return to the menu...")
        elif choice == "4":
            name = input("Enter reactor name to remove: ")
            manager.remove_reactor(name)
            
            input("\nPress Enter to return to the menu...")
        elif choice == "5":
            manager.list_reactors()

            input("\nPress Enter to return to the menu...")
        elif choice == "6":
            try:
                cycles = int(input("Enter the number of simulation cycles: "))
                interval = float(input("Enter the interval between cycles (seconds): "))
                
                print("Simulating reactor activity...")

                manager.live_update(cycles, interval)
            except ValueError as e:
                print(f"Error: {e}")

            input("\nPress Enter to return to the menu...")
        elif choice == "7":
            print("Exiting Reactor Management System.")

            break
        else:
            print("Invalid choice! Please try again.")
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    menu()
