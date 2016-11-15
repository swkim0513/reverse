from pico2d import*

class Machine_key_extreme():
    global x,y

    def __init__(self):
        self.x = 200
        self.y = 920
        self.image = load_image('machine_key.png')
    def draw(self):
        self.image.clip_draw(0,0,400,80,self.x,self.y)
