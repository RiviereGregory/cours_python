import wave
from array import array


class Sound:
    samples = None
    nb_samples = None

    def __init__(self, filename, displayname):
        self.filename = filename
        self.displayname = displayname
        self.load_sound()

    def load_sound(self):
        wav_file = wave.open(self.filename, 'rb')
        self.nb_samples = wav_file.getnframes()
        frames = wav_file.readframes(self.nb_samples)
        self.samples = array('h', frames)


class SoundKit:
    sounds = ()

    def get_nb_tracks(self):
        return len(self.sounds)

    def get_all_samples(self):
        all_samples = []
        for i in range(0, len(self.sounds)):
            all_samples.append(self.sounds[i].samples)

        return all_samples


class SoundsKit1(SoundKit):
    sounds = (Sound("sounds/kit1/kick.wav", "KICK"),
              Sound("sounds/kit1/clap.wav", "CLAP"),
              Sound("sounds/kit1/shaker.wav", "SHAKER"),
              Sound("sounds/kit1/snare.wav", "SNARE"))


class SoundsKit2(SoundKit):
    sounds = (Sound("sounds/kit1/kick.wav", "KICK"),
              Sound("sounds/kit1/clap.wav", "CLAP"),
              Sound("sounds/kit1/shaker.wav", "SHAKER"),
              Sound("sounds/kit1/snare.wav", "SNARE"),
              Sound("sounds/kit1/bass.wav", "BASS"),
              Sound("sounds/kit1/effects.wav", "EFFETS"),
              Sound("sounds/kit1/pluck.wav", "PLUCK"),
              Sound("sounds/kit1/vocal_chop.wav", "VOCAL"),
              Sound("sounds/kit1/kick.wav", "KICK"),
              Sound("sounds/kit1/clap.wav", "CLAP"),
              Sound("sounds/kit1/shaker.wav", "SHAKER"),
              Sound("sounds/kit1/snare.wav", "SNARE"),
              Sound("sounds/kit1/bass.wav", "BASS"),
              Sound("sounds/kit1/effects.wav", "EFFETS"),
              Sound("sounds/kit1/pluck.wav", "PLUCK"),
              Sound("sounds/kit1/vocal_chop.wav", "VOCAL"),
              Sound("sounds/kit1/kick.wav", "KICK"),
              Sound("sounds/kit1/clap.wav", "CLAP"),
              Sound("sounds/kit1/shaker.wav", "SHAKER"),
              Sound("sounds/kit1/snare.wav", "SNARE"),
              Sound("sounds/kit1/bass.wav", "BASS"),
              Sound("sounds/kit1/effects.wav", "EFFETS"),
              Sound("sounds/kit1/pluck.wav", "PLUCK"),
              Sound("sounds/kit1/vocal_chop.wav", "VOCAL")
              )


class SoundsKit3(SoundKit):
    sounds = (Sound("sounds/kit1/kick.wav", "KICK"),
              Sound("sounds/kit1/clap.wav", "CLAP"),
              Sound("sounds/kit1/shaker.wav", "SHAKER"),
              Sound("sounds/kit1/snare.wav", "SNARE"),
              Sound("sounds/kit1/bass.wav", "BASS"),
              Sound("sounds/kit1/effects.wav", "EFFETS"),
              Sound("sounds/kit1/pluck.wav", "PLUCK"),
              Sound("sounds/kit1/vocal_chop.wav", "VOCAL")
              )


class SoundsKitService:
    soundkit = SoundsKit3()

    def get_nb_tracks(self):
        return self.soundkit.get_nb_tracks()

    def get_sound_at(self, index):
        if index >= self.get_nb_tracks():
            return None

        return self.soundkit.sounds[index]
