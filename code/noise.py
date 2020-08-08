# From https://github.com/talonvoice/examples/blob/master/noise.py
import time

from talon import ctrl
from talon import tap
from talon import noise
from talon.track.geom import Point2d

class NoiseModel:
    def __init__(self):
        noise.register('pop', self.on_pop)

    def on_pop(self, noise):
        ctrl.mouse_click(button=0, hold=16000)

model = NoiseModel()
