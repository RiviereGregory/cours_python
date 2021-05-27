from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout

from track import TrackWidget

Builder.load_file("track.kv")

NB_TRACK = 4


class MainWidget(RelativeLayout):
    tracks_layout = ObjectProperty()

    def on_parent(self, widget, parent):
        for i in range(0, NB_TRACK):
            self.tracks_layout.add_widget(TrackWidget())


class MrBeatApp(App):
    pass


MrBeatApp().run()
