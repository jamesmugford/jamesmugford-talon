from talon import Context, Module, app, actions, speech_system

mod = Module()


@mod.action_class
class Actions:
    def dragon_wake():
        """For windows and Mac with Dragon, enables Talon commands and Dragon's command mode."""
        actions.speech.enable()

        engine = speech_system.engine.name
        # app.notify(engine)
        if "dragon" in engine:
            actions.user.engine_wake()
            # note: this may not do anything for all versions of Dragon. Requires Pro.
            actions.user.engine_mimic("wake up")

    def dragon_sleep():
        """For windows and Mac with Dragon, disables Talon commands and exits Dragon's command mode"""
        engine = speech_system.engine.name
        # app.notify(engine)

        if "dragon" in engine:
            # app.notify("dragon mode")
            actions.speech.disable()
            actions.user.engine_wake()
            # note: this may not do anything for all versions of Dragon. Requires Pro.
            actions.user.engine_mimic("go to sleep")
