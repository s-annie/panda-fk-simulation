#!/usr/bin/env python3
import math
import numpy as np

def calculate(joint_list):
    s = [math.sin(j) for j in joint_list]
    c = [math.cos(j) for j in joint_list]

    # J1 rotate with z
    ts1 = np.matrix([[c[0], -s[0], 0, 0],
                        [s[0], c[0], 0, 0],
                        [0, 0, 1, 0.333],
                        [0, 0, 0, 1]])
    # J2 rotate with y
    ts2 = np.matrix([[c[1], 0, s[1], 0],
                        [0, 1, 0, 0],
                        [-s[1], 0, c[1], 0],
                        [0, 0, 0, 1]])
    # J3 rotate with z
    ts3 = np.matrix([[c[2], -s[2], 0, 0],
                        [s[2], c[2], 0, 0],
                        [0, 0, 1, 0.316],
                        [0, 0, 0, 1]])
    # J4 rotate with y
    ts4 = np.matrix([[c[3], 0, s[3], 0.0825],
                        [0, 1, 0, 0],
                        [-s[3], 0, c[3], 0],
                        [0, 0, 0, 1]])
    # J5 rotate with z
    ts5 = np.matrix([[c[4], -s[4], 0, -0.0825],
                        [s[4], c[4], 0, 0],
                        [0, 0, 1, 0.384],
                        [0, 0, 0, 1]])
    # J6 rotate with y
    ts6 = np.matrix([[c[5], 0, s[5], 0],
                        [0, 1, 0, 0],
                        [-s[5], 0, c[5], 0],
                        [0, 0, 0, 1]])
    # J7 rotate with z
    ts7 = np.matrix([[c[6], -s[6], 0, 0.088],
                        [s[6], c[6], 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

    tts = ts1*ts2*ts3*ts4*ts5*ts6*ts7
    print(tts[0, 3], tts[1, 3], tts[2, 3])
