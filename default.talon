#defines modes specific to Dragon.
speech.engine: dragon
mode: all
-
# wakes Dragon on Mac, deactivates talon speech commands
dragon mode: user.dragon_mode()
#sleep dragon on Mac, activates talon speech commands
talon mode: user.talon_mode()



snore:
	#speech.disable()
#	app.notify("All Sleep")
	user.dragon_sleep()
	
key(ctrl-f7):
#	app.notify("All Sleep")
	user.dragon_sleep()

key(ctrl-f8):
#	app.notify("All Wake")
	user.dragon_wake()

dredge: key(alt-tab)

bulk message: key(f13)			


key(f15):
	core.repeat_command(1)
