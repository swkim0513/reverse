from pico2d import*

class Life_gauge():
    def __init__(self):
        self.image = load_image('life_gauge.png')
    def draw(self):
        self.image.clip_draw(0,0,400,50,900,50)
    def update(self):
        pass