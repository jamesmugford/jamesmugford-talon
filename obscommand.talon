os: windows
mode: command
-

record:
  user.obs_toggle_record()
  print("toggle record")

parrot(whistle):
  user.obs_toggle_record()
  print("toggle record")
  user.play_beep()