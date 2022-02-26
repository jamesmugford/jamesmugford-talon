from talon import Context, Module, actions, cron

import winsound

ctx = Context()
mod = Module()

@mod.action_class
class Actions:

    def play_beep():
       """Switches the parrot mode around"""
       winsound.Beep(1000, 500)
       return

