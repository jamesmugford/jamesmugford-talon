# From https://github.com/talonvoice/examples/blob/master/noise.py

from talon import ctrl
from talon import noise

class NoiseModel:
    def __init__(self):
        noise.register('pop', self.on_pop)

    def on_pop(self, noise):
        ctrl.mouse_click(button=0, hold=16000)

model = NoiseModel()
