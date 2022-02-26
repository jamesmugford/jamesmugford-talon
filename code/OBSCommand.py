import os
from talon import Context, Module, actions, cron

import winsound

ctx = Context()
mod = Module()

@mod.action_class
class Actions:

    def obs_start_recording():
        """OBS start"""
        os.system('cmd /c "C:/Users/james/OneDrive/yzjmcm/bin/OBSCommand.exe /startrecording"')
        return