from pico2d import *


note_snum = 0
note_dnum = 0
note_fnum = 0
note_spnum = 0
note_jnum = 0
note_knum = 0
note_lnum = 0

note_sy = [1123,2123,3344,4833,5093,6238,7292,8912,9020,12381,11127,12969,13848,14971,15111]
note_dy = [1111,2222,3333,4000,5000,6000,7000,8000,9000,10000]
note_fy = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
note_spy = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
note_jy = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
note_ky = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
note_ly = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

note_s_size = 15
note_d_size = 10
note_f_size = 10
note_sp_size = 10
note_j_size = 10
note_k_size = 10
note_l_size = 10

def note_reset():
    global note_snum,note_dnum,note_fnum,note_spnum,note_jnum,note_knum,note_lnum
    note_snum = 0
    note_dnum = 0
    note_fnum = 0
    note_spnum = 0
    note_jnum = 0
    note_knum = 0
    note_lnum = 0