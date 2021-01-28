#!/usr/bin/env python
from itertools import permutations
from random import choice, randint
import qrcode


fn = '/home/clover/catkin_ws/src/clover/clover_simulation/resources/worlds/clover.world'
qr_fn = '/home/clover/.gazebo/models/aruco_map_txt/materials/textures/aruco_marker_2_90.png'

rnd_permutation = lambda x: choice(list(permutations(x)))

# QR
qrs = ['yellow','blue','green']
qrcode.make(','.join(rnd_permutation(qrs)) + ',red').save(qr_fn)

# Dronepoints
dps = ["      <uri>model://dronepoint_blue</uri>\n",
"      <uri>model://dronepoint_green</uri>\n",
"      <uri>model://dronepoint_yellow</uri>\n"]
dp = rnd_permutation(dps)

x = randint(52, 88) / 10.0
y = randint(52, 88) / 10.0
dp_4 = '      <pose>{} {} 0 0 0 0</pose>\n'.format(x,y)

with open(fn, 'r') as file:
    data = file.readlines()

data[19] = dp[0]
data[24] = dp[1]
data[29] = dp[2]
data[36] = dp_4

with open(fn, 'w') as file:
    file.writelines( data )

print("Updated. Press any key to exit...")
input()
