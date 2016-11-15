from pico2d import*

class Machine_extreme():
    def __init__(self):
        self.x = 200
        self.y = 413
        self.image = load_image('machine_2_extreme.png')
    def draw(self):
        self.image.clip_draw(0,0,400,950,self.x,self.y)
    def update(self):
        pass
    def get_bb(self):
        return self.x -200, self.y +480, self.x + 200, self.y +440
    def draw_bb(self):
        draw_rectangle(*self.get_bb())