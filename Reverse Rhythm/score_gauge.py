from pico2d import*


class Score_gauge():
    def __init__(self):
        self.image = load_image('score_gauge.png')
    def draw(self):
        self.image.clip_draw(0,0,800,100,800,50)
    def update(self):
        pass