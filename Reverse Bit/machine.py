from pico2d import*

class Machine():
    def __init__(self):
        self.image = load_image('machine_2.png')
    def draw(self):
        self.image.clip_draw(0,0,400,950,200,550)
    def update(self):
        pass
