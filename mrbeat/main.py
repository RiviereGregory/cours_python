from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, Clock
from kivy.uix.relativelayout import RelativeLayout

from audio_engine import AudioEngine
from sounds_kit_service import SoundsKitService
from track import TrackWidget

Builder.load_file("track.kv")
Builder.load_file("play_indicator.kv")

TRACK_NB_STEP = 16


class MainWidget(RelativeLayout):
    tracks_layout = ObjectProperty()
    play_indicator_widget = ObjectProperty()
    TRACK_STEPS_LEFT_ALIGN = NumericProperty(dp(100))
    step_index = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.sound_kit_service = SoundsKitService()
        # kick_sound = self.sound_kit_service.get_sound_at(0)

        self.audio_engine = AudioEngine()

        # self.audio_engine.create_track(kick_sound.samples, 120)

        # appeler create_mixer(... , 120, TRACK_NB_STEP)
        self.mixer = self.audio_engine.create_mixer(self.sound_kit_service.soundkit.get_all_samples(), 120,
                                                    TRACK_NB_STEP, self.on_mixer_current_step_changed)

    def on_parent(self, widget, parent):
        self.play_indicator_widget.set_nb_steps(TRACK_NB_STEP)
        # self.play_indicator_widget.set_current_step_index(10)
        for i in range(0, self.sound_kit_service.get_nb_tracks()):
            sound = self.sound_kit_service.get_sound_at(i)
            self.tracks_layout.add_widget(
                TrackWidget(sound, self.audio_engine, TRACK_NB_STEP, self.mixer.tracks[i], self.TRACK_STEPS_LEFT_ALIGN))

    def on_mixer_current_step_changed(self, step_index):
        # print("on_mixer_current_step_changed : " + str(step_index))
        self.step_index = step_index
        Clock.schedule_once(self.update_play_indicator_cbk, 0)

    def update_play_indicator_cbk(self, dt):
        if self.play_indicator_widget is not None:
            self.play_indicator_widget.set_current_step_index(self.step_index)


class MrBeatApp(App):
    pass


MrBeatApp().run()
