"""
Copyright (c) 2021 James Mugford

"""

from talon import ctrl
from talon import noise

class NoiseModel:
    def __init__(self):
        print("pop_media_express enabled")
        self.flipFlop = False
        noise.register('pop', self.on_pop)

    def on_pop(self, noise):
        print("on_pop")
        if self.flipFlop:
            self.flipFlop = False
            ctrl.key_press("esc")
        else:
            self.flipFlop = True
            ctrl.key_press("cmd+r")

model = NoiseModel()
