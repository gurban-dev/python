from abc import ABC, abstractmethod

# Part 1 — Abstract Base Class (Abstraction + Encapsulation)

class SmartDevice(ABC):
  def __init__(self, name: str):
    # protected
    self._name = name

    # private → encapsulation
    self.__is_on = False

  @abstractmethod
  def turn_on(self):
    pass

  @abstractmethod
  def turn_off(self):
    pass

  @abstractmethod
  def status(self):
    pass

# Encapsulated power state getter and setter
def _set_power(self, value: bool):
  self.__is_on = value

def _is_on(self):
  return self.__is_on


# Part 2 — Subclasses (Inheritance + Polymorphism)

class LightBulb(SmartDevice):
  def __init__(self, name: str, brightness=0):
    super().__init__(name)

    self.brightness = brightness

def turn_on(self):
  self._set_power(True)

  # default behavior
  self.brightness = 50

  print(f"{self._name} turned on. Brightness set to 50.")

def turn_off(self):
  self._set_power(False)
  self.brightness = 0
  print(f"{self._name} turned off.")

def status(self):
  state = "ON" if self._is_on() else "OFF"
  return f"LightBulb [{self._name}]: {state}, Brightness = {self.brightness}"

class Thermostat(SmartDevice):
  def __init__(self, name: str, temperature=68):
    super().__init__(name)
    # private → encapsulation
    self.__temperature = temperature

# Getter
def get_temperature(self):
  return self.__temperature

# Setter with validation
def set_temperature(self, value):
  if value < 40:
    raise ValueError("Temperature cannot be lower than 40°F.")
  self.__temperature = value

def turn_on(self):
  self._set_power(True)
  print(f"{self._name} thermostat is now on.")

def turn_off(self):
  self._set_power(False)
  print(f"{self._name} thermostat is now off.")

def status(self):
  state = "ON" if self._is_on() else "OFF"

class SecurityCamera(SmartDevice):
  def __init__(self, name: str, resolution="1080p"):
    super().__init__(name)
    self.resolution = resolution

  def turn_on(self):
    self._set_power(True)
    print(f"{self._name} camera activated at {self.resolution} resolution.")

  def turn_off(self):
    self._set_power(False)
    print(f"{self._name} camera deactivated.")

  def status(self):
    state = "ON" if self._is_on() else "OFF"
    return f"SecurityCamera [{self._name}]: {state}, Resolution = {self.resolution}"


  # Part 3 — Polymorphic Function


def show_device_status(devices):
  print("\n--- DEVICE STATUS REPORT ---")
  for d in devices:
    print(d.status())
    print("-----------------------------\n")

# Part 5 — Demo Script

if __name__ == "__main__":
  # Instantiate one of each device
  bulb = LightBulb("Living Room Light")
  thermo = Thermostat("Hallway Thermostat")
  cam = SecurityCamera("Front Door Camera")

  # Turn devices on/off
  bulb.turn_on()
  thermo.turn_on()
  cam.turn_off()

  # Adjust settings
  thermo.set_temperature(72)
  bulb.brightness = 80  # allowed because brightness is not private

  # Show full system status (polymorphism demonstration)
  devices = [bulb, thermo, cam]
  show_device_status(devices)