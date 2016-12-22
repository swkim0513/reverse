from pico2d import *

class Music:
    def __init__(self):
        self.image = load_image('note_1.png')
        self.bgm = load_music('bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()