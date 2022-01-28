# From https://github.com/talonvoice/examples/blob/master/noise.py

from talon import ctrl
from talon import noise
import winsound

class NoiseModel:
    def __init__(self):
        print("pop_to_click enabled")
        noise.register('pop', self.on_pop)

    def on_pop(self, noise):
        print("on_pop")
        ctrl.key_press("keypad_7")
        winsound.Beep(1000, 500)



model = NoiseModel()