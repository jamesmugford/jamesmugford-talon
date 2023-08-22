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

parrot(tut):
	print("tut again")
	user.play_beep()
	core.repeat_command(1)

dredge: key(alt-tab)

dictation start: key(alt-p)
dictation stop: key(alt-o)

pause: key(alt-1)
recenter: key(alt-2)

track: key(f9)

bulk message: key(f13)


# Function key hotkey mappings

# f14 = some auto hotkey debug test

key(f15): bcore.repeat_phrase(1)

key(f16): speech.toggle()