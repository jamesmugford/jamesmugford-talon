###################################
# comment out hiss while dictating #
###################################

import time

from talon import ctrl, actions
from talon import tap, noise
from talon.track.geom import Point2d
from talon_plugins import speech, eye_mouse, eye_zoom_mouse
from talon_plugins.eye_mouse import config, toggle_camera_overlay, toggle_control

class NoiseModel:
    def __init__(self):
        self.hiss_start = 0
        self.hiss_last = 0
        self.button = 0
        self.mouse_origin = Point2d(0, 0)
        self.mouse_last = Point2d(0, 0)
        self.dragging = False

        tap.register(tap.MMOVE, self.on_move)
        noise.register('hiss', self.on_noise)

    def on_move(self, typ, e):
        print('on_move')
        # if typ != tap.MMOVE: return
        # self.mouse_last = pos = Point2d(e.x, e.y)
        # if self.hiss_start and not self.dragging:
        #     if (pos - self.mouse_origin).len() > 10:
        #         self.dragging = True
        #         self.button = 0
        #         x, y = self.mouse_origin.x, self.mouse_origin.y
        #         ctrl.mouse(x, y)
        #         #ctrl.mouse_click(x, y, button=0, down=True)

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

            # if now - self.hiss_last < 0.25:
            #     ctrl.mouse_click(button=self.button, down=True)
            #     self.hiss_last = now
            #     self.dragging = True
            # else:
            #     self.mouse_origin = self.mouse_last
            # self.hiss_start = now
        else:
            #eye_mouse.control_mouse.disable()
            actions.tracking.control1_toggle(False)
            #toggle_control(False)
            # ctrl.key_press("keypad_5")
            # ctrl.mouse_click(button=0)
            # print('hiss end')
            # if self.dragging:
            #     ctrl.mouse_click(button=self.button, up=True)
            #     self.dragging = False
            # else:
            #     duration = time.time() - self.hiss_start
            #     if duration > 0.5:
            #         self.button = 1
            #         #ctrl.mouse_click(button=1)55
            #         self.hiss_last = now
            #     elif duration > 0.2:
            #         self.button = 0
            #         ctrl.mouse_click(button=0)
            #         self.hiss_last = now
            # self.hiss_start = 0

model = NoiseModel()
