import os
import os.path
import requests
import time
from pathlib import Path
from talon import cron, ctrl, ui, Module, Context, actions, noise, settings, imgui, canvas
from talon.engine import engine
from talon.track.geom import Point2d
from talon_plugins import speech, eye_mouse, eye_zoom_mouse
import math
import time
import json






import platform
import subprocess
import ctypes
import os
import pathlib

key = actions.key
self = actions.self
dragging = False
scroll_amount = 0
click_job = None
scroll_job = None
gaze_job = None
cancel_scroll_on_pop = True
gaze_pos2 = Point2d(0, 0)

main_screen = ui.main_screen()

size_px = Point2d(main_screen.width, main_screen.height)

mod = Module()
mod.list('mouse_button', desc='List of mouse button words to mouse_click index parameter')
mod.setting('mouse_enable_pop_click', int)
mod.setting('mouse_enable_pop_stops_scroll', int)
mod.setting('mouse_focus_change_stops_scroll', int)
mod.setting('mouse_wake_hides_cursor', int)

ctx = Context()
ctx.settings["self.mouse_enable_pop_click"] = 0
ctx.settings["self.mouse_enable_pop_stops_scroll"] = 0
ctx.settings["self.mouse_wake_hides_cursor"] = 0

ctx.lists['self.mouse_button'] = {
    # right click
    'righty': '1',
    'rickle': '1',

    # left click
    'chiff': '0',
}

continuous_scoll_mode = ""


@mod.action_class
class Actions:
    def hitboxes_debug():
        """Hitboxes Debug"""
        print("Hitboxes Debug")



    def hitboxes_init():
        """Hitboxes Init"""
        print("Hitboxes Init")
        # FIXME
        if eye_mouse.tracker:
            eye_mouse.tracker.register('gaze', on_gaze)
        #else:
            #print("Please enable control mouse (zoom or gaze) first")
            #eye_mouse.control_mouse.toggle()








def on_gaze(frame):
#   print(frame.gaze.y)
    global gaze_pos2
    gaze_pos2 = frame.gaze # frame.gaze.y # * eye_mouse.main_screen



