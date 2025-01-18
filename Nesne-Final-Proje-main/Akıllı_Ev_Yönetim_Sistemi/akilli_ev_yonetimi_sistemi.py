from abc import ABC, abstractmethod

# Controllable Interface
class Controllable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def is_on(self):
        pass

# Appliance Base Class
class Appliance(Controllable):
    def __init__(self, name):
        self.name = name
        self._is_on = False

    def turn_on(self):
        self._is_on = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self._is_on = False
        print(f"{self.name} is now OFF.")

    def is_on(self):
        return self._is_on

# Light Class
class Light(Appliance):
    def __init__(self, name, brightness=100):
        super().__init__(name)
        self.brightness = brightness

    def set_brightness(self, brightness):
        if 0 <= brightness <= 100:
            self.brightness = brightness
            print(f"{self.name} brightness set to {self.brightness}%.")
        else:
            print("Brightness must be between 0 and 100.")

# Thermostat Class
class Thermostat(Appliance):
    def __init__(self, name, temperature=22):
        super().__init__(name)
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"{self.name} temperature set to {self.temperature}°C.")

# SecuritySystem Class
class SecuritySystem(Appliance):
    def __init__(self, name):
        super().__init__(name)
        self.alarm_on = False

    def activate_alarm(self):
        self.alarm_on = True
        print(f"{self.name} alarm activated.")

    def deactivate_alarm(self):
        self.alarm_on = False
        print(f"{self.name} alarm deactivated.")

# Main Console Application
def main():
    devices = [
        Light("Living Room Light"),
        Thermostat("Home Thermostat"),
        SecuritySystem("Home Security")
    ]

    while True:
        print("\n--- Smart Home Management System ---")
        for i, device in enumerate(devices):
            status = "ON" if device.is_on() else "OFF"
            print(f"{i + 1}. {device.name} ({status})")

        print("0. Exit")
        choice = input("Select a device to manage (0 to exit): ")

        if choice == "0":
            print("Exiting Smart Home Management System.")
            break

        if choice.isdigit() and 1 <= int(choice) <= len(devices):
            device = devices[int(choice) - 1]
            print(f"\nManaging {device.name}")
            print("1. Turn ON")
            print("2. Turn OFF")
            print("3. Check Status")

            if isinstance(device, Light):
                print("4. Set Brightness")
            elif isinstance(device, Thermostat):
                print("4. Set Temperature")
            elif isinstance(device, SecuritySystem):
                print("4. Activate Alarm")
                print("5. Deactivate Alarm")

            action = input("Choose an action: ")

            if action == "1":
                device.turn_on()
            elif action == "2":
                device.turn_off()
            elif action == "3":
                print(f"{device.name} is {'ON' if device.is_on() else 'OFF'}.")
            elif action == "4" and isinstance(device, Light):
                brightness = int(input("Enter brightness (0-100): "))
                device.set_brightness(brightness)
            elif action == "4" and isinstance(device, Thermostat):
                temperature = int(input("Enter temperature: "))
                device.set_temperature(temperature)
            elif action == "4" and isinstance(device, SecuritySystem):
                device.activate_alarm()
            elif action == "5" and isinstance(device, SecuritySystem):
                device.deactivate_alarm()
            else:
                print("Invalid action.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
