from pico2d import *


RUN_SPEED_PPS = 250


current_time = get_time()
def get_frame_time():
    global current_time

    frame_time = get_time() - current_time

    return frame_time

frame_time = get_frame_time()