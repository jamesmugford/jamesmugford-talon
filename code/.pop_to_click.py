# From https://github.com/talonvoice/examples/blob/master/noise.py

from talon import ctrl
from talon import noise

class NoiseModel:
    def __init__(self):
        print("pop_to_click enabled")
        self.popFlipFlop = True
        noise.register('pop', self.on_pop)

    def on_pop(self, noise):
        print("on_pop")
        if self.popFlipFlop:
            self.popFlipFlop = False
            ctrl.key_press("keypad_5")
        else:
            self.popFlipFlop = True
            ctrl.key_press("keypad_5")
            ctrl.mouse_click(button=0, hold=4)



model = NoiseModel()
