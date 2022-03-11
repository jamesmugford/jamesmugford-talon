import os
from talon import Context, Module, actions, cron

ctx = Context()
mod = Module()

#actions.user.engine_mimic("wake up")

is_recording = False

@mod.action_class
class Actions:
  #def __init__(self):
  
  def obs_toggle_record():
#    global bIsRecording
    """OBS toggle record"""
    global is_recording
    
    if is_recording:
      os.system('cmd /c "OBSCommand.exe /stoprecording"')
      is_recording = False
    else:
      os.system('cmd /c "OBSCommand.exe /startrecording"')
      is_recording = True
	
    return
