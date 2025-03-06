###################################
# comment out hiss while dictating #
###################################

import time

from talon import ctrl, actions
from talon import tap, noise
from talon.types import Point2d

class NoiseModel:
    def __init__(self):
        self.hiss_start = 0
        self.hiss_last = 0
        self.button = 0
        self.mouse_origin = Point2d(0, 0)
        self.mouse_last = Point2d(0, 0)
        self.dragging = False

        noise.register('hiss', self.on_noise)

    def on_noise(self, noise):
        now = time.time()
        print(noise)
        if noise == True:
            print('hiss start')
#            eye_mouse.control_mouse.enable()
            actions.tracking.control1_toggle(True)
            #toggle_control1(True)
            #actions.tracking.control_enabled()
            # thisctrl.key_press("keypad_5")
        else:
            #eye_mouse.control_mouse.disable()
            actions.tracking.control1_toggle(False)
            #toggle_control(False)
            # ctrl.key_press("keypad_5")
            # ctrl.mouse_click(button=0)
            # print('hiss end')
            

model = NoiseModel()
