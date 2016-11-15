from pico2d import*

class Pdm():
    def __init__(self):
        self.image = load_image('pdm.png')
    def draw(self):
        self.image.clip_draw(0,0,1200,1100,600,550)
    def update(self):
        pass