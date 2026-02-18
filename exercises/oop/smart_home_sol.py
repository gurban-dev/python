from abc import ABC, abstractmethod

# Part 1 - Abstract Base Class (Abstraction + Encapsulation)

# A Python class must inherit from ABC for it to be
# abstract class.
class SmartDevice(ABC):
    def __init__(self, name: str):
        # Treated as protected.
        # One underscore prefixes the name of the instance variable.
        self._name = name

        # Treated as private -> encapsulation
        # Two underscores prefixes the name of the instance variable.
        self.__is_on = False

    @abstractmethod
    def turn_on(self):
        # pass is included in this block of code because syntactically,
        # an instruction must be written, but an action does not need
        # to occur.
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def status(self):
        pass

    # Mutator/setter because it changes the value of the
    # instance variable '__is_on'.
    def _set_power(self, value: bool):
        self.__is_on = value

    # Selector/Getter because it returns the instance variable
    # '__is_on'.
    def _is_on(self):
        return self.__is_on


# Part 2 - Subclasses (Inheritance + Polymorphism)
class LightBulb(SmartDevice):
  def __init__(self, name: str, brightness: int=0):
    # Invokes the parent class' (SmartDevice) constructor method.
    super().__init__(name)

    self.brightness = brightness

  def turn_on(self):
    self._set_power(True)

    # Default behavior.
    self.brightness = 50

    print(f"{self._name} turned on. Brightness set to 50.")

  def turn_off(self):
    self._set_power(False)
    self.brightness = 0

    print(f"{self._name} turned off.")

  def set_brightness(self, new_brightness):
    self.brightness = new_brightness

  def get_brightness(self):
    return self.brightness

  def status(self):
    state = "ON" if self._is_on() else "OFF"

    return f"LightBulb [{self._name}]: {state}, Brightness = {self.brightness}"


class Thermostat(SmartDevice):
    def __init__(self, name: str, temperature=68):
        super().__init__(name)

        # Treated as private because of the two underscores that
        # prefix "temperature".
        self.__temperature = temperature

    # Selector/Getter
    def get_temperature(self):
        return self.__temperature

    # Mutator/Setter with validation
    def set_temperature(self, value):
        if value < 40:
            raise ValueError("Temperature cannot be lower than 40°F or 4.5 Celsius.")

        self.__temperature = value

    # turn_on() is a mutator/setter method because it changes
    # the value of an instance variable/attribute.

    # Note: Methods that mutate the value of a class variable/attribute
    # are also categorised as selector/setter methods.
    def turn_on(self):
        self._set_power(True)

        print(f"{self._name} thermostat is now on.")

    def turn_off(self):
        self._set_power(False)

        print(f"{self._name} thermostat is now off.")

    def status(self):
        # state = <expression1> if <condition> else <expression2>
        state = "ON" if self._is_on() else "OFF"

        return f"Thermostat [{self._name}]: {state}, Temperature = {self.__temperature}"


class SecurityCamera(SmartDevice):
    def __init__(self, name: str, resolution="1080p"):
        # Invokes the parent class' constructor method.
        super().__init__(name)

        self.resolution = resolution

    def turn_on(self):
        self._set_power(True)
        print(f"{self._name} activated at {self.resolution} resolution.")

    def turn_off(self):
        self._set_power(False)
        print(f"{self._name} deactivated.")

    def status(self):
        state = "ON" if self._is_on() else "OFF"

        return f"SecurityCamera [{self._name}]: {state}, Resolution = {self.resolution}"


# Part 3 - Polymorphic Function
def show_device_status(devices):
    print("\n--- DEVICE STATUS REPORT ---")

    for device in devices:
        print(device.status())

# Part 5 - Demo Script
if __name__ == "__main__":
    # Instantiate one of each device.
    bulb = LightBulb("Living Room Light")

    thermo = Thermostat("Hallway Thermostat")

    # The argument "Front Door Camera" will be passed to the
    # constructor method, and assigned to the "name" parameter.
    camera = SecurityCamera("Front Door Camera")

    # Turn devices on/off
    bulb.turn_on()
    thermo.turn_on()
    camera.turn_off()

    # Adjust settings.
    thermo.set_temperature(72)

    # Allowed because brightness instance attribute is not private.
    # bulb.brightness = 80

    bulb.set_brightness(80)

    # Show full system status (polymorphism demonstration).
    devices: list[SmartDevice] = [bulb, thermo, camera]

    show_device_status(devices)