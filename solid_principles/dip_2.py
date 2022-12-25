"""
    Higher level modules should not depend upon lower level modules. Both should depend upon abstraction.
"""

from abc import ABC, abstractmethod

print("----------------------------- Before DIP ---------------------------")


class LightBulb:
    def turn_on(self):
        print("Bulb: turn on")

    def turn_off(self):
        print("Bulb: turn off")


"""
    Here the class ElectricPowerSwitch depends upon LightBulb, High level module depending upon lower level module
    rather than abstraction.
"""


class ElectricPowerSwitch:
    def __init__(self, l: LightBulb) -> None:
        self.l = l
        self.on = False

    def press_switch(self):
        if self.on:
            self.l.turn_off()
            self.on = False
        else:
            self.l.turn_on()
            self.on = True


l = LightBulb()

switch = ElectricPowerSwitch(l)
switch.press_switch()
switch.press_switch()


print("----------------------------- After DIP ---------------------------")


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("Bulb: turn on")

    def turn_off(self):
        print("Bulb: turn off")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turn on")

    def turn_off(self):
        print("Fan: turn off")


class ElectricPowerSwitch:

    # Now this module is depending upon abstraction rather than low level modules
    def __init__(self, l: Switchable) -> None:
        self.l = l
        self.on = False

    def press_switch(self):
        if self.on:
            self.l.turn_off()
            self.on = False
        else:
            self.l.turn_on()
            self.on = True


l = Fan()

switch = ElectricPowerSwitch(l)
switch.press_switch()
switch.press_switch()
