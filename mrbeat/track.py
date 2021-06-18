from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton


class TrackStepButton(ToggleButton):
    pass


class TrackSoundButton(Button):
    pass


class TrackWidget(BoxLayout):
    def __init__(self, sound, audio_engine, track_nb_step, track_source, steps_left_align, **kwargs):
        super(TrackWidget, self).__init__(**kwargs)

        self.audio_engine = audio_engine
        self.sound = sound
        self.track_nb_step = track_nb_step
        self.track_source = track_source

        sound_and_separator_layout = BoxLayout()
        sound_and_separator_layout.size_hint_x = None
        sound_and_separator_layout.width = steps_left_align
        self.add_widget(sound_and_separator_layout)

        sound_button = TrackSoundButton()
        sound_button.text = sound.displayname
        sound_button.on_press = self.on_sound_button_press
        sound_and_separator_layout.add_widget(sound_button)
        # separateur
        separator_image = Image(source="images/track_separator.png")
        separator_image.size_hint_x = None
        separator_image.width = dp(15)
        sound_and_separator_layout.add_widget(separator_image)


        self.step_buttons = []
        for i in range(0, self.track_nb_step):
            step_button = TrackStepButton()
            step_button.bind(state=self.on_step_button_state)
            if int(i / 4) % 2 == 0:
                step_button.background_normal = "images/step_normal1.png"
            else:
                step_button.background_normal = "images/step_normal2.png"
            self.step_buttons.append(step_button)
            self.add_widget(step_button)

    def on_sound_button_press(self):
        self.audio_engine.play_sound(self.sound.samples)

    def on_step_button_state(self, widget, value):
        # 'down' == 1
        steps = []
        for i in range(0, self.track_nb_step):
            if self.step_buttons[i].state == "down":
                steps.append(1)
            else:
                steps.append(0)
        print(steps)
        self.track_source.set_steps(steps)
