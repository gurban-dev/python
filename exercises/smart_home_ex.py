'''
Concepts:
Abstraction
Encapsulation
Inheritance
Polymorphism

Task:
Design a simple Smart Home system using OOP. Your design must demonstrate:

* Abstraction (via abstract base classes)
* Encapsulation (private/protected attributes + getters/setters)
* Inheritance (subclasses extend a parent class)
* Polymorphism (overridden methods with different behaviors)

---

Part 1 — Abstract Base Class

Create an abstract class SmartDevice that includes:

* A protected attribute _name
* A private attribute __is_on (encapsulation)
* A constructor that sets name and default power state (off)
* Abstract methods:
  turn_on()
  turn_off()
  status()

Use abc.ABC and @abstractmethod.

---

Part 2 — Subclasses via Inheritance

Create three subclasses:

1. LightBulb
2. Thermostat
3. SecurityCamera

Each subclass must:

* Inherit from SmartDevice
* Override turn_on(), turn_off(), and status()
* Add at least one custom attribute:
  LightBulb → brightness
  Thermostat → temperature
  SecurityCamera → resolution
* Implement custom behavior. Example:
  Turning on a LightBulb sets brightness to 50 by default.

---

Part 3 — Demonstrate Polymorphism

Write a function:
show_device_status(device_list)

It should:

* Accept a list of SmartDevice objects
* Loop through them and call .status()
* Work without knowing device types

---

Part 4 — Encapsulation Requirement

For at least one subclass:

* Use a private attribute (e.g., __temperature)
* Provide getter and setter methods
* Validate input (e.g., temperature must be >= 40°F)

---

Part 5 — Demo Script

Write a script that:

* Instantiates one object of each subclass
* Turns some devices on and others off
* Adjusts some settings
* Calls show_device_status() to prove polymorphism

---

Bonus (Optional):

* Add a SmartHome class to store/manage devices
* Implement **str**() or other operators
* Add error handling for invalid operations
'''