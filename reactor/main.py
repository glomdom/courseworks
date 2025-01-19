import time
import curses
import random
from threading import Thread, Event

class Reactor:
    def __init__(self, reactor_id, name, status="offline", fuel_level=100, coolant_level=100):
        self.__id = reactor_id
        self.name = name
        self._status = status
        self.__temperature = 100
        self.output = 50
        self.fuel_level = fuel_level
        self.coolant_level = coolant_level

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < 0:
            raise ValueError("Temperature cannot be negative.")
        self.__temperature = value

    @staticmethod
    def validate_status(status):
        return status in ["active", "offline", "maintenance"]

    def update(self):
        if self._status == "active":
            self.temperature += random.randint(-3, 5)

            if self.coolant_level > 0 and self.temperature > 150:
                self.temperature -= random.randint(1, 3)
                self.coolant_level -= random.uniform(0.3, 0.7)

            if 50 <= self.temperature <= 300:
                base_output = (self.temperature - 50) * 0.5
                fluctuation = random.uniform(0, 5)
                self.output = max(base_output + fluctuation, 0)
            else:
                self.output = 0

            if self.output > 0 and self.fuel_level > 0:
                fuel_needed = self.output * 0.01

                if self.fuel_level >= fuel_needed:
                    self.fuel_level -= fuel_needed
                else:
                    self.output *= self.fuel_level / fuel_needed
                    self.fuel_level = 0

            if self.fuel_level < 20:
                self.fuel_level += random.uniform(0.5, 1.5)
            if self.coolant_level < 20:
                self.coolant_level += random.uniform(0.2, 1.0)
        else:
            self.temperature = max(self.temperature - random.randint(1, 3), 20)
            self.output = 0

    def __str__(self):
        return f"{self.name} (ID: {self.__id}, Status: {self._status})"

class NuclearReactor(Reactor):
    def __init__(self, reactor_id, name, status="offline", fuel_level=100, coolant_level=100):
        super().__init__(reactor_id, name, status, fuel_level, coolant_level)
        self.reactor_type = "Nuclear"

class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class ReactorFacility(LoggerMixin):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.reactors = []
        self.update_event = Event()

    def add_reactor(self, reactor):
        if not isinstance(reactor, Reactor):
            self.log("Attempted to add an invalid reactor.")

            return

        self.reactors.append(reactor)
        self.log(f"Reactor {reactor.name} added.")

    def list_reactors(self):
        return [str(reactor) for reactor in self.reactors]

    def update_reactors(self):
        while not self.update_event.is_set():
            for reactor in self.reactors:
                reactor.update()

            time.sleep(0.5)

def curses_input(stdscr, prompt, y, x):
    stdscr.addstr(y, x, prompt)
    curses.echo()
    user_input = stdscr.getstr(y, x + len(prompt)).decode("utf-8")
    curses.noecho()

    return user_input

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)

    facility = ReactorFacility("Main Reactor Facility")

    facility.update_event.clear()
    update_thread = Thread(target=facility.update_reactors, daemon=True)
    update_thread.start()

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Reactor Manager Menu:", curses.A_BOLD)
        stdscr.addstr(2, 0, "1. List Reactors")
        stdscr.addstr(3, 0, "2. Add Reactor")
        stdscr.addstr(4, 0, "3. Start Live Monitoring")
        stdscr.addstr(5, 0, "4. Exit")
        stdscr.refresh()

        choice = stdscr.getkey()

        if choice == "1":
            stdscr.clear()
            reactors = facility.list_reactors()

            if not reactors:
                stdscr.addstr(0, 0, "No reactors in the facility.", curses.color_pair(2))
            else:
                for i, reactor in enumerate(reactors):
                    stdscr.addstr(i, 0, reactor)
            
            stdscr.addstr(len(reactors) + 1, 0, "Press any key to return.")
            stdscr.getkey()

        elif choice == "2":
            stdscr.clear()

            reactor_id = curses_input(stdscr, "Enter Reactor ID: ", 0, 0)
            name = curses_input(stdscr, "Enter Reactor Name: ", 1, 0)
            status = curses_input(stdscr, "Enter Reactor Status (active/offline/maintenance): ", 2, 0)

            if not Reactor.validate_status(status):
                status = "offline"

            reactor = NuclearReactor(reactor_id, name, status)
            facility.add_reactor(reactor)

            stdscr.addstr(4, 0, "Reactor added successfully.", curses.color_pair(3))
            stdscr.addstr(5, 0, "Press any key to return.")
            stdscr.getkey()

        elif choice == "3":
            stdscr.nodelay(True)
            stdscr.clear()
            stdscr.addstr(0, 0, "Live Monitoring (Press any key to quit):", curses.A_BOLD)

            try:
                while True:
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Live Monitoring (Press any key to quit):", curses.A_BOLD)
                    for i, reactor in enumerate(facility.reactors):
                        temp_color = curses.color_pair(2) if reactor.temperature > 150 else curses.color_pair(3)

                        stdscr.addstr(i * 5 + 2, 0, f"Reactor {i}: {reactor.name}")
                        stdscr.addstr(i * 5 + 3, 2, "Temp: ")
                        stdscr.addstr(f"{reactor.temperature}°C", temp_color)
                        stdscr.addstr(f"  Output: ")
                        stdscr.addstr(f"{reactor.output:.2f} MW", curses.color_pair(1))
                        stdscr.addstr(f"  Fuel: ")
                        stdscr.addstr(f"{reactor.fuel_level:.2f}%", curses.color_pair(3))
                        stdscr.addstr(f"  Coolant: ")
                        stdscr.addstr(f"{reactor.coolant_level:.2f}%", curses.color_pair(4))

                    stdscr.refresh()
                    if stdscr.getch() != -1:
                        break

                    time.sleep(0.5)

            finally:
                stdscr.nodelay(False)

        elif choice == "4":
            stdscr.addstr(8, 0, "Exiting Reactor Manager. Goodbye!", curses.color_pair(3))
            stdscr.refresh()
            facility.update_event.set()
            update_thread.join()
            break

        else:
            stdscr.addstr(6, 0, "Invalid choice. Please try again.", curses.color_pair(2))
            stdscr.addstr(7, 0, "Press any key to return.")
            stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(main)
