from pico2d import*

class Pdm():
    def __init__(self):
        self.image = load_image('pdm.png')
        self.frame_time = 0
        self.bgm = load_music('pdm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.clip_draw(0,0,1200,1100,600,550)
    def update(self):
        pass