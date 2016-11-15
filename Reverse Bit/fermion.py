from pico2d import*

class Fermion():
    def __init__(self):
        self.image = load_image('fermion.png')
    def draw(self):
        self.image.clip_draw(0,0,1200,950,600,550)
    def update(self):
        pass