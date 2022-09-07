-

work next: key(ctrl-super-right)
work last: key(ctrl-super-left)


enter: key(enter)

lock windows: key(super-l)


page: key(pgdown)

invert: key(super-alt-n)

# sleep: key(plus)

mouse: key(keypad_5)

bash: key(alt)

min: key(super-down)
max: key(super-up)

switch:
	user.mouse_toggle_control_mouse()
	user.mouse_toggle_zoom_mouse()

snore:
	speech.disable()
	app.notify("Talon Sleep")
wake: 
	speech.enable()
	app.notify("Talon Awake")


parrot(tut):
	print("tut again")
	user.play_beep()
	core.repeat_command(1)

dredge: key(alt-tab)

bulk message: key(f13)

key(f15):
	core.repeat_command(1)

dictation start: key(alt-p)
dictation stop: key(alt-o)

pause: key(alt-1)
recenter: key(alt-2)